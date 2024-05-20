
document.addEventListener('DOMContentLoaded', function () {
    function initMap() {
        var locationName = "{{ event.location }}";
        fetch('https://nominatim.openstreetmap.org/search?format=json&q=' + locationName)
            .then(response => response.json())
            .then(data => {
                var latitude = data[0].lat;
                var longitude = data[0].lon;
                var map = L.map('map').setView([latitude, longitude], 15);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: 'Map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                }).addTo(map);
                var marker = L.marker([latitude, longitude]).addTo(map);
                marker.bindPopup(locationName).openPopup();
                var bounds = L.latLngBounds([[latitude, longitude]]);
                map.fitBounds(bounds);
            });
    }
    initMap();
});