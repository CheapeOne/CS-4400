
console.log("Getting report...");
$.get( '/city-official/poi-report/make').done(function (data){
    data.report.forEach(function(row){
        addReportRow(row);
    });
    console.log("Got report!");
}).fail(function(res){
    console.log(res.responseText);
});

function addReportRow(row) {
    $("#report").append(`
        <tr>
            <th>`+ row.Location_Name +`</th>
            <th>`+ row.City +`</th>
            <th>`+ row.State +`</th>
            <th>`+ row.Mold_Min +`</th>
            <th>`+ row.Mold_Avg +`</th>
            <th>`+ row.Mold_Max +`</th>
            <th>`+ row.AQ_Min +`</th>
            <th>`+ row.AQ_Avg +`</th>
            <th>`+ row.AQ_Max +`</th>
            <th>`+ row.Num_Points +`</th>
            <th>`+ row.Flagged +`</th>
        </tr>
    `);
}