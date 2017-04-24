console.log("Getting pending points...");

$.get( '/admin/pending-points/get').done(function (data){
    data.points.forEach(function(point){
        addPendingPoint(point);
    });
    console.log("Got pending points!");
}).fail(function(res){
    console.log(res.responseText);
});


function addPendingPoint(point) {

    datetime_string = convertDateForSQL(point.Date_Time);

    $("#pending-points").append(`
        <tr>
            <th>` + point.POI_Location_Name + `</th>
            <th>` + point.Data_Type + `</th>
            <th>` + point.Data_Value + `</th>
            <th>` + point.Date_Time + `</th>
            <th><a href="/admin/pending-points/accept?poi=` + point.POI_Location_Name + `&time=` + datetime_string + `" class="card-link btn btn-success">Accept</a></th>
            <th><a href="/admin/pending-points/reject?poi=` + point.POI_Location_Name + `&time=` + datetime_string + `" class="card-link btn btn-danger">Reject</a></th>
        </tr>
    `);
}
