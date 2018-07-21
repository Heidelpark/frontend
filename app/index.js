var mapboxgl = require('mapbox-gl/dist/mapbox-gl.js');
 
mapboxgl.accessToken = 'pk.eyJ1IjoiaGVpZGVscGFyayIsImEiOiJjamp2NjkxaTc0dmQxM3BybWR3czAwemlyIn0.8wIK9XCuy90FnVDV9iXEVg';
var map = new mapboxgl.Map({
container: 'YOUR_CONTAINER_ELEMENT_ID',
style: 'mapbox://styles/mapbox/streets-v10'
});
