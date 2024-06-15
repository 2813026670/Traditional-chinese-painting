import './assets/main.css';

import { createApp } from 'vue';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'; // 确保使用正确的 CSS 文件路径
import App from './App.vue';
import MyInput from './components/MyInput.vue';

const app = createApp(App);

app.component('MyInput', MyInput); // 在使用 ElementPlus 之前注册自定义组件
app.use(ElementPlus); // 集成 ElementPlus

app.mount('#app');