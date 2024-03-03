
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -33.866, lng: 151.196 },
    zoom: 15,
  });
  const request = {
    placeId: "ChIJN1t_tDeuEmsRUsoyG83frY4",
    fields: ["name", "formatted_address", "place_id", "geometry"],
  };
  const infowindow = new google.maps.InfoWindow();
  const service = new google.maps.places.PlacesService(map);

  service.getDetails(request, (place, status) => {
    if (
      status === google.maps.places.PlacesServiceStatus.OK &&
      place &&
      place.geometry &&
      place.geometry.location
    ) {
      const marker = new google.maps.Marker({
        map,
        position: place.geometry.location,
      });

      google.maps.event.addListener(marker, "click", () => {
        const content = document.createElement("div");
        const nameElement = document.createElement("h2");

        nameElement.textContent = place.name;
        content.appendChild(nameElement);

        const placeIdElement = document.createElement("p");

        placeIdElement.textContent = place.place_id;
        content.appendChild(placeIdElement);

        const placeAddressElement = document.createElement("p");

        placeAddressElement.textContent = place.formatted_address;
        content.appendChild(placeAddressElement);
        infowindow.setContent(content);
        infowindow.open(map, marker);
      });
    }
  });
}
function place_list(location, activity) {
	alert(location + activity);
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { location },
    zoom: 15,
  });
  const request = {
    query: activity,
    fields: ["name", "formatted_address", "place_id", "geometry"],
  };
  const infowindow = new google.maps.InfoWindow();
  const service = new google.maps.places.PlacesService(map);

  service.getDetails(request, (place, status) => {
    if (
      status === google.maps.places.PlacesServiceStatus.OK &&
      place &&
      place.geometry &&
      place.geometry.location
    ) {
      const marker = new google.maps.Marker({
        map,
        position: place.geometry.location,
      });

      google.maps.event.addListener(marker, "click", () => {
        const content = document.createElement("div");
        const nameElement = document.createElement("h2");

        nameElement.textContent = place.name;
        content.appendChild(nameElement);

        const placeIdElement = document.createElement("p");

        placeIdElement.textContent = place.place_id;
        content.appendChild(placeIdElement);

        const placeAddressElement = document.createElement("p");

        placeAddressElement.textContent = place.formatted_address;
        content.appendChild(placeAddressElement);
        infowindow.setContent(content);
        infowindow.open(map, marker);
      });
    }
  });
}

var map;
var service;
var infowindow;

function exaple_places(activity) {
  var sydney = new google.maps.LatLng(-33.867, 151.195);

  infowindow = new google.maps.InfoWindow();

  map = new google.maps.Map(
      document.getElementById('map'), {center: sydney, zoom: 0});

  var request = {
    query: activity,
    fields: ['name', 'geometry'],
  };

  var service = new google.maps.places.PlacesService(map);
	console.log
  service.findPlaceFromQuery(request, function(results, status) {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
      for (var i = 0; i < results.length; i++) {
        createMarker(results[i]);
      }
      map.setCenter(results[0].geometry.location);
    }
  });
}

function createMarker(place) {
  if (!place.geometry || !place.geometry.location) return;

  const marker = new google.maps.Marker({
    map,
    position: place.geometry.location,
  });

  google.maps.event.addListener(marker, "click", () => {
    infowindow.setContent(place.name || "");
    infowindow.open(map);
  });
}

var map;
var service;
var infowindow;
var geocoder;

function initialize(address, activity) {
	geocoder = new google.maps.Geocoder();
	var pyrmont = new google.maps.LatLng(-33.8665433,151.1956316);

	map = new google.maps.Map(document.getElementById('map'), {
      center: pyrmont,
      zoom: 15
    });
	geocoder.geocode( { 'address': address}, function(results, status) {
	if (status == 'OK') {
		map.setCenter(results[0].geometry.location);
		var place = results[0].geometry.location
	  var request = {
		location: place,
		radius: '500',
		query: activity
	  };

	  service = new google.maps.places.PlacesService(map);
	  service.textSearch(request, callback);
	} else {
	alert('Geocode was not successful for the following reason: ' + status);
	}
    });
}
function codeAddress(address) {
	geocoder = new google.maps.Geocoder();
	var latlng = new google.maps.LatLng(-34.397, 150.644);
    var mapOptions = {
      zoom: 8,
      center: latlng
    }
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
    //var address = document.getElementById('address').value;
    geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == 'OK') {
		  console.log(results);
        map.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
            map: map,
            position: results[0].geometry.location
        });
      } else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });
  }
function callback(results, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    for (var i = 0; i < results.length; i++) {
      var place = results[i];
      createMarker(results[i]);
    }
  }
}

var map;
var service;
var infowindow;
var geocoder;

function get_activity() {
    var address = document.getElementById('address').value;
    var activity = document.getElementById('activity').value;
    alert(address);
	geocoder = new google.maps.Geocoder();
	var pyrmont = new google.maps.LatLng(-33.8665433,151.1956316);

	map = new google.maps.Map(document.getElementById('map'), {
      center: pyrmont,
      zoom: 15
    });
	geocoder.geocode( { 'address': address}, function(results, status) {
	if (status == 'OK') {
		map.setCenter(results[0].geometry.location);
		var place = results[0].geometry.location
	  var request = {
		location: place,
		radius: '500',
		query: activity
	  };

	  service = new google.maps.places.PlacesService(map);
	  service.textSearch(request, callback);
	} else {
	alert('Geocode was not successful for the following reason: ' + status);
	}
    });
}
