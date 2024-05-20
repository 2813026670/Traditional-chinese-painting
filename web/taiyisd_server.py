from flask import Flask, render_template, request, make_response
from flask_cors import *
from diffusers import StableDiffusionPipeline
from PIL import Image
import io
import torch

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


@app.route('/taiyisd', methods=['POST'])
def generate_image():
    if request.method == 'POST':

        prompt = request.form.get('prompt')
        image_tensor = pipe(prompt=prompt, guidance_scale=8.5).images[0] 

        if torch.is_tensor(image_tensor) and image_tensor.is_cuda:
            image_tensor = image_tensor.cpu()

        # 将 Tensor 转换为 PIL Image
        if torch.is_tensor(image_tensor):
            pil_image = Image.fromarray((image_tensor.permute(1, 2, 0).numpy() * 255).astype('uint8'))
        else:
            # 如果 pipe 直接返回了 PIL Image，则无需进行任何转换
            pil_image = image_tensor

        # 将 PIL Image 转存为BytesIO对象
        img_bytes = io.BytesIO()
        pil_image.save(img_bytes, format='JPEG')
        img_bytes.seek(0)

        # 创建带有图像内容的HTTP响应
        response = make_response(img_bytes.getvalue())
        response.headers.set('Content-Type', 'image/jpeg')

        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True, port = (5005 + int(device_id)))