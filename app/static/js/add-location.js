// A $( document ).ready() block.
$( document ).ready(function() {
    addStates("#state-input");
    addCities("#city-input");
});

$('#add-location-form').submit(false); // stop redirect

function submitLocation(){
    console.log("Adding location...");
    $.post( '/city-scientist/add-location/validate', $('#add-location-form').serialize()).done(function (data){
        window.location = data.destination;
    });    
}