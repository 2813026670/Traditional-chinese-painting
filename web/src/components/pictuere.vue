<template>
    <div>
      <button @click="fetchAndDisplayImages">Load Images</button>
      <div v-if="images.length > 0">
        <img v-for="(image, index) in images" :key="index" :src="image" alt="Image">
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        images: [],
      };
    },
    methods: {
      async fetchAndDisplayImages() {
        try {
          const response = await axios.get('/get_latest_images');
          this.images = response.data.images.map(image => `data:image/jpeg;base64,${image}`);
        } catch (error) {
          console.error('Failed to fetch images:', error);
        }
      },
    },
  };
  </script>