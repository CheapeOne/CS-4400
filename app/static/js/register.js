$('#registration-form').submit(false); // stop redirect

$('#type-input').on('change', function() {
  if(this.value == "city scientist"){
    setupCityScientist();
  } else {
    setupCityOfficial()
  }
});


function setupCityScientist(){
    $("#registration-form").append()
}

function setupCityOfficial(){
    $("#registration-form").append()
}

function submitRegistration(){
    console.log("Registering...");
    $.post( '/register/validate', $('#registration-form').serialize()).done(function (data){
        window.location = data.destination;
    });    
}
