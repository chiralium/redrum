<template>
  <div class="status_bar">
    <div v-bind:style="{ backgroundColor : this.status_code === 200 ? 'green' : 'red' }"></div>
    <h1 v-if="status_code === 200">Все хорошо!</h1>
    <h1 v-else>ПЕГАС УПАЛЛ!.</h1>
  </div>
</template>

<script>
  export default {
    name: "Pegas.vue",
    data : function () {
      return {
        status_code : 400
      }
    },

    mounted() {
      setInterval(
        () => {
          fetch(
            'http://localhost:5000/api/pegas/',
            {
              method: 'get'
            }
          ).then( response => response.json() )
            .then(
              (data) => {
                return this.status_code = data.status
              }
            )
        },
        4000
      )
    }
  }
</script>

<style scoped>
  .status_bar {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .status_bar > div {
    position: absolute;
    transform: translate(-50%, -50%);
    left: 50%;
    top: 50%;
    border: 5px solid black;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    align-items: center;
  }
</style>
