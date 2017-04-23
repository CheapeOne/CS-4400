// Add universal javascript here
function addStates(dropdownId){
    console.log("Getting States...");
    $.get( '/city-state/states').done(function (data){
        data.states.forEach(function(state){
            addState(state, dropdownId);
        });
        console.log("Got States!");
    });
}

function addState(state, dropdownId) {
    $(dropdownId).append(`
        <option>`+ state.State +`</option>
    `);
}

// Add universal javascript here
function addCities(dropdownId){
    console.log("Getting Cities...");
    $.get( '/city-state/cities').done(function (data){
        data.cities.forEach(function(city){
            addCity(city, dropdownId);
        });
        console.log("Got Cities!");
    });
}

function addCity(city, dropdownId) {
    $(dropdownId).append(`
        <option>`+ city.City +`</option>
    `);
}

// Add universal javascript here
function addLocations(dropdownId){
    console.log("Getting POIs...");
    $.get( '/poi/locations').done(function (data){
        data.locations.forEach(function(location){
            addLocation(location, dropdownId);
        });
        console.log("Got POIs!");
    });
}

function addLocation(location, dropdownId) {
    $(dropdownId).append(`
        <option>`+ location.Location_Name +`</option>
    `);
}
