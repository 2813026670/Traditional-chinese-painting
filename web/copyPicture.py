from flask import Flask, jsonify
import os
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:5173']) 

app = Flask(__name__)

def get_latest_subfolder(parent_folder):
    """ 获取最新子文件夹的路径 """
    subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]
    latest_subfolder = max(subfolders, key=os.path.getmtime)
    return latest_subfolder

def encode_images_to_base64(folder_path):
    """ 将指定文件夹下的所有图片转换为Base64编码 """
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    images_base64 = []

    for img_file in image_files:
        with open(os.path.join(folder_path, img_file), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            images_base64.append(encoded_string)
    return images_base64

@app.route('/get_latest_images', methods=['GET'])
def get_latest_images():
    parent_folder = 'D:/BaiduNetdiskDownload/S2P官方配布/style2paints45beta1214B/style2paints45beta1214B/assets/game/rooms'  # 替换为你的父文件夹路径
    latest_subfolder = get_latest_subfolder(parent_folder)
    images_base64 = encode_images_to_base64(latest_subfolder)
    
    # 输出Base64数组到控制台
    print("Base64 Encoded Images:", images_base64)
    
    return jsonify({"images": images_base64})

if __name__ == '__main__':
    app.run(debug=True)