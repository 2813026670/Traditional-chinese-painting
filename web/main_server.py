import base64
import io
import json
from tkinter import Image
import uuid
import pandas as pd
import math
import cv2
import numpy as np
from sklearn.cluster import KMeans
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from PIL import Image
import base64
from flask import Flask, jsonify, render_template, request, make_response
from flask_cors import *
from diffusers import StableDiffusionPipeline
from PIL import Image
import io
import torch
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

app = Flask(__name__)
CORS(app, supports_credentials=True)
# device_id = sys.argv[1]
# device = "cuda:" + device_id
device_id = 0
device = "cuda:0"
print(device)

model_dir = "D:\hf_out_4_2430"
pipe = StableDiffusionPipeline.from_pretrained(model_dir, torch_dtype=torch.float16).to(device)
print("Set device")
# pipe = pipe.to(device)
print("Start inference")


UPLOAD_FOLDER = 'uploads'  # 定义上传文件的目录
if not os.path.exists(UPLOAD_FOLDER):  # 如果目录不存在，则创建目录
    os.makedirs(UPLOAD_FOLDER)

def ColourDistance(rgb1, rgb2):
    rmean = (rgb1[0] + rgb2[0]) / 2
    r = rgb1[0] - rgb2[0]
    g = rgb1[1] - rgb2[1]
    b = rgb1[2] - rgb2[2]
    d = math.sqrt((2 + rmean / 256) * (r ** 2) + 4 * (g ** 2) + (2 + (255 - rmean) / 256) * (b ** 2))
    return d

