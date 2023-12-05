<script setup>
    import axios from 'axios'
</script>

<template>
    <div class="container mt-3" v-if="weatherLoaded">
        <div class="d-flex flex-lg-row flex-column">
            <div class="card w-100 mb-3 mb-lg-0 p-3 main-weather m-1">
                <h1>Today</h1>
                <h2 class="place"> {{cityName}} {{ country }} </h2>
                <div class="temperature">
                    <h1> {{ temperature }} &deg;C <img :src="icon" alt="icon weather"></h1>
                    <h2> {{ description }} </h2>
                </div>
                <p>{{date}} {{time}}</p>
            </div>
            <div class="card w-100 p-3 additional-weather m-1">
                <div class="mb-3">
                    <h4>Additional Information</h4>
                </div>
                <div>
                    <div class="d-flex justify-content-between">
                        <h6>Feels Like</h6>
                        <p>{{ feelsLike }} &deg;C</p>
                    </div>
                    <div class="d-flex justify-content-between">
                        <h6>Wind Speed</h6>
                        <p>{{ windSpeed }} m/s</p>
                    </div>
                    <div class="d-flex justify-content-between">
                        <h6>Pressure</h6>
                        <p>{{ pressure }} hPa</p>
                    </div>
                    <div class="d-flex justify-content-between">
                        <h6>Humidity</h6>
                        <p>{{ humidity }} %</p>
                    </div>
                    <div class="d-flex justify-content-between">
                        <h6>Cloudiness</h6>
                        <p>{{ cloudiness }} %</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="w-100 d-flex justify-content-center align-items-center" v-if="isError">
      <div class="w-50 alert alert-warning alert-dismissible fade show" role="alert">
        <strong>Failed to fetch data for this city</strong>
      </div>
    </div>
</template>

<script>
    export default (await import('vue')).defineComponent({
        name: 'Weather',
        components: {
        },
        props: {
            city: String,
        },
        data() {
            return {
                city: this.city,
                temperature: null,
                description: null,
                date: null,
                time: null,
                cityName: null,
                country: null,
                feelsLike: null,
                windSpeed: null,
                pressure: null,
                humidity: null,
                cloudiness: null,
                icon: null,
                months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                weatherLoaded: false,
                isError: false,
            }
        },
        async created() {
            try {
                this.isError = false;
                this.weatherLoaded = false;
                let url = "https://api.openweathermap.org/data/2.5/weather?q=" + this.city + "&units=metric&appid=0164a6f5ecd0e56453dce5381fc06fd5";
                const response = await axios.get(url);
                const weatherData = response.data;
                this.temperature = Math.round(weatherData.main.temp);
                this.description = weatherData.weather[0].description;
                const currDate = new Date();
                this.date = currDate.getDate() + ' ' + this.months[currDate.getMonth()] + ' ' + currDate.getFullYear();
                const hours = currDate.getHours().toString().padStart(2, '0');
                const minutes = currDate.getMinutes().toString().padStart(2, '0');
                const seconds = currDate.getSeconds().toString().padStart(2, '0');
                this.time = hours + ':' + minutes + ':' + seconds;
                this.cityName = weatherData.name;
                this.country = weatherData.sys.country;
                this.feelsLike = Math.round(weatherData.main.feels_like);
                this.windSpeed = weatherData.wind.speed;
                this.pressure = weatherData.main.pressure;
                this.humidity = weatherData.main.humidity;
                this.cloudiness = weatherData.clouds.all;
                this.icon = "https://api.openweathermap.org/img/w/" + weatherData.weather[0].icon + ".png";
                await this.$nextTick();
                this.weatherLoaded = true;
            } catch (error) {
                this.weatherLoaded = false;
                this.isError = true;
            }
        }
    })
</script>

<style>
    .main-weather {
        border-radius: 20px;
        color: #F5E8C7 !important;
        background-image: url("https://www.liveabout.com/thmb/35QTy-QxEsQlfQymA7p3Rrb3MUc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/107907029-56a7bf5e5f9b58b7d0ed7718.jpg");
        background-size: cover;
        background-position: center;
        background-blend-mode: overplay;
        background-repeat: no-repeat;   
        color: #363062 !important;
    }
    .additional-weather {
        background-color: #818FB4 !important;
        color: #F5E8C7 !important;
    }
</style>
