<script>
import { ref } from 'vue'
import axios from 'axios';

export default {
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

      selected1: '',
      options1: [
        { value: '花鸟', label: '花鸟' },
        { value: '山水', label: '山水' },
        { value: '人物', label: '人物' }
      ],
      feedback1: '',

      selected2: '',
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
      feedback2: '',

      selected3: '',
      options3: [
        { value: '气韵', label: '气韵' },
        { value: 'option2', label: '选项2' },
        { value: 'option3', label: '选项3' }
      ],
      feedback3: '',

      selected4: '',
      options4: [
        { value: '鸟', label: '鸟' },
        { value: 'option2', label: '选项2' },
        { value: 'option3', label: '选项3' }
      ],
      feedback4: '',

      selected5: '',
      options5: [
        { value: '五色系', label: '五色系' },
        { value: 'option2', label: '选项2' },
        { value: 'option3', label: '选项3' }
      ],
      feedback5: '',
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
        { value: '9', label: '9' }
      ],
      SelectedColorNumber: '',
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
    handledelete1() {
      this.feedback1 = '';
    },

    handlechange2(value) {
      this.feedback2 = value;
    },
    handledelete2() {
      this.feedback2 = '';
    },

    handlechange3(value) {
      this.feedback3 = value;
    },
    handledelete3() {
      this.feedback3 = '';
    },

    handlechange4(value) {
      this.feedback4 = value;
    },
    handledelete4() {
      this.feedback4 = '';
    },

    handlechange5(value) {
      this.feedback5 = value;
    },
    handledelete5() {
      this.feedback5 = '';
    },

    generateImages() {

      this.prompts = [this.feedback1, this.feedback2, this.feedback3, this.feedback4, this.feedback5];
    },
    testTiaoseFunction() {
      this.tiaoseimages = this.tiaoseimages2;
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

    selectColorNumber(value) {
      this.SelectedColorNumber = value;
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
      this.sendPostRequest();
    },
    updateColorNames() {  
    this.colorNames2 = this.colorNames.slice(0, this.SelectedColorNumber); // 取前 selectedColorNumber 个  
  }, 
  },
  watch: {  
  SelectedColorNumber:function (val) {
    this.SelectedColorNumber=val;
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
        <!--反馈框-->
        <div class="feedback">
          <div class="feedback1" v-if="feedback1 !== ''"><!--//下拉框1的反馈框-->
            <div class="feedback-option1">{{ feedback1 }}</div>
            <button class="feed-button1" v-if="feedback1 !== ''" v-on:click="handledelete1">✖</button>
          </div>

          <div class="feedback2" v-if="feedback2 !== ''"><!--//下拉框2的反馈框-->
            <div class="feedback-option2">{{ feedback2 }}</div>
            <button class="feed-button2" v-if="feedback2 !== ''" v-on:click="handledelete2">✖</button>
          </div>


          <div class="feedback3" v-if="feedback3 !== ''"><!--//下拉框3的反馈框-->
            <div class="feedback-option3">{{ feedback3 }}</div>
            <button class="feed-button3" v-if="feedback3 !== ''" v-on:click="handledelete3">✖</button>
          </div>

          <div class="feedback4" v-if="feedback4 !== ''"><!--//下拉框4的反馈框-->
            <div class="feedback-option4">{{ feedback4 }}</div>
            <button class="feed-button4" v-if="feedback4 !== ''" v-on:click="handledelete4">✖</button>
          </div>

          <div class="feedback5" v-if="feedback5 !== ''"><!--//下拉框5的反馈框-->
            <div class="feedback-option5">{{ feedback5 }}</div>
            <button class="feed-button5" v-if="feedback5 !== ''" v-on:click="handledelete5">✖</button>
          </div>
        </div>

        <!--选择框-->
        <div class="select">
          <div class="select1">
            <el-select v-model="selected1" placeholder="主题" fallback-placements="top-start" @change="handlechange1">
              <el-option v-for="item in options1" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>

          <div class="select2">
            <el-select v-model="selected2" placeholder="意境" fallback-placements="top-start" @change="handlechange2">
              <el-option v-for="item in options2" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>

          <div class="select3">
            <el-select v-model="selected3" placeholder="物象" fallback-placements="top-start" @change="handlechange3">
              <el-option v-for="item in options3" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>

          <div class="select4">
            <el-select v-model="selected4" placeholder="技法" fallback-placements="top-start" @change="handlechange4">
              <el-option v-for="item in options4" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>

          <div class="select5">
            <el-select v-model="selected5" placeholder="赋彩" fallback-placements="top-start" @change="handlechange5">
              <el-option v-for="item in options5" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>



        <div class="color-selector-container">
          <div class="color-selector">
            <el-radio-group v-model="selectedColorGroup" class="radio-group">
              <el-radio label="fiveColors">五色系</el-radio>
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
                  <el-radio v-for="(monoColor, index) in monoColors" :key="index" :label="monoColor">
                    <span style="color: black; font-size: 16px;">{{ monoColor }}</span>
                  </el-radio>
                </el-radio-group>
              </div>
            </div>

          </div>
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
              <span style="font-size: 15px; width: 80px; margin-top: 3%;">颜色数量:</span>
              <el-select v-model="selectColorNumberArray" placeholder="数量" fallback-placements="top-start"
                @change="selectColorNumber" style="  align-content: center; width: 80px;">
                <el-option v-for="item in colorNumber" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-select>
            </div>
            <div style="display: flex;  flex-direction: row; flex:9;">
              <div class="ChooseColorScheme" >
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
              <div class="TestButton" >
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
          <div>{{ this.colorNames2 }}</div>
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
  background-color:rgb(234, 227, 216);
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
}


.feedback1,
.feedback2,
.feedback3,
.feedback4,
.feedback5 {
  height: 25px;
  background-color: #d9d9d9;
  /* 假设你想要的背景颜色是 #f0f0f0 */
  padding: 10px;
  /* 添加一些内边距以使内容不紧贴边缘 */
  display: flex;
  /* 使用 flex 布局以便子元素可以水平排列 */
  align-items: center;
  /* 垂直居中子元素 */
  margin-right: 3px;
  margin-left: 3px;
  margin-top: 13px;
}

/* 设置 feedback-option 的样式 */
.feedback-option1,
.feedback-option2,
.feedback-option3,
.feedback-option4,
.feedback-option5 {
  height: 25px;
  width: auto;
  margin-right: 2px;
}

/* 设置 feed-button2 的样式*/
.feed-button1,
.feed-button2,
.feed-button3,
.feed-button4,
.feed-button5 {
  background-color: transparent;
  /* 设置为透明背景，以继承父容器的背景颜色 */
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

.colorNumberBox{
  display: flex;  
  flex-direction: row; 
  border: 1px solid black;
  flex:2;
  background-color: white;
}
.TestButton{
  border: 1px solid black;
  flex:2;
  background-color: white;
}
.ChooseColorScheme{
  border: 1px solid black;
  flex:3;
  background-color: white;
}
.palette-button {
  display: inline-block;
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  position: relative;
  cursor: pointer;
}

.color-blocks-container {  
  display: flex;  
  flex-direction: column; /* 设置为垂直方向 */  
  /* 其他样式，如间距、对齐等 */  
}
.color-block {
  width: 20px;
  height: 20px;
  display: inline-block;
  margin-right: 5px;
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