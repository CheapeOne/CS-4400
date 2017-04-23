$.get( '/city-official/poi-report/make').done(function (data){
    console.log(data);
}).fail(function(res){
    console.log(res.responseText);
});