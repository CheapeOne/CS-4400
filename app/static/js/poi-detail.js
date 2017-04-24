
var poi = "";

// A $( document ).ready() block.
$( document ).ready(function() {

    poi = getParameterByName("poi");
    console.log(poi);

    $("#poi-name").text("POI Details: " + poi);

    addInitialDataPoints(poi);

    addDataTypes("#type-input");

    checkFlagged(poi);

    $('#detail-table').DataTable();
});

function checkFlagged(poi) {
    var isFlagged = getIsFlagged(poi);

    if(isFlagged){
        $("#flag-button").hide();
    } else {
        $("#unflag-button").hide();
    }
}

function getIsFlagged(poi){
    console.log("Getting is flagged...");
    $.get( '/city-official/poi-detail/is-flagged?poi='+poi).done(function (data){
        console.log("Got is flagged ");
        console.log(data.flagged[0].Flagged);
        return data.flagged[0].Flagged;
    }).fail(function(res){
        console.log(res.responseText);
    });     
}

function flagPOI(flagged){
    console.log("Setting is flagged...");
    $.get( '/city-official/poi-detail/set-flagged?poi='+poi+"&flagged="+flagged).done(function (data){
        console.log("Set is flagged ");
        console.log(data.flagged[0].Flagged);
        
        if(flagged){
            //if we just flagged, hide the flag button and show the unflag button
            $("#flag-button").hide();
            $("#unflag-button").show();
        } else {
            $("#flag-button").show();
            $("#unflag-button").hide();
        }

    }).fail(function(res){
        console.log(res.responseText);
    }); 
} 

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
