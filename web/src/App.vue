<script>
import { ref } from 'vue'
import axios from 'axios';
import MyInput from './components/MyInput.vue';
import ColorPalette from './components/ColorPalette.vue';
export default {
  components: {
    MyInput,

  },

  data() {
    return {
      feedbackArray: [],
      msg: "TcpColor",
      box: "container",
      topbox: "title",
      texttitle: "text",
      mainbox: "main",
      leftbox: "left",
      middlebox: "middle",
      middleTopbox: "middle-top",
      middleBottombox: "middle-bottom",
      rightbox: "right",

      inputValue: '',
      selected1: [],
      options1: [
        { value: '花鸟', label: '花鸟' },
        { value: '山水', label: '山水' },
        { value: '人物', label: '人物' }
      ],
      feedback1: [],

      selected2: [],
      options2: [
        { value: '气韵', label: '气韵' },
        { value: '神妙', label: '神妙' },
        { value: '高古', label: '高古' },
        { value: '苍润', label: '苍润' },
        { value: '沉雄', label: '沉雄' },
        { value: '冲和', label: '冲和' },
        { value: '澹远', label: '澹远' },
        { value: '朴拙', label: '朴拙' },
        { value: '超脱', label: '超脱' },
        { value: '奇辟', label: '奇辟' },
        { value: '纵横', label: '纵横' },
        { value: '淋漓', label: '淋漓' },
        { value: '荒寒', label: '荒寒' },
        { value: '清旷', label: '清旷' },
        { value: '性灵', label: '性灵' },
        { value: '圆浑', label: '圆浑' },
        { value: '幽遂', label: '幽遂' },
        { value: '明净', label: '明净' },
        { value: '健拔', label: '健拔' },
        { value: '简洁', label: '简洁' },
        { value: '精谨', label: '精谨' },
        { value: '儁爽', label: '儁爽' },
        { value: '空灵', label: '空灵' },
        { value: '韶秀', label: '韶秀' },
      ],
      feedback2: [],

      selected3: [],
      options3: [{ 'value': '画作', 'label': '画作' }, { 'value': '鸟', 'label': '鸟' }, { 'value': '树枝', 'label': '树枝' }, { 'value': '竹', 'label': '竹' }, { 'value': '印章', 'label': '印章' }, { 'value': '花', 'label': '花' }, { 'value': '月亮', 'label': '月亮' }, { 'value': '山石', 'label': '山石' }, { 'value': '日', 'label': '日' }, { 'value': '车', 'label': '车' }, { 'value': '芦苇', 'label': '芦苇' }, { 'value': '藻', 'label': '藻' }, { 'value': '鸭', 'label': '鸭' }, { 'value': '兰', 'label': '兰' }, { 'value': '伞', 'label': '伞' }, { 'value': '舟船', 'label': '舟船' }, { 'value': '桥', 'label': '桥' }, { 'value': '荷叶', 'label': '荷叶' }, { 'value': '鸳鸯', 'label': '鸳鸯' }, { 'value': '云', 'label': '云' }, { 'value': '篮', 'label': '篮' }, { 'value': '作品屏风', 'label': '作品屏风' }, { 'value': '马', 'label': '马' }, { 'value': '坡', 'label': '坡' }, { 'value': '鸟', 'label': '鸟' }, { 'value': '草', 'label': '草' }, { 'value': '山', 'label': '山' }, { 'value': '船', 'label': '船' }, { 'value': '蔬菜', 'label': '蔬菜' }, { 'value': '月', 'label': '月' }, { 'value': '石', 'label': '石' }, { 'value': '果', 'label': '果' }, { 'value': '荷', 'label': '荷' }, { 'value': '鹅', 'label': '鹅' }, { 'value': '梅', 'label': '梅' }, { 'value': '鱼', 'label': '鱼' }, { 'value': '灵芝', 'label': '灵芝' }, { 'value': '屏风', 'label': '屏风' }, { 'value': '驴', 'label': '驴' }, { 'value': '叶', 'label': '叶' }, { 'value': '树木', 'label': '树木' }, { 'value': '龙', 'label': '龙' }, { 'value': '竹篮', 'label': '竹篮' }, { 'value': '虫', 'label': '虫' }, { 'value': '题跋', 'label': '题跋' }, { 'value': '瀑布', 'label': '瀑布' }, { 'value': '人物', 'label': '人物' }, { 'value': '假山', 'label': '假山' }, { 'value': '马车', 'label': '马车' }, { 'value': '亭台', 'label': '亭台' }, { 'value': '画作屏风', 'label': '画作屏风' }, { 'value': '楼阁', 'label': '楼阁' }, { 'value': '水', 'label': '水' }, { 'value': '菊', 'label': '菊' }, { 'value': '走兽', 'label': '走兽' }, { 'value': '马鞍', 'label': '马鞍' }, { 'value': '车轿', 'label': '车轿' }, { 'value': '鸡', 'label': '鸡' }, { 'value': '松', 'label': '松' }],
      feedback3: [],

      selected4: [],
      options4: [{ 'value': '行云流水描', 'label': '行云流水描' }, { 'value': '浓淡相间法', 'label': '浓淡相间法' }, { 'value': '解索皴', 'label': '解索皴' }, { 'value': '泼墨泼彩法', 'label': '泼墨泼彩法' }, { 'value': '双勾法（写意）', 'label': '双勾法（写意）' }, { 'value': '蚂蝗描', 'label': '蚂蝗描' }, { 'value': '勾填法（写意）', 'label': '勾填法（写意）' }, { 'value': '米点皴', 'label': '米点皴' }, { 'value': '斧劈皴', 'label': '斧劈皴' }, { 'value': '没骨法（写意）', 'label': '没骨法（写意）' }, { 'value': '高古游丝描', 'label': '高古游丝描' }, { 'value': '折芦描', 'label': '折芦描' }, { 'value': '勾染法（写意）', 'label': '勾染法（写意）' }, { 'value': '工笔淡彩法', 'label': '工笔淡彩法' }, { 'value': '破墨破色法（写意）', 'label': '破墨破色法（写意）' }, { 'value': '折带皴', 'label': '折带皴' }, { 'value': '乱柴皴', 'label': '乱柴皴' }, { 'value': '披麻皴', 'label': '披麻皴' }, { 'value': '混描', 'label': '混描' }, { 'value': '兼工带写法', 'label': '兼工带写法' }, { 'value': '没骨法（工笔）', 'label': '没骨法（工笔）' }, { 'value': '曹衣描', 'label': '曹衣描' }, { 'value': '弹涡皴', 'label': '弹涡皴' }, { 'value': '雨点皴', 'label': '雨点皴' }, { 'value': '没骨法', 'label': '没骨法' }, { 'value': '双勾法', 'label': '双勾 法' }, { 'value': '枯柴描', 'label': '枯柴描' }, { 'value': '钉头鼠尾描', 'label': '钉头鼠尾描' }, { 'value': '铁线描', 'label': '铁线描' }, { 'value': '白 描法', 'label': '白描法' }, { 'value': '蚯蚓描', 'label': '蚯蚓描' }, { 'value': '破墨破色法', 'label': '破墨破色法' }, { 'value': '浓淡相间法（工笔）', 'label': '浓淡相间法（工笔）' }, { 'value': '白描法（工笔）', 'label': '白描法（工笔）' }, { 'value': '枣核描', 'label': '枣核描' }, { 'value': '柳叶描', 'label': '柳叶描' }, { 'value': '琴弦描', 'label': '琴弦描' }, { 'value': '镢头钉描', 'label': '镢头钉描' }, { 'value': '工笔重彩法', 'label': '工笔重彩法' }, { 'value': '马牙皴', 'label': '马牙皴' }, { 'value': '战笔水纹描', 'label': '战笔水纹描' }, { 'value': '牛毛皴', 'label': '牛毛皴' }, { 'value': '勾染法', 'label': '勾染法' }, { 'value': '竹叶描', 'label': '竹叶描' }, { 'value': '卷云皴', 'label': '卷云皴' }, { 'value': '荷叶皴', 'label': '荷叶皴' }, { 'value': '泼墨泼彩法（写意）', 'label': '泼墨泼彩法（写意）' }, { 'value': '拖泥带水皴', 'label': '拖泥带水皴' }, { 'value': '减笔描', 'label': '减笔描' }, { 'value': '泼墨', 'label': '泼墨' }, { 'value': '勾填法', 'label': '勾填法' }],
      feedback4: [],

      selected5: [],
      options5: [{ 'value': '重彩-金碧', 'label': '重彩-金碧' }, { 'value': '吴妆', 'label': '吴妆' }, { 'value': '水墨', 'label': '水墨' }, { 'value': '白描', 'label': '白描' }, { 'value': '浅设色', 'label': '浅设色' }, { 'value': '淡彩-螺青', 'label': '淡彩-螺青' }, { 'value': '淡彩', 'label': '淡彩' }, { 'value': '设色、 描金', 'label': '设色、描金' }, { 'value': '重彩-青绿', 'label': '重彩-青绿' }, { 'value': '重彩', 'label': '重彩' }, { 'value': '设色', 'label': '设色' }, { 'value': '淡彩-浅绛', 'label': '淡彩-浅绛' }],
      feedback5: [],
      images: [],
      images2: [
        '../图片/OIP-1.jpg',
        '图片/OIP-2.jpg',
        '图片/OIP-3.jpg',
        '图片/OIP-4.jpg',
        '图片/OIP-5.jpg',
        '图片/OIP-6.jpg',
        '图片/OIP-7.jpg',
        '图片/OIP-8.jpg',
        '图片/OIP-9.jpg'
      ],//测试图片显示
      tiaoseimages: [],
      tiaoseimages2: [
        '../图片/OIP-1.jpg',
        '图片/OIP-2.jpg',
        '图片/OIP-3.jpg',

      ],
      prompts: [],
      feedbackImage: [],
      feedbackKeywords: [],

      selectedColorGroup: '', // 初始未选择任何色系  
      selectedMonoColor: '', // 初始未选择单色系中的颜色  
      fiveColors: [
        { name: '青', color: 'rgb(3,0,249)' },
        { name: '赤', color: 'red' },
        { name: '白', color: 'white' },
        { name: '黑', color: 'black' },
        { name: '黄', color: 'yellow' },
      ],
      monoColors: ['青', '赤', '白/黑', '黄'], // 单色系的颜色名  
      colorNames: [],
      colorNames2: [],
      colorRGBs: [],
      colorRGBs2: null,
      imageBase64s: [],
      palettearray: [],
      testcolorRGB: [],
      testcolorRGB2: [],
      testcolorNAMES: [],
      currentPaletteIndex: null,

      selectColorNumberArray: '',
      colorNumber: [
        { value: '3', label: '3' },
        { value: '5', label: '5' },
      ],
      SelectedColorNumber: '',
      OneOrFiveColored: '',

      listData: ["原图配色方案", "推荐配色方案"],
      activeIndex: null,

      roomId: null,
      resultId: null,

      copyimagesHome: 'D:/BaiduNetdiskDownload/S2P官方配布/style2paints45beta1214B/style2paints45beta1214B/assets/game/rooms/',
      copyimages: '',

      selectedFile: null,
      processedImage: null,
      errorMessage: '', // 新增错误信息状态
      base64Image: null,
      base64Content: null,

      showModal: false, // 控制弹窗的显示与隐藏  
      roomimages: [],

      displayedImages: [], // 这里将存放显示的8张图片

      displayedImages1: [],// 这里将存放第1~8张图片
      displayedImages2: [],
      displayedImages3: [],
      displayedImages4: [],
      displayedImages5: [],

      currentRoom: localStorage.getItem('currentRoom') || '',
    }
  },



  setup() {


    const checked1 = ref('1');
    const checked2 = ref(false);
    const radio1 = ref('1');
    return { checked1, checked2, radio1 };
  },

  methods: {
    handlechange1(value) {
      this.feedback1 = value;
    },
    handledelete1(index) {
      this.feedback1.splice(index, 1);
    },

    handlechange2(value) {
      this.feedback2 = value;
    },
    handledelete2(index) {
      this.feedback2.splice(index, 1);
    },

    handlechange3(value) {
      this.feedback3 = value;
    },
    handledelete3(index) {
      this.feedback3.splice(index, 1);
    },

    handlechange4(value) {
      this.feedback4 = value;
    },
    handledelete4(index) {
      this.feedback4.splice(index, 1);
    },

    handlechange5(value) {
      this.feedback5 = value;
    },
    handledelete5(index) {
      this.feedback5.splice(index, 1);
    },

    hasFeedback() {
      return (
        this.feedback1.length > 0 ||
        this.feedback2.length > 0 ||
        this.feedback3.length > 0 ||
        this.feedback4.length > 0 ||
        this.feedback5.length > 0 ||
        this.inputValue > 0
      );
    },

    generateImages() {
      //this.prompts = this.feedbackArray;
      this.prompts = [this.feedback1, this.feedback2, this.feedback3, this.feedback4, this.feedback5, '色系', this.inputValue];
    },
    testTiaoseFunction() {
      this.tiaoseimages = this.tiaoseimages2;
    },

    FiveColorSelectFunction() {
      this.OneOrFiveColored = "五色系";
    },
    OneColorSelectFunction(monoColor) {
      this.OneOrFiveColored = monoColor + "色系";
    },

    OneOrFiveColorSelectFunction() {
      this.prompts.splice(5, 1, this.OneOrFiveColored);
    },

    sendPostRequest() {
      axios.post('/get_palette', {
        prompt: this.prompts
      },
        {
          timeout: 500000 // 设置 5 秒的超时时间  
        })
        .then(response => {
          const palettesData = response.data; // 假设 response.data 是调色板信息的数组  

          // 初始化数组  
          this.colorNames = [];
          this.colorRGBs = [];
          this.imageBase64s = [];

          // 遍历调色板数据  
          palettesData.forEach(item => {
            const { palette, image } = item;
            const { color_names, color_rgb } = palette;
            // 将颜色名称、颜色 RGB 值和图片 base64 编码分别添加到数组中
            this.palettearray = this.palettearray.concat(palette);
            this.colorNames.push(color_names);
            this.colorRGBs.push(color_rgb);
            this.imageBase64s.push(image);


            this.images = this.imageBase64s.map(base64 => {
              // 假设所有图片都是PNG格式  
              return `data:image/png;base64,${base64}`;
            });
          });
        })
        .catch(error => {
          console.error('发送请求失败:', error);
        });
    },

    showPaletteNames(index) {
      this.currentPaletteIndex = index;
    },//显示颜色方案名字
    hidePaletteNames() {
      this.currentPaletteIndex = null;
    },//隐藏颜色方案名字

    selectColorNumber(value) {
      this.SelectedColorNumber = value;
    },

    extractColor(paletteIndex) {
      // 清空 testcolorRGB 和 testcolorNAMES 数组
      this.testcolorRGB = [];
      this.testcolorNAMES = [];

      // 获取当前调色板的颜色值和名称
      const colors = this.colorRGBs[paletteIndex];
      const colorNames = this.colorNames[paletteIndex];

      // 根据 SelectedColorNumber 的值和颜色数组的实际长度确定处理颜色的最大数量
      const limit = Math.min(this.SelectedColorNumber, colors.length);

      // 迭代颜色，最多迭代到 limit 指定的数量，将颜色转换为十六进制格式，并存储对应的名称
      for (let i = 0; i < limit; i++) {
        const hexColor = '#' + colors[i].toString(16).padStart(6, '0');
        this.testcolorRGB.push(hexColor);
        this.testcolorNAMES.push(colorNames[i]);
      }

      // 更新当前选中的调色板索引
      this.currentPaletteIndex = paletteIndex;
    },

    imageButtomFunction() {
      this.generateImages();
      this.OneOrFiveColorSelectFunction();
      this.sendPostRequest();
    },
    updateColorNames() {
      this.SelectedColorNumber = 9;
    },
    changeColor(index) {
      this.activeIndex = index;
      if (index === 0) {
        this.updateColorNames();
      } else if (index === 1) {
        this.colorNames2 = this.sortByContrast(this.colorNames);
      }
    },

    //重新排序
    meanColor(row) {
      // 将行转换为 RGB 值数组
      const rgbValues = row.map(color =>
        [parseInt(color.substring(0, 2), 16),
        parseInt(color.substring(2, 4), 16),
        parseInt(color.substring(4, 6), 16)]
      );

      // 计算平均 RGB 值
      const meanRGB = rgbValues.reduce((acc, val) =>
        acc.map((sum, i) => sum + val[i]),
        [0, 0, 0]
      ).map(value => Math.floor(value / rgbValues.length));

      // 转换回十六进制字符串
      return '#' + meanRGB.map(val => val.toString(16).padStart(2, '0')).join('');
    },
    darkestColor(array) {
      let darkestHex = '#ffffff';
      let darkestValue = Infinity;

      for (let row of array) {
        for (let color of row) {
          let rgbSum = parseInt(color.substring(0, 2), 16) +
            parseInt(color.substring(2, 4), 16) +
            parseInt(color.substring(4, 6), 16);

          if (rgbSum < darkestValue) {
            darkestValue = rgbSum;
            darkestHex = color;
          }
        }
      }

      return darkestHex;
    },
    euclideanDistance(color1, color2) {
      const rmean = (parseInt(color1.substring(1, 3), 16) + parseInt(color2.substring(1, 3), 16)) / 2;
      const r = parseInt(color1.substring(1, 3), 16) - parseInt(color2.substring(1, 3), 16);
      const g = parseInt(color1.substring(3, 5), 16) - parseInt(color2.substring(3, 5), 16);
      const b = parseInt(color1.substring(5, 7), 16) - parseInt(color2.substring(5, 7), 16);

      // 使用感知加权欧几里得距离公式
      return Math.sqrt((2 + rmean * 0.0039) * (r ** 2) + 4 * (g ** 2) + (2 + (255 - rmean) * 0.0075) * (b ** 2));
    },
    sortByContrast(array) {
      const darkest = this.darkestColor(array);
      const distances = array.map(row => ({
        row,
        distance: this.euclideanDistance(this.meanColor(row), darkest)
      }));

      return distances.sort((a, b) => b.distance - a.distance).map(item => item.row);
    },
    sortColors() {
      this.colorRGBs2 = this.sortByContrast(this.colorNames);
    },


    //图片上传
    handleFileUpload() {
      const file = event.target.files[0];
      if (file) {
        if (this.validateFileType(file)) { // 添加文件类型验证
          this.selectedFile = file;
          const reader = new FileReader();
          // 定义 FileReader 加载完成后的处理函数  
          reader.onload = (e) => {
            this.base64Image = e.target.result;
            this.base64Content = this.base64Image.replace(/^data:image\/[^;]+;base64,/, "");
            this.uploadSketch();
          }; reader.readAsDataURL(file);
        } else {
          this.errorMessage = '只支持PNG图片文件上传！';
        }
      } else {
        this.errorMessage = '请选择一个文件！';
      }
    },
    validateFileType(file) { // 文件类型验证函数
      const allowedTypes = ['image/png'];
      return allowedTypes.includes(file.type);
    },
    //第一个接口，得到roomID
    uploadSketch() {
      const formData = new FormData();
      formData.append('sketch', this.base64Content);
      axios.post('http://127.0.0.1:8233/upload_sketch', formData, {
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
    //第二个接口，得到返回ID
    sendRequestResult() {
      axios.post('http://127.0.0.1:8233/request_result', {
        room: this.roomId
      })
        .then(response => {
          this.resultId = response.data.resultId;
          this.errorMessage = ''; // 清除错误信息
        })
        .catch(error => {
          this.errorMessage = '请求处理结果失败，请检查房间ID和参数！';
          console.error(error);
        });
    },
    //第三个接口，得到图片base64
    getProcessedImage() {
      axios.post('http://127.0.0.1:8233/get_processed_image', { resultId: this.resultId }, {
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
        });
    },

    goToExternalPage() {
      window.open('http://127.0.0.1:8233/index.html', '_blank');   //跳转到另一个页面
      //window.open('http://localhost:5173/', '_blank');
    },

    fetchImages() {
      //this.copyimages = `${this.copyimagesHome}${this.resultId}`
      this.copyimages = `${this.copyimagesHome}${tupian}`
    },


    generateAndShowImage() {
      this.drawColorGrid(this.$refs.colorCanvas);
    },
    drawColorGrid(canvas) {
      const ctx = canvas.getContext('2d');
      const colors = this.testcolorRGB;
      const cellSize = 100;
      const rows = Math.ceil(colors.length / 3); // 每行最多显示6个色块
      const cols = Math.min(colors.length, 3);

      for (let i = 0; i < colors.length; i++) {
        const row = Math.floor(i / cols);
        const col = i % cols;
        const x = col * cellSize;
        const y = row * cellSize;

        ctx.fillStyle = colors[i];
        ctx.fillRect(x, y, cellSize, cellSize);
      }
    },
    saveImage() {  
      const canvas = this.$refs.colorCanvas;  
      if (canvas.toDataURL) {  
        // 创建一个链接元素  
        const link = document.createElement('a');  
        link.download = 'color-grid.png'; // 指定下载文件名  
        link.href = canvas.toDataURL('image/png').replace("image/png", "image/octet-stream"); // 使用replace替换MIME类型以确保兼容性  
        link.click(); // 模拟点击进行下载  
  
        // 清理（可选）  
        // document.body.removeChild(link);  
      } else {  
        console.error('Canvas.toDataURL() is not supported.');  
      }  
    },  


    async fetchAndDisplayImages() {
      try {
        const response = await axios.get('/get_latest_images');
        this.roomimages = response.data.images.map(image => `data:image/png;base64,${image}`);
        //this.roomimages = response.data.images;
        console.log(this.roomimages);
        this.displayedImages1 = this.roomimages.slice(0, 8); // 取前8张图片,为第一组
        this.displayedImages2 = this.roomimages.slice(8, 16); // 取第9~16图片,为第二组
        this.displayedImages3 = this.roomimages.slice(16, 24);
        this.displayedImages4 = this.roomimages.slice(24, 32);
        this.displayedImages5 = this.roomimages.slice(32, 40);
        this.displayedImages = this.displayedImages1;
        console.log(this.displayedImages2);
      } catch (error) {
        console.error('Failed to fetch images:', error);
      }
    },

    getImageSrc(base64String) {
      // 确定图像类型，这里假定所有图像都是PNG
      return `data:image/png;base64,${base64String}`;
    },

    SetdisplayedImages1() {
      this.displayedImages = this.displayedImages1;
    },
    SetdisplayedImages2() {
      this.displayedImages = this.displayedImages2;
      this.$forceUpdate(); 
    },
    SetdisplayedImages3() {
      this.displayedImages = this.displayedImages3;
    },
    SetdisplayedImages4() {
      this.displayedImages = this.displayedImages4;
    },
    SetdisplayedImages5() {
      this.displayedImages = this.displayedImages5;
    },

  },



  watch: {
    SelectedColorNumber(newVal, oldVal) {
      console.log(newVal, oldVal);
      for (let i = 0; i < this.colorNames.length; i++) {
        this.colorNames2[i] = this.colorNames[i].slice(0, newVal);
      };
    }
  },


  computed: {
    TextFeedback1() {//选择框1的文本反馈信息
      return this.feedback1.length > 0 ? this.TextFeedback1 = this.feedback1.join('、') : '';
    },
    TextFeedback2() {
      return this.feedback2.length > 0 ? this.TextFeedback2 = this.feedback2.join('、') : '';
    },
    TextFeedback3() {
      return this.feedback3.length > 0 ? this.TextFeedback3 = this.feedback3.join('、') : '';
    },
    TextFeedback4() {
      return this.feedback4.length > 0 ? this.TextFeedback4 = this.feedback4.join('、') : '';
    },
    TextFeedback5() {
      return this.feedback5.length > 0 ? this.TextFeedback5 = this.feedback5.join('、') : '';
    },
    feedbackStr2() {
      let feedbackStr = '此图为传统中国画';
      if (this.TextFeedback1) feedbackStr += `,类型为${this.TextFeedback1}`;
      if (this.TextFeedback2) feedbackStr += `,意境为${this.TextFeedback2}`;
      if (this.TextFeedback3) feedbackStr += `,物象为${this.TextFeedback3}`;
      if (this.TextFeedback4) feedbackStr += `,技法为${this.TextFeedback4}`;
      if (this.TextFeedback5) feedbackStr += `,赋彩为${this.TextFeedback5}`;
      //if (this.OneOrFiveColored) feedbackStr += `,色系为${this.OneOrFiveColored}`;
      return feedbackStr;
    },
    feedbackArray() {
      return [this.feedbackStr2]; // 确保返回一个数组

    },

  }
}

</script>

<template>
  <div v-bind:class="box">
    <div v-bind:class="topbox">
      <span v-bind:class="texttitle"> TcpColor </span>
    </div>
    <div v-bind:class="mainbox">
      <div v-bind:class="leftbox">
        <div class="leftTitle" style="display:flex; align-items:center;">
          <span style="color:#675229;font-size: 34px;">🅐</span>
          <span v-bind:id="texttitle" style="color:#95815c;font-size: 18px;">控制面板</span>
        </div>
        <!--

        反馈框
        <div class="feedback">
          <div class="feedback1" v-if="feedback1.length > 0">
            <div class="feedback-option1" v-for="(item, index) in feedback1" :key="index">
              {{ item }}
              <button class="feed-button1" @click="handledelete1(index)">✖</button>
            </div>
          </div>

          <div class="feedback2" v-if="feedback2.length > 0">
            <div class="feedback-option2" v-for="(item, index) in feedback2" :key="index">
              {{ item }}
              <button class="feed-button2" @click="handledelete2(index)">✖</button>
            </div>
          </div>


          <div class="feedback3" v-if="feedback3.length > 0">
            <div class="feedback-option3" v-for="(item, index) in feedback3" :key="index">
              {{ item }}
              <button class="feed-button3" @click="handledelete3(index)">✖</button>
            </div>
          </div>

          <div class="feedback4" v-if="feedback4.length > 0">
            <div class="feedback-option4" v-for="(item, index) in feedback4" :key="index">
              {{ item }}
              <button class="feed-button4" @click="handledelete4(index)">✖</button>
            </div>
          </div>

          <div class="feedback5" v-if="feedback5.length > 0">
            <div class="feedback-option5" v-for="(item, index) in feedback5" :key="index">
              {{ item }}
              <button class="feed-button5" @click="handledelete5(index)">✖</button>
            </div>
          </div>
        </div>
        -->
        <div>
          <!-- 使用组件 -->
          <my-input v-model="inputValue" id="my-input" type="text" label="" placeholder="输入"
            style="margin-bottom: 2px;"></my-input>
        </div>

        <!--选择框-->
        <div class="select">
          <div class="select1">
            <el-select v-model="selected1" placeholder="主题" multiple fallback-placements="top-start"
              @change="handlechange1">
              <el-option v-for="item in options1" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>

          <div class="select2">
            <el-select v-model="selected2" placeholder="意境" multiple fallback-placements="top-start"
              @change="handlechange2">
              <el-option v-for="item in options2" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>

          <div class="select3">
            <el-select v-model="selected3" placeholder="物象" multiple fallback-placements="top-start"
              @change="handlechange3">
              <el-option v-for="item in options3" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>

          <div class="select4">
            <el-select v-model="selected4" placeholder="技法" multiple fallback-placements="top-start"
              @change="handlechange4">
              <el-option v-for="item in options4" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>

          <div class="select5">
            <el-select v-model="selected5" placeholder="赋彩" multiple fallback-placements="top-start"
              @change="handlechange5">
              <el-option v-for="item in options5" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>



        <div class="color-selector-container">
          <div class="color-selector">
            <el-radio-group v-model="selectedColorGroup" class="radio-group">
              <el-radio label="fiveColors" @change="FiveColorSelectFunction">五色系</el-radio>
              <el-radio label="monoColors">单色系</el-radio>
            </el-radio-group>
            <div class="color-selector-show">
              <!-- 五色系颜色块 -->
              <div class="fiveColors-selector">
                <div v-for="(color, index) in fiveColors" :key="index" class="color-block-container">
                  <div class="color-block" :style="{ backgroundColor: color.color }"></div>
                  <div class="color-name">{{ color.name }}</div> <!-- 假设color对象有一个name属性 -->
                </div>
              </div>

              <!-- 单色系单选框 -->
              <div v-if="selectedColorGroup === 'monoColors'" class="monoColors-selector">
                <el-radio-group v-model="selectedMonoColor" class="radio-group"
                  style="display: flex; flex-flow: column nowrap; align-items: flex-start;">
                  <el-radio v-for="(monoColor, index) in monoColors" :key="index" :label="monoColor"
                    @change="OneColorSelectFunction(monoColor)">
                    <span style="color: black; font-size: 16px;">{{ monoColor }}</span>
                  </el-radio>
                </el-radio-group>
              </div>
            </div>
          </div>
        </div>

        <div class="ColorFeedback-text" v-if="hasFeedback()">
          <p>此图为传统中国画
            <span v-if="this.TextFeedback1">,类型为{{ TextFeedback1 }}</span>
            <span v-if="this.TextFeedback2">,意境为{{ TextFeedback2 }}</span>
            <span v-if="this.TextFeedback3">,物象为{{ TextFeedback3 }}</span>
            <span v-if="this.TextFeedback4">,技法为{{ TextFeedback4 }}</span>
            <span v-if="this.TextFeedback5">,赋彩为{{ TextFeedback5 }}</span>
            <span v-if="this.OneOrFiveColored">,赋彩为{{ OneOrFiveColored }}</span>
          </p>
          <p v-if="this.inputValue.length > 0">
            用户输入:{{ this.inputValue }}
          </p>
        </div>
        <div class="produce-picture">
          <button @click="imageButtomFunction()"
            style="width: 150px; font-size: 15px ;height: 30px;color: rgb(161, 155, 139);  background-color: rgb(217, 217, 217);border: hidden;cursor: pointer;">
            生成配色方案</button>
        </div>
      </div>


      <div v-bind:class="middlebox">
        <!-- 画作概览 -->
        <div v-bind:class="middleTopbox">
          <div style="display:flex; align-items:center;">
            <span style="color:#675229;font-size: 34px;">🅑</span>
            <span v-bind:id="texttitle" style="color:#95815c;font-size: 18px;">画作概览</span>
          </div>
          <div class="grid-container">
            <div class="grid-item" v-for="(image, index) in images" :key="index">
              <img :src="image" :alt="'image ' + (index + 1)">
            </div>
          </div>
        </div>

        <div v-bind:class="middleBottombox">
          <div style="display:flex; align-items:center;">
            <span style="color:#675229;font-size: 34px;">🅒</span>
            <span v-bind:id="texttitle" style="color:#95815c;font-size: 18px;">推荐配色方案</span>
          </div>
          <div class="test-tiaose">
            <div class="colorNumberBox">
              <span
                style="font-size: 15px; width: 80px; margin-top:4px; margin-right: 2%; margin-left: 5px;">颜色数量：</span>

              <el-select v-model="selectColorNumberArray" placeholder="请选择" @change="selectColorNumber"
                style="  align-content: center; width: 80px; height: 20px;margin-right: 6%; ">
                <el-option v-for="item in colorNumber" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-select>
              <!--<button  @click="updateColorNames" style="height: 30px; margin-top:2px;margin-right: 6%;">
                原图配色方案
              </button>
              <button  @click="" style="height: 30px; margin-top:2px;">
                推荐配色方案
              </button>-->

              <button class="chcolor" v-for="(item, index) in listData" :key="index" @click="changeColor(index)"
                :class="activeIndex === index ? 'active' : ''">
                {{ item }}
              </button>

            </div>
            <div style="display: flex;  flex-direction: row; flex:10; max-height: 263px;">
              <div class="ChooseColorScheme">
                <div v-for="(palette, index) in colorNames2" :key="index" class="palette-button"
                  @mouseover="showPaletteNames(index)" @mouseout="hidePaletteNames" @click="extractColor(index)">
                  <!-- 遍历colorNames2数组中的每一个颜色方案（palette），为每一个方案创建一个按钮-->
                  <div class="color-blocks-container">
                    <div v-for="(color, colorIndex) in palette" :key="colorIndex"
                      :style="{ backgroundColor: '#' + colorRGBs[index][colorIndex].toString(16).padStart(6, '0') }"
                      class="color-block"></div>
                  </div>
                  <div v-if="currentPaletteIndex === index" class="palette-names">
                    {{ palette.join(', ') }}
                  </div>
                </div>
              </div>
              <div class="TestButton">
                <div style="  display: flex; justify-content: center;">
                  <button @click="generateAndShowImage" style="margin: 1px auto;">生成并显示图像</button>
                  <button @click="saveImage" style="margin: 1px auto;">保存图像</button>  
                </div>
                <canvas ref="colorCanvas" width="300" height="300"></canvas>
                <button @click="goToExternalPage" style="height: 25px; margin: 5px auto;">打开上色功能</button>
                <!--选择的颜色方案-->
                <div class="color-scheme-display" style="margin: auto;">
                  <div v-for="(color, index) in testcolorRGB" :key="index" class="color-entry1">
                    <div class="color-preview1" :style="{ backgroundColor: color }"></div>
                    <span class="color-name1">{{ this.testcolorNAMES[index] }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-bind:class="rightbox">
        <div style="display:flex; align-items:center;">
          <span style="color:#675229;font-size: 34px;">🅓</span>
          <span v-bind:id="texttitle" style="color:#95815c;font-size: 18px;">测试配色方案</span>
        </div>
        <div style="  display: flex; flex-direction: column;">
          <!--<div>
            <button @click="goToExternalPage">测试跳转页面</button>

            <div>
              <button @click="showModal = true" style="height: 25px; margin: 5px auto;">打开上色功能</button>
              <div v-if="showModal" class="modal-overlay">
                <div class="modal">
                  <button @click="showModal = false" class="close-btn">&times;</button>
                  <iframe src="http://127.0.0.1:8233/index.html" frameborder="0" class="modal-iframe"></iframe>
                </div>
              </div>
            </div>

            <div>
              <div>
                <button @click="fetchImages">显示图片</button>
                <div v-if="copyimages.length > 0">
                  <img v-for="(imageSrc, index) in copyimages" :key="index" :src="imageSrc" alt="Image">
                </div>
                <div v-else>没有图片可显示</div>
              </div>
            </div>

            <input type="file" @change="handleFileUpload" />
            <button @click="sendRequestResult" :disabled="!roomId">请求处理结果</button>
            <button @click="getProcessedImage" :disabled="!resultId">查看处理结果图片</button>
            <img :src="processedImage" alt="Processed Image" v-if="processedImage">
            <p>房间ID: {{ roomId }}</p>
            <p>处理结果ID: {{ resultId }}</p>
            <p v-if="errorMessage" style="color:red;">错误提示: {{ errorMessage }}</p>
          </div>-->
          <!--显示调色板信息
          <div>上传文件</div>
          <div>{{ this.testcolorRGB }}</div>
          <div>{{ this.SelectedColorNumber }}</div>
          <div>{{ this.prompts }}</div>
          <div>{{ this.colorNames2 }}</div>
          <div>{{ this.colorRGBs }}</div>
          <div>{{ this.OneOrFiveColored }}</div>
          <div>{{ this.colorRGBs2 }}</div>
          <div>{{ this.array }}</div>
          <div>{{ this.feedbackStr2 }}</div>
          <div>{{ this.base64Content }}</div>
          <img :src="base64Image" alt="Uploaded Image">
          <li v-for="(item, index) in colorNames2" :key="index">
            {{ index + 1 }}. {{ item }}
          </li>-->
          <!--<div>{{ displayedImages2 }}</div>-->
          <div style="display: flex; margin:2px auto;">
            <button @click="fetchAndDisplayImages" style="width:95px; height: 25px; margin: 2px;">显示图片</button>
          </div>
          <div style="display: flex; margin:2px auto;">
            <button @click="SetdisplayedImages1" style="width:25px; height: 25px; margin: 2px;">1</button>
            <button @click="SetdisplayedImages2" style="width:25px; height: 25px; margin: 2px;">2</button>
            <button @click="SetdisplayedImages3" style="width:25px; height: 25px; margin: 2px;">3</button>
            <button @click="SetdisplayedImages4" style="width:25px; height: 25px; margin: 2px;">4</button>
            <button @click="SetdisplayedImages5" style="width:25px; height: 25px; margin: 2px;">5</button>
          </div>
          <div style="height: 560px;width: 480px;overflow-y: auto;border: 1px solid #ccc; margin: 0 auto;">
            <div class="image-container">
              <img v-for="(image, index) in displayedImages" :key="index" :src="image" alt="Image" class="image">
            </div>
          </div>
          <div class="testbox">
            <div class="testpicture" v-for="(image, index) in tiaoseimages" :key="index">
              <div class="tset"><img :src="image" :alt="'image ' + (index + 1)"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style>
.container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: 0;
  padding: 0;
}

.title {
  display: flex;
  height: 30px;
  border: 2px solid #d1bf90;
  background-color: #d1bf90;
  align-content: center;
  justify-content: center;
}

.text {
  text-align: center;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  /*字体样式*/
  font-weight: bolder;
  /*字体粗细*/
  color: #f7f5f5;
}

.main {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
}

.left {
  flex: 2;
  background-color: rgb(231, 227, 216);

  margin-top: 4px;
  margin-right: 2px;
}

.right {
  flex: 2;
  background-color: rgb(231, 227, 216);

  margin-top: 4px;
  margin-left: 2px;
}

.middle {
  flex: 2;
  display: flex;
  flex-direction: column;
}

.middle-top {
  flex: 1;
  background-color: rgb(231, 227, 216);
  display: flex;
  flex-direction: column;
  margin-top: 4px;
  margin-left: 2px;
  margin-right: 2px;
}

.middle-bottom {
  flex: 1;
  background-color: rgb(231, 227, 216);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-top: 4px;
  margin-left: 2px;
  margin-right: 2px;
}


/* 下拉框 */
.select {
  margin-top: 5px;
  margin-left: 90px;
  margin-right: 90px;

}


.select1,
.select2,
.select3,
.select4,
.select5 {
  margin-top: 10px;
}

/* 更改选择框（输入框）的背景色 */
.el-select__wrapper.el-tooltip__trigger {
  background-color: #95815c;
  /* 设置输入框背景色 */
  color: white;
  height: 40px;
}

.el-select__selected-item.el-select__placeholder span {
  color: white;
  /* 将文本颜色设置为白色 */
}

/* 更改下拉框的背景色 */
.el-select-dropdown__wrap {
  background-color: #d1bf90;
  /* 设置下拉框背景色 */
}

/* 更改下拉选项的背景色 */
.el-select-dropdown__item {
  background-color: #d1bf90;
  /* 设置下拉选项背景色 */
  color: black;
  /* 设置下拉选项文本颜色 */
}

/* 更改选中项的背景色 */
.el-select-dropdown__item.selected {
  background-color: #d1bf90;
  /* 设置选中项背景色 */
  color: white;
  /* 设置选中项文本颜色 */
}


/* 控制面板文本颜色 */
.leftTitle {
  display: flex;
  align-items: center;
  /* 垂直居中 */
}

/* 反馈框 */
.feedback {
  height: 65px;
  display: flex;
  background-color: aliceblue;
  border: 1px solid black;
  margin-top: 5px;
  margin-bottom: 5px;
  margin-left: 40px;
  margin-right: 40px;
  padding-left: 6px;
  padding-right: 3px;
  flex-wrap: wrap;
  /* 允许内容换行 */
  overflow-y: auto;
  /* 当内容过多时显示垂直滚动条 */
  max-height: 200px;
  /* 设定最大高度，以便内容过多时出现滚动条 */
}


.feedback1,
.feedback2,
.feedback3,
.feedback4,
.feedback5 {
  height: 25px;
  /* 添加一些内边距以使内容不紧贴边缘 */
  display: flex;
  /* 使用 flex 布局以便子元素可以水平排列 */
  align-items: center;
  /* 垂直居中子元素 */
  margin-top: 13px;
  margin-bottom: 3px;
  /* 垂直间距，用于换行时的间隔 */
}

/* 设置 feedback-option 的样式 */
.feedback-option1,
.feedback-option2,
.feedback-option3,
.feedback-option4,
.feedback-option5 {
  height: 25px;
  width: auto;
  padding-left: 5px;
  margin-right: 3px;
  align-items: center;
  justify-content: center;
  border: 1px solid black;
  background-color: #d9d9d9;
}

/* 设置 feed-button2 的样式*/
.feed-button1,
.feed-button2,
.feed-button3,
.feed-button4,
.feed-button5 {
  background-color: #d9d9d9;
  border: none;
  /* 移除边框线 */
  font-weight: bold;
  /* 使其看起来更像一个操作按钮 */
}


/*五色系和单色系*/
.color-selector-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 5px;
}

.color-selector-show {
  display: flex;
  flex-direction: row;
}

.monoColors-selector {
  margin-right: 50px;
}

.fiveColors-selector {
  /* 为五个颜色选择器容器添加样式 */
  display: flex;
  flex-direction: column;
  gap: 8px;
  /* 添加间距 */
  margin-right: 57px;
}

.color-block-container {
  display: flex;
  align-items: center;
  /* 垂直居中 */
  margin-bottom: 2px;
  /* 可选，为每个颜色块容器添加垂直间距 */
}

.color-block {
  width: 50px;
  /* 举例，设置颜色块的宽度 */
  height: 50px;
  /* 举例，设置颜色块的高度 */
  margin-right: 5px;
  /* 为颜色块和颜色名之间添加间距 */
}

.color-name {
  /* 为颜色名添加样式 */
  color: black;
  font-size: 15px;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 6px;
  /* 格子之间的间距 */
  justify-content: center;
  margin-top: 4px;
  margin-bottom: 4px;
  margin-left: auto;
  margin-right: auto;
  width: 350px;

}

/* 色系选择文本 */
.ColorFeedback-text {
  padding-left: 8px;
  padding-right: 8px;
  background-color: #95815c;
  /* 红色背景 */
  color: white;
  /* 白色文本 */
  display: flex;
  /* 使用弹性布局来垂直居中内容 */
  flex-direction: column;
  /* 垂直排列子元素 */
  justify-content: center;
  /* 垂直居中 */
  align-items: center;
  /* 水平居中 */
  text-align: center;
  /* 文本居中 */
  margin-top: 2px;
  margin-bottom: 2px;
  margin-left: 10%;
  margin-right: 10%;
  height: 85px;
}

/* 生成图片 */
.produce-picture {
  display: flex;
  justify-content: center;
  margin-top: 8px;
  /*水平居中 */
}

.grid-item {
  width: 110px;
  /* 根据需要调整格子的宽度 */
  height: 90px;
  /* 根据需要调整格子的高度 */
  object-fit: cover;
  /* 图片填充方式，根据需要调整 */
}

.grid-item img {
  width: 100%;
  height: 100%;
}

.test-tiaose {
  display: flex;
  flex-direction: column;
  border: 1px solid black;
  height: 90%;
}

.testbox {
  display: grid;
  grid-template-rows: repeat(3, 1fr);
  /* 创建三行，每行高度相等 */
  row-gap: 10px;
  /* 行之间的间隙为 10 像素 */
}

.testpicture {
  height: fit-content;
}

.colorNumberBox {
  display: flex;
  flex-direction: row;
  border: 1px solid black;
  height: 34px;
  background-color: white;
}

.colorNumberBox .el-select__wrapper.el-tooltip__trigger {
  max-height: 20px !important;
  /* 设置你期望的高度 */
  line-height: 20px;
  /* 保持文本垂直居中 */
}

.TestButton {
  border: 1px solid black;
  flex: 2;
  background-color: white;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  /* 允许垂直滚动 */
}

.ChooseColorScheme {
  border: 1px solid black;
  flex: 3;
  background-color: white;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
  overflow-y: auto;
  /* 允许垂直滚动 */
}

.palette-button {
  display: inline-block;
  margin: 2px;
  padding: 2px;
  border: 1px solid #ccc;
  position: relative;
  cursor: pointer;
  width: calc(100% / 3 - 20px);
  /* 假设每行最多3个项目，并留出一些间距 */
}

.color-blocks-container {
  display: flex;
  flex-direction: column;
  /* 设置为垂直方向 */
  justify-content: space-around;
  align-items: center;
  padding: auto;
}

.color-block {
  width: 20px;
  height: 20px;
  display: inline-block;
  margin-bottom: 1px;
}

.palette-names {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 5px;
  display: flex;
  justify-content: center;
}

.chcolor {
  background-color: #ccc;
  color: black;
  margin: 5px 0 5px 20px;
  height: 24px;
}

.active {
  background-color: black;
  color: white;
}

.colorNumberBox .el-select__wrapper.el-tooltip__trigger {
  min-height: 22px;
  width: 90px;
  margin-top: 5px;
  background-color: rgb(217, 217, 217);
  border: 1px solid black
}

.colorNumberBox .el-select__selected-item.el-select__placeholder span {
  color: black;

  /* 将文本颜色设置为黑色 */
}

/* 选择的颜色方案样式 */
.color-scheme-display {
  display: flex;
  margin: 10px auto;
  flex-direction: column;
  align-items: flex-start;
}

.color-entry1 {
  display: flex;
  align-items: center;
  margin-bottom: 2px;
  /* 设置颜色块之间的间距 */
}

.color-preview1 {
  width: 40px;
  /* 你可以根据需要设置颜色块的宽度 */
  height: 40px;
  /* 你可以根据需要设置颜色块的高度 */
  border: 1px solid #ccc;
  /* 可选：为颜色块添加边框 */
  margin-left: 15px;
}

.color-name1 {
  margin-left: 10px;
  /* 设置颜色块和颜色名之间的间距 */
  font-size: 14px;
}


.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 50%;
  height: 50%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: auto;
  /* 允许滚动条出现，如果iframe内容超出视口 */
  z-index: 1000;
}

.modal {
  position: relative;
  width: 100%;
  /* 宽度设置为100%，但会被内部iframe的min-width等属性限制 */
  height: 100%;
  /* 高度设置为100%，但同样会受到限制 */
  display: flex;
  flex-direction: column;
  /* 垂直布局 */
  box-sizing: border-box;
  /* 包含padding和border在width和height内 */
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  z-index: 1001;
  /* 确保关闭按钮在iframe之上 */
}

.modal-iframe {
  width: 100%;
  height: 100%;
  border: none;
  display: block;
  /* 移除iframe下方的默认空间 */
}




.image-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  /* 两列 */
  gap: 10px;
  /* 图片之间的间距 */
}

.image {
  width: 100%;
  /* 图片宽度自动调整以适应容器 */
  height: auto;
  /* 保持原始宽高比 */
}


canvas {
  margin-top: 2px;
  border: 1px solid black;
}


</style>
