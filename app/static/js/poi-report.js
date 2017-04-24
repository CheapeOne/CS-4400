
console.log("Getting report...");
$.get( '/city-official/poi-report/make').done(function (data){
    console.log(data);
    data.report.forEach(function(row){
        addReportRow(row);
    });
    console.log("Got report!");
}).fail(function(res){
    console.log(res.responseText);
});

function addReportRow(row) {
    flagged = "";
    if(row.Flagged == 0){
        flagged = "No";
    } else {
        flagged = "Yes";
    }

    $("#report").append(`
        <tr>
            <th>`+ row.POI_Location_Name +`</th>
            <th>`+ row.City +`</th>
            <th>`+ row.State +`</th>
            <th>`+ row.min_value_mold +`</th>
            <th>`+ row.avg_value_mold +`</th>
            <th>`+ row.max_value_mold +`</th>
            <th>`+ row.min_value_airquality +`</th>
            <th>`+ row.avg_value_airquality +`</th>
            <th>`+ row.max_value_airquality +`</th>
            <th>`+ (row.count_airquality + row.count_mold) +`</th>
            <th>`+ flagged +`</th>
        </tr>
    `);
}