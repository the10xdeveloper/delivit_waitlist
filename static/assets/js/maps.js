function initMap() {
    const pickupAddress = JSON.parse(`{{ pickup_address }}`);
    const deliveryAddress = JSON.parse(`{{ delivery_address }}`);
    const pickupLatLng = {lat: parseFloat(pickupAddress.latitude), lng: parseFloat(pickupAddress.longitude)};
    const deliveryLatLng = {
        lat: parseFloat(deliveryAddress.latitude),
        lng: parseFloat(deliveryAddress.longitude)
    };
    const map = new google.maps.Map(document.getElementById("map"), {
        center: pickupLatLng,
        zoom: 13,
    });
    const pickupMarker = new google.maps.Marker({
        position: pickupLatLng,
        map: map,
        title: "Pickup Address",
    });
    const deliveryMarker = new google.maps.Marker({
        position: deliveryLatLng,
        map: map,
        title: "Delivery Address",
    });
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer({map: map});
    directionsService.route(
        {
            origin: pickupLatLng,
            destination: deliveryLatLng,
            travelMode: "TRANSIT",
        },
        function (response, status) {
            if (status === "OK") {
                directionsRenderer.setDirections(response);
            } else {
                window.alert("Directions request failed due to " + status);
            }
        }
    );
}