def create_color_palette(image_path, num_colors):
    # 加载图像并转换为RGB格式
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 使用FT算法计算显著性图
    saliency_ft = cv2.saliency.StaticSaliencyFineGrained_create()
    (success, saliency_map_ft) = saliency_ft.computeSaliency(image)
    saliency_map_ft = (saliency_map_ft * 255).astype("uint8")

    # 将显著性图转换为二值图像
    _, thresh_map = cv2.threshold(saliency_map_ft, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 对二值显著性图和原始图像执行按位AND操作
    salient_image = cv2.bitwise_and(image, image, mask=thresh_map)

    # 将显著图像转换为RGB值数组
    salient_image_array = np.float32(salient_image.reshape(-1, 3))

    # 对图像数组执行k-means聚类
    kmeans = KMeans(n_clusters=num_colors, init='k-means++', n_init=100, random_state=0)
    kmeans.fit(salient_image_array)

    # 获取前num_colors个聚类中心
    top_colors = kmeans.cluster_centers_.astype(int)

    # 将RGB值转换为十六进制颜色代码
    hex_codes = ['#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2]) for color in top_colors]

    # 计算图像中每种颜色的百分比
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    color_percents = (counts / len(salient_image_array)) * 100

    # 按颜色频率对颜色和百分比进行排序
    sorted_indices = np.argsort(color_percents)[::-1]
    sorted_colors = [hex_codes[i] for i in sorted_indices]
    sorted_percents = color_percents[sorted_indices]

    return sorted_colors[:num_colors], sorted_percents[:num_colors]

def find_closest_color(colors_palette):
    with open("colors1.json", "r", encoding="utf-8", errors="ignore") as file:
        rgb_dict = json.load(file)

    color_names = []
    color_rgb = []
    for color_str in colors_palette:
        # Convert color string to RGB
        red = int(color_str[1:3], 16)
        green = int(color_str[3:5], 16)
        blue = int(color_str[5:7], 16)
        rgb_color = (red, green, blue)

        min_distance = float("inf")
        closest_color_name = ""

        for rgb_info in rgb_dict:
            rgb = "#" + rgb_info["rgb"]
            if len(rgb) == 7:
                red = int(rgb[1:3], 16)
                green = int(rgb[3:5], 16)
                blue = int(rgb[5:7], 16)
                dec_num = (red, green, blue)
                distance = ColourDistance(dec_num, rgb_color)
                if distance < min_distance:
                    min_distance = distance
                    closest_color_name = rgb_info["name"]
                    closest_color_rgb = rgb_info["rgb"]
        color_names.append(closest_color_name)
        color_rgb.append(closest_color_rgb)
    return color_names , color_rgb

@app.route('/get_palette', methods=['POST'])
def get_palette():
    prompt = request.json.get('prompt')

    # 从另一个接口获取图像数据
    image_response = requests.post('http://127.0.0.1:5001/taiyisd', data={'prompt': prompt})
    if image_response.status_code == 200:
        image_data_list = image_response.json().get('images', [])
        palettes = []

        for image_base64_str in image_data_list:
            # 解码 base64 编码的图像数据
            image_data = base64.b64decode(image_base64_str)

            # 将图像数据转换为 PIL Image 对象
            pil_image = Image.open(io.BytesIO(image_data))

            # 将 PIL Image 转存为临时文件
            image_path = os.path.join(UPLOAD_FOLDER, 'generated_image.png')
            pil_image.save(image_path)

            # 提取颜色调色板
            num_colors = 9
            colors, percents = create_color_palette(image_path, num_colors)

            # 寻找最接近的颜色名称
            color_names, color_rgb = find_closest_color(colors)

            # 转换调色板信息为基本数据类型
            palette = {'color_names': color_names, 'color_rgb': color_rgb}
            
            # 将生成的图片转换为 base64 编码的字符串
            img_base64_str = base64.b64encode(image_data).decode('utf-8')
            
            # 创建带有图像内容的JSON响应
            response_data = {'palette': palette, 'image': img_base64_str}
            palettes.append(response_data)

            # 删除临时图像文件
            os.remove(image_path)

        # 返回所有颜色调色板
        return jsonify(palettes)
    else:
        return jsonify({'error': 'Failed to fetch images from the other API'})
    

@app.route('/taiyisd', methods=['POST'])
def generate_image():
    if request.method == 'POST':
        
        prompt = request.form.get('prompt')
#         image_tensor = pipe(prompt=prompt, guidance_scale=8.5).images[0] 

#         if torch.is_tensor(image_tensor) and image_tensor.is_cuda:
#             image_tensor = image_tensor.cpu()

# # 将 Tensor 转换为 PIL Image
#         if torch.is_tensor(image_tensor):
#             pil_image = Image.fromarray((image_tensor.permute(1, 2, 0).numpy() * 255).astype('uint8'))
#         else:
#     # 如果 pipe 直接返回了 PIL Image，则无需进行任何转换
#             pil_image = image_tensor

#         # 将 PIL Image 转存为BytesIO对象
#         img_bytes = io.BytesIO()
#         pil_image.save(img_bytes, format='JPEG')
#         img_bytes.seek(0)

#         # 创建带有图像内容的HTTP响应
#         response = make_response(img_bytes.getvalue())
#         response.headers.set('Content-Type', 'image/jpeg')

#         return response
        image_list = []

        for i in range(9):
            image_tensor = pipe(prompt=prompt, guidance_scale=8.5).images[0]

            if torch.is_tensor(image_tensor) and image_tensor.is_cuda:
                image_tensor = image_tensor.cpu()

            # 将张量转换为PIL图像
            if torch.is_tensor(image_tensor):
                pil_image = Image.fromarray((image_tensor.permute(1, 2, 0).numpy() * 255).astype('uint8'))
            else:
                pil_image = image_tensor

            # 将PIL图像转换为字节流
            img_bytes = io.BytesIO()
            pil_image.save(img_bytes, format='JPEG')
            img_bytes.seek(0)

            # 将字节流转换为base64编码的字符串
            base64_str = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

            # 将base64编码的字符串存储到列表中
            image_list.append(base64_str)

        return jsonify({'images': image_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True, port=5001)
 