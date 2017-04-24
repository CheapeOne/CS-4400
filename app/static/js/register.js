$('#registration-form').submit(false); // stop redirect

$('#type-input').on('change', function() {

    console.log(this.value);

  if(this.value == "City Scientist"){
    setupCityScientist();
  } else {
    setupCityOfficial()
  }
});


function setupCityScientist(){
    $("#registration-form .city-official").remove();

    $('#register-button').attr('onclick','submitScientistRegistration()');
}


function setupCityOfficial(){
    $("#registration-form").append(`
        <div class="form-group city-official">
            <label for="city-input">City</label>
            <select name="city" class="form-control" id="city-input">
                <!-- gotten from db -->
            </select>
        </div>

        <div class="form-group city-official">
            <label for="state-input">State</label>
            <select name="state" class="form-control" id="state-input">
                <!-- gotten from db -->
            </select>
        </div>

        <div class="form-group city-official">
            <label for="title-input">Title</label>
            <input type="text" name="title" class="form-control" id="title-input" placeholder="Enter the location's name">
        </div>
    `);

    addStates("#state-input");
    addCities("#city-input");

    $('#register-button').attr('onclick','submitOfficialRegistration()');
}

function submitScientistRegistration(){
    console.log("Registering Scientist...");
    $.post( '/register/scientist/validate', $('#registration-form').serialize()).done(function (data){
        window.location = data.destination;
    });    
}

function submitOfficialRegistration(){
    console.log("Registering Official...");
    $.post( '/register/official/validate', $('#registration-form').serialize()).done(function (data){
        window.location = data.destination;
    });    
}
