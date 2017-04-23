console.log("Searching POIs...");
$.get( '/city-official/poi-search/get-results').done(function (data){
    console.log(data);
}).fail(function(res){
    console.log(res.responseText);
});    