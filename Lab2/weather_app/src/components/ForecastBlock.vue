<script setup>
    import axios from 'axios'
</script>

<template>
    <div class="container mt-3 text-center d-flex justify-content-between forecast" v-if="forecastLoaded">
        <div v-for="day in forecast" :key="day.date">
            <div class="forecast-day">
                <div><img :src="day.iconUrl" alt="icon weather"></div>
                <div>{{ getDayName(day.date) }}</div>
                <div>{{ day.temperature }}&deg;C</div>
            </div>
        </div>
    </div>
</template>

<script>
  export default (await import('vue')).defineComponent({
    props: {
        city: String
    },
    data() {
        return {
            forecast: [],
            forecastLoaded: false,
        }
    },
    async created() {
        try {
            this.forecastLoaded = false;   
            let url = "https://api.openweathermap.org/data/2.5/forecast?q=" + this.city + "&units=metric&appid=0164a6f5ecd0e56453dce5381fc06fd5";
            const response = await axios.get(url);
            const forecastData = response.data.list;
            this.forecast = forecastData
                .map(item => ({
                    date: new Date(item.dt_txt),
                    temperature: Math.round(item.main.temp),
                    description: item.weather[0].description,
                    iconUrl: "https://api.openweathermap.org/img/w/" + item.weather[0].icon + ".png",
                }))
                .reduce((acc, item) => {
                    if (!acc.some(day => day.date.toDateString() === item.date.toDateString())) {
                        acc.push(item);
                    }
                    return acc;
                }, [])
                .slice(1, 5);  
            this.forecastLoaded = true;          
        } catch (error) {
            this.forecastLoaded = false;
        }
    },
    methods: {
        getDayName(date) {
            const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
            return dayNames[date.getDay()];
        }
    }
  })
</script>

<style>
    .forecast {
        border-radius: 20px;
        background-color: #435585;
    }
    .forecast-day {
        color: #F5E8C7;
    }
</style>
