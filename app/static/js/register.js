$('#registration-form').submit(false); // stop redirect

function submitRegistration(){
    console.log("Registering...");
    $.post( '/register/validate', $('#registration-form').serialize()).done(function (data){
        console.log(data);
    });    
}
