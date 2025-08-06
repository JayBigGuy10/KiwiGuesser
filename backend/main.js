var map = L.map('map').setView([36.1625, -86.225], 13);

// L.tileLayer('https://basemaps.linz.govt.nz/v1/tiles/aerial/WebMercatorQuad/{z}/{x}/{y}.webp?api=c01k1ey01rv6mfk26d2r8hzgsmc', {
//     maxZoom: 19,
//     attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
// }).addTo(map);

L.tileLayer('https://titiler.xyz/mosaicjson/tiles/WebMercatorQuad/{z}/{x}/{y}@1x?url=https%3A%2F%2Fgist.githubusercontent.com%2Fvincentsarago%2Fc6ace3ccd29a82a4a5531693bbcd61fc%2Fraw%2Fe0d0174a64a9acd2fb820f2c65b1830aab80f52b%2FNOAA_Nashville_Tornado.json', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

