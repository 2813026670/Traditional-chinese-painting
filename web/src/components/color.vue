<template>
    <div>
        <input type="file" @change="handleFileUpload" />
        <button @click="sendRequestResult" :disabled="!roomId">请求处理结果</button>
        <button @click="getProcessedImage" :disabled="!resultId">查看处理结果图片</button>
        <img :src="processedImage" alt="Processed Image" v-if="processedImage">
        <p>房间ID: {{ roomId }}</p>
        <p>处理结果ID: {{ resultId }}</p>
        <p v-if="errorMessage" style="color:red;">错误提示: {{ errorMessage }}</p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            roomId: null,
            resultId: null,
            selectedFile: null,
            processedImage: null,
            errorMessage: '', // 新增错误信息状态
        };
    },
    methods: {
        handleFileUpload() {
            const file = event.target.files[0];
            if (file) {
                if (this.validateFileType(file)) { // 添加文件类型验证
                    this.selectedFile = file;
                    this.uploadSketch();
                } else {
                    this.errorMessage = '只支持图片文件上传！';
                }
            } else {
                this.errorMessage = '请选择一个文件！';
            }
        },
        validateFileType(file) { // 文件类型验证函数
            const allowedTypes = ['image/png'];
            return allowedTypes.includes(file.type);
        },
        uploadSketch() {
            const formData = new FormData();
            formData.append('sketch', this.selectedFile);

            axios.post('/upload_sketch', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(response => {
                    this.roomId = response.data.roomId;
                    this.errorMessage = ''; // 清除错误信息
                })
                .catch(error => {
                    this.errorMessage = '上传草图失败，请重试！';
                    console.error(error);
                });
        },
        sendRequestResult() {
            axios.post('/request_result', {
                room: this.roomId
            })
                .then(response => {
                    this.resultId = response.data;
                    this.errorMessage = ''; // 清除错误信息
                })
                .catch(error => {
                    this.errorMessage = '请求处理结果失败，请检查房间ID和参数！';
                    console.error(error);
                });
        },
        getProcessedImage() {
            axios.post('/get_processed_image', { resultId: this.resultId }, {
                responseType: 'arraybuffer',
            })
                .then(response => {
                    const base64String = btoa(new Uint8Array(response.data).reduce((data, byte) => data + String.fromCharCode(byte), ''));
                    this.processedImage = `data:image/png;base64,${base64String}`;
                    this.errorMessage = ''; // 清除错误信息
                })
                .catch(error => {
                    this.errorMessage = '获取处理结果图片失败，请重试！';
                    console.error(error);
                }),
  }
    }
}
</script>