<template>  
  <div class="color-scheme-display">  
    <div   
      v-for="(color, index) in testcolorRGB"   
      :key="index"   
      class="color-entry"  
    >  
      <div class="color-preview" :style="{ backgroundColor: color }"></div>  
      <span class="color-name" :style="{ color: color }">{{ colorNames[index] }}</span>  
    </div>  
  </div>  
</template>  
  
<script>  
export default {  
  props: {  
    colors: {  
      type: Array,  
      required: true  
    },  
    names: {  
      type: Array,  
      required: true  
    }  
  }   
};  
</script>  
  
<style scoped>  
.color-scheme-display {  
  display: flex;  
  flex-direction: column;  
  align-items: flex-start;  
}  
  
.color-entry {  
  display: flex;  
  align-items: center;  
  margin-bottom: 10px; /* 设置颜色块之间的间距 */  
}  
  
.color-preview {  
  width: 50px; /* 你可以根据需要设置颜色块的宽度 */  
  height: 50px; /* 你可以根据需要设置颜色块的高度 */  
  border: 1px solid #ccc; /* 可选：为颜色块添加边框 */  
}  
  
.color-name {  
  margin-left: 10px; /* 设置颜色块和颜色名之间的间距 */  
  font-size: 14px;  
}  
</style>