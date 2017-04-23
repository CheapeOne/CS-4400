$('#add-point-form').submit(false); // stop redirect

function submitPoint(){
    console.log("Adding point...");
    $.post( '/city-scientist/add-point/validate', $('#add-point-form').serialize()).done(function (data){
        window.location = data.destination;
    });    
}
