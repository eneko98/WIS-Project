document.addEventListener('DOMContentLoaded', function () {
    // Function to initialize the map
    function initMap() {
        // Get the event location name from the passed variable
        var locationName = eventLocation;

        // Use Nominatim to geocode the location name to get its coordinates
        fetch('https://nominatim.openstreetmap.org/search?format=json&q=' + encodeURIComponent(locationName))
            .then(response => response.json())
            .then(data => {
                if (data.length === 0) {
                    console.error('Location not found: ' + locationName);
                    return;
                }

                // Extract latitude and longitude from the response
                var latitude = data[0].lat;
                var longitude = data[0].lon;

                // Create a map centered at the event location
                var map = L.map('map').setView([latitude, longitude], 15);

                // Add OpenStreetMap tile layer to the map
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: 'Map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                }).addTo(map);

                // Place a marker at the event location
                var marker = L.marker([latitude, longitude]).addTo(map);
                marker.bindPopup(locationName).openPopup();

                // Fit the map bounds to include the marker
                var bounds = L.latLngBounds([[latitude, longitude]]);
                map.fitBounds(bounds);
            })
            .catch(error => {
                console.error('Error fetching location:', error);
            });
    }

    // Call the initMap function when the DOM content is loaded
    initMap();
});
