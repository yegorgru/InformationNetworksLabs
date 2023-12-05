<script setup>
    import WeatherBlock from './components/WeatherBlock.vue'
    import ForecastBlock from './components/ForecastBlock.vue'
</script>

<template>
    <header class="container h-100 p-5">
        <h1 class="mb-5">Weather App</h1>
        <div class="input-group">
            <input type="text" id="cityInput" class="form-control" placeholder="Enter city name" maxlength="50" aria-label="City" v-model="city">
            <div class="input-group-append">
                <button class="btn btn-primary" type="button" id="searchButton" @click="search">Search</button>
            </div>
        </div>
    </header>
    <main>
        <WeatherBlock :city="city" v-if="weatherLoaded"></WeatherBlock>
        <ForecastBlock :city="city" v-if="weatherLoaded"></ForecastBlock>
    </main>
</template>

<script>
    export default (await import('vue')).defineComponent({
        name: 'App',
        components: {
        },
        data() {
            return {
                city: '',
                weatherLoaded: false,
            }
        },
        methods: {
            async search() {
                this.weatherLoaded = false;
                await this.$nextTick();
                this.weatherLoaded = true;
            }
        }
    })
</script>

<style>
    body {
        background-color: #363062 !important;
    }
    header {
        background-color: #435585;
        border-radius: 20px;
        color: #F5E8C7;
        text-align: center;
        margin-top: 5rem;
    }
    .input-group {
        width: 100%;
        max-width: 400px;
        margin: 0 auto;
    }
    #cityInput {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
        background-color: #F5E8C7;
        color: #363062;
    }
    #cityInput::placeholder {
        color: #363062;
    }
    #searchButton {
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;
        background-color: #818FB4;
        color: #F5E8C7;
    }
</style>
