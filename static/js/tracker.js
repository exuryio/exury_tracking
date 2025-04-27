// tracker.js
(function() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      const data = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude
      };

      fetch("https://exury.io/api/track", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(result => {
        console.log("Ubicación enviada:", result);
      })
      .catch(error => {
        console.error("Error al enviar la ubicación:", error);
      });
    });
  } else {
    console.warn("Geolocalización no soportada por este navegador.");
  }
})();
