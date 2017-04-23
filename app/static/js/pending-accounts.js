console.log("Getting pending accounts...");

$.get( '/admin/pending-accounts/get').done(function (data){
    console.log(data);
}).fail(function(res){
    console.log(res.responseText);
});
