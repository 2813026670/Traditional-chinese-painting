<script>
import { ref } from 'vue'
import axios from 'axios';
import MyInput from './components/MyInput.vue';

export default {
  components: {
    MyInput
  },
  data() {
    return {
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
      options3: [{ 'value': '画作', 'label': '画作' }, { 'value': '树枝', 'label': '树枝' }, { 'value': '竹', 'label': '竹' }, { 'value': '印章', 'label': '印章' }, { 'value': '花', 'label': '花' }, { 'value': '月亮', 'label': '月亮' }, { 'value': '山石', 'label': '山石' }, { 'value': '日', 'label': '日' }, { 'value': '车', 'label': '车' }, { 'value': '芦苇', 'label': '芦苇' }, { 'value': '藻', 'label': '藻' }, { 'value': '鸭', 'label': '鸭' }, { 'value': '兰', 'label': '兰' }, { 'value': '伞', 'label': '伞' }, { 'value': '舟船', 'label': '舟船' }, { 'value': '桥', 'label': '桥' }, { 'value': '荷叶', 'label': '荷叶' }, { 'value': '鸳鸯', 'label': '鸳鸯' }, { 'value': '云', 'label': '云' }, { 'value': '篮', 'label': '篮' }, { 'value': '作品屏风', 'label': '作品屏风' }, { 'value': '马', 'label': '马' }, { 'value': '坡', 'label': '坡' }, { 'value': '鸟', 'label': '鸟' }, { 'value': '草', 'label': '草' }, { 'value': '山', 'label': '山' }, { 'value': '船', 'label': '船' }, { 'value': '蔬菜', 'label': '蔬菜' }, { 'value': '月', 'label': '月' }, { 'value': '石', 'label': '石' }, { 'value': '果', 'label': '果' }, { 'value': '荷', 'label': '荷' }, { 'value': '鹅', 'label': '鹅' }, { 'value': '梅', 'label': '梅' }, { 'value': '鱼', 'label': '鱼' }, { 'value': '灵芝', 'label': '灵芝' }, { 'value': '屏风', 'label': '屏风' }, { 'value': '驴', 'label': '驴' }, { 'value': '叶', 'label': '叶' }, { 'value': '树木', 'label': '树木' }, { 'value': '龙', 'label': '龙' }, { 'value': '竹篮', 'label': '竹篮' }, { 'value': '虫', 'label': '虫' }, { 'value': '题跋', 'label': '题跋' }, { 'value': '瀑布', 'label': '瀑布' }, { 'value': '人物', 'label': '人物' }, { 'value': '假山', 'label': '假山' }, { 'value': '马车', 'label': '马车' }, { 'value': '亭台', 'label': '亭台' }, { 'value': '画作屏风', 'label': '画作屏风' }, { 'value': '楼阁', 'label': '楼阁' }, { 'value': '水', 'label': '水' }, { 'value': '菊', 'label': '菊' }, { 'value': '走兽', 'label': '走兽' }, { 'value': '马鞍', 'label': '马鞍' }, { 'value': '车轿', 'label': '车轿' }, { 'value': '鸡', 'label': '鸡' }, { 'value': '松', 'label': '松' }],
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
      imageBase64s: [],
      palettearray: [],
      testcolorRGB: [],
      currentPaletteIndex: null,

      selectColorNumberArray: '',
      colorNumber: [
        { value: '3', label: '3' },
        { value: '5', label: '5' },
      ],
      SelectedColorNumber: '',
      OneOrFiveColored: '',
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

    generateImages() {

      this.prompts = [this.feedback1, this.feedback2, this.feedback3, this.feedback4, this.feedback5, '色系',this.inputValue];
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
      axios.post('http://127.0.0.1:5001/get_palette', {
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
    },
    hidePaletteNames() {
      this.currentPaletteIndex = null;
    },

    selectColorNumber() {
      this.SelectedColorNumber = this.selectColorNumberArray;
    },

    extractColor(paletteIndex) {
      // 清空 testcolorRGB 数组，以便存储当前按钮的所有颜色  
      this.testcolorRGB = [];
      // 获取当前按钮下的所有颜色值  
      const colors = this.colorRGBs[paletteIndex].map(color => {
        return '#' + color.toString(16).padStart(6, '0');
      });
      // 将所有颜色添加到 testcolorRGB 数组中  
      this.testcolorRGB.push(...colors);
      // 可以在这里添加其他逻辑，比如显示一个消息或执行其他操作  
    },

    imageButtomFunction() {
      this.generateImages();
      this.OneOrFiveColorSelectFunction();
      this.sendPostRequest();
    },
    updateColorNames() {
      this.SelectedColorNumber = 9;
    },
  },
  watch: {
    SelectedColorNumber: function (val) {
      this.SelectedColorNumber = val;
      this.colorNames2 = this.colorNames.slice(0, this.SelectedColorNumber);
    }
  },

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
        <!--反馈框
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
          <my-input v-model="inputValue" id="my-input" type="text" label=""
            placeholder="输入"></my-input>
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

        <div class="ColorFeedback-text">
          <p>此图为传统中国画, 类型为{{ feedback1 }},意境为{{ feedback2 }},物象为{{ feedback3 }},技法为{{ feedback4 }},赋彩为{{ feedback5 }}
          </p>
          <p>
            用户输入:{{this.inputValue}}
          </p>
        </div>

        <div class="produce-picture">
          <button @click="imageButtomFunction()" style="width: 150px;height: 30px;">生成图片</button>
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
            <span v-bind:id="texttitle" style="color:#95815c;font-size: 18px;">推荐调色板</span>
          </div>
          <div class="test-tiaose">
            <div class="colorNumberBox">
              <span
                style="font-size: 15px; width: 80px; margin-top:4px; margin-right: 2%; margin-left: 5px;">颜色数量:</span>
              <el-select v-model="selectColorNumberArray" placeholder="数量" fallback-placements="top-start"
                @change="selectColorNumber(value)"
                style="  align-content: center; width: 80px; height: 20px;margin-right: 6%;">
                <el-option v-for="item in colorNumber" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-select>
              <button @click="updateColorNames" style="height: 30px; margin-top:2px;margin-right: 6%;">
                原图配色方案
              </button>
              <button @click="" style="height: 30px; margin-top:2px;">
                推荐配色方案
              </button>
            </div>
            <div style="display: flex;  flex-direction: row; flex:10;">
              <div class="ChooseColorScheme">
                <div v-for="(palette, index) in colorNames2" :key="index" class="palette-button"
                  @mouseover="showPaletteNames(index)" @mouseout="hidePaletteNames" @click="extractColor(index)">
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
                <button @click="testTiaoseFunction">测试调色板</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-bind:class="rightbox">
        <span>🅓测试调色板</span>
        <div>
          <div>上传文件</div>
          <div>{{ this.testcolorRGB }}</div>
          <div>{{ this.SelectedColorNumber }}</div>
          <div>{{ this.prompts }}</div>
          <div>{{ this.colorNames2 }}</div>
          <div>{{ this.OneOrFiveColored }}</div>
          <div>{{ this.inputValue }}</div>
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
  background-color: rgb(234, 227, 216);

  margin-top: 4px;
  margin-right: 2px;
}

.right {
  flex: 2;
  background-color: rgb(234, 227, 216);

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
  background-color: rgb(234, 227, 216);
  display: flex;
  flex-direction: column;
  margin-top: 4px;
  margin-left: 2px;
  margin-right: 2px;
}

.middle-bottom {
  flex: 1;
  background-color: rgb(234, 227, 216);
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
  margin-top: 18px;
}

/* 更改选择框（输入框）的背景色 */
.el-select__wrapper.el-tooltip__trigger {
  background-color: #95815c !important;
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
  margin-top: 15px;
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
  gap: 10px;
  /* 添加间距 */
  margin-right: 57px;
}

.color-block-container {
  display: flex;
  align-items: center;
  /* 垂直居中 */
  margin-bottom: 8px;
  /* 可选，为每个颜色块容器添加垂直间距 */
}

.color-block {
  width: 50px;
  /* 举例，设置颜色块的宽度 */
  height: 50px;
  /* 举例，设置颜色块的高度 */
  margin-right: 10px;
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
  grid-gap: 10px;
  /* 格子之间的间距 */
  justify-content: center;
  margin-top: 4px;
  margin-bottom: 9px;
  margin-left: auto;
  margin-right: auto;
  width: 350px;

}

/* 色系选择文本 */
.ColorFeedback-text {
  padding-top: 5px;
  padding-bottom: 5px;
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
  margin-left: 10%;
  margin-right: 10%;
}

/* 生成图片 */
.produce-picture {
  display: flex;
  align-items: center;
  /*垂直居中 */
  justify-content: center;
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
  margin-top: 5px;
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
}

.ChooseColorScheme {
  border: 1px solid black;
  flex: 3;
  background-color: white;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
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
</style>