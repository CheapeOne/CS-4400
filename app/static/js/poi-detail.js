// A $( document ).ready() block.
$( document ).ready(function() {

    var poi = getParameterByName("poi");
    console.log(poi);

    $("#poi-name").text("POI Details: " + poi);

    addInitialDataPoints(poi);

    addDataTypes("#type-input");
});

function addInitialDataPoints(poi){
    console.log("Getting initial data points...");
    $.get( '/city-official/poi-detail/all?poi='+poi).done(function (data){
        console.log(data);
        data.points.forEach(function(point){
            addDetailRow(point);
        });
        console.log("Got initial data points!");
    }).fail(function(res){
        console.log(res.responseText);
    });
}


function filterDataPoints(){
    $.get( '/city-official/poi-detail/details').done(function (data){
    data.points.forEach(function(point){
        addDetailRow(point);
    });
    console.log("Got report!");
    }).fail(function(res){
        console.log(res.responseText);
    });
}


function addDetailRow(point) {
    $("#detail").append(`
        <tr>
            <th>`+ point.Data_Type +`</th>
            <th>`+ point.Data_Value +`</th>
            <th>`+ point.Date_Time +`</th>
        </tr>
    `);
}
