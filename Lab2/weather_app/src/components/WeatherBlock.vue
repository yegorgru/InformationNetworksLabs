<script setup>
</script>

<template>
    <div class="container mt-3">
        <div class="d-flex flex-lg-row flex-column">
            <div class="card w-100 mb-3 mb-lg-0 p-3 main-weather">
                <h1>Today</h1>
                <p>date</p>
                <small>time</small>
                <h2 class="place"> city <small> country </small></h2>
                <div class="temperature">
                    <h1> temperature &deg;C </h1>
                    <h2> description </h2>
                </div>
            </div>
            <div class="card w-100 p-3 additional-weather">
                <div class="mb-3">
                    <h4>Additional Information</h4>
                </div>
                <div>
                    <div class="d-flex justify-content-between">
                        <h6>Wind Speed</h6>
                        <p>{{ wind }} m/s</p>
                    </div>
                    <div class="d-flex justify-content-between">
                        <h6>Pressure</h6>
                        <p>{{ pressure }} hPa</p>
                    </div>
                    <div class="d-flex justify-content-between">
                        <h6>Humidity</h6>
                        <p>{{ humidity }} %</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
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
