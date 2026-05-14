window.onload = function () {

    const map = L.map('map').setView([30.4158, 79.3189], 10);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    L.marker([30.4158, 79.3189])
        .addTo(map)
        .bindPopup("📍 Gopeshwar")
        .openPopup();

};