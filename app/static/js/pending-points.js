console.log("Getting pending points...");

$.get( '/admin/pending-points/get').done(function (data){
    console.log(data);
}).fail(function(res){
    console.log(res.responseText);
});
