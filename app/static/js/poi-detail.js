console.log("Getting report...");
$.get( '/city-official/poi-detail/details').done(function (data){
    data.report.forEach(function(row){
        addDetailRow(row);
    });
    console.log("Got report!");
}).fail(function(res){
    console.log(res.responseText);
});

function addDetailRow(row) {
    $("#detail").append(`
        <tr>
            <th>`+ row.Data_Type +`</th>
            <th>`+ row.Data_Value +`</th>
            <th>`+ row.Date_Time +`</th>
            <th>`+ (row.Flagged ? row.Date_Flagged : 'No') +`</th>
            <th>`+ `Action goes here` +`</th>
        </tr>
    `);
}
