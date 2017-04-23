$('#login-form').submit(false); // stop redirect

function submitLogin(){
    console.log("Logging in...");
    $.post( '/login/validate', $('#login-form').serialize()).done(function (data){
        window.location = data.destination;
    });    
}
