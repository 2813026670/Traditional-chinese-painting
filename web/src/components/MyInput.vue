<template>
  <div class="InputBox">
    <label :for="id">{{ label }}</label>
    <textarea
      :id="id"
      :value="internalValue"
      @input="handleInput($event)"
      :placeholder="placeholder"
      :class="[
        'TextArea',
        { 'input-error': hasError },
      ]"
    ></textarea>
    <p v-if="hasError" class="error-message">{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyInput',
  props: {
    modelValue: {
      type: String,
      default: ''
    },
    id: {
      type: String,
      required: true
    },
    type: {
      type: String,
      default: 'text'
    },
    label: {
      type: String,
      default: ''
    },
    placeholder: {
      type: String,
      default: ''
    }
  },
  emits: ['update:modelValue'],
  data() {
    return {
      internalValue: this.modelValue, // 内部存储的值
      hasError: false, // 是否有错误
      errorMessage: '', // 错误消息
      badWords: ['250', 'sb',"傻瓜"] // 不良信息列表
    };
  },
  methods: {
    handleInput(event) {
    const value = event.target.value;
    let truncatedValue = value;

    // 检查不良信息
    let isValid = true;
    this.badWords.forEach(word => {
      if (value.includes(word)) {
        isValid = false;
        this.errorMessage = `请避免使用不文明用语：“${word}”。`;
        alert(`输入包含不合规内容，请重新输入。`);
        truncatedValue = ''; // 清空输入框
      }
    });

    // 检查长度是否超过20个字符
    if (truncatedValue.length > 20) {
      isValid = false;
      truncatedValue = truncatedValue.substring(0, 20);
      alert('输入已超过20个字符的限制，请重新输入。');
    }

    if (isValid) {
      this.hasError = false;
      this.internalValue = truncatedValue;
      this.$emit('update:modelValue', truncatedValue);
    } else {
      this.hasError = true;
      event.target.value = truncatedValue; // 更新输入框的值
    }
  }
  }
  }
</script>

<style>
.InputBox {
  display: flex;
  background-color: aliceblue;
  border: 1px solid black;
  margin: auto;
  width: 400px;
  flex-wrap: wrap;
  overflow-y: auto;
  height: 70px;
}

.TextArea {
  width: 100%;
  min-height: 100%;
  font-size: 15px;
  white-space: pre-wrap;
  resize: none;
  overflow-y: auto;
}
</style>