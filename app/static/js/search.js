// A $( document ).ready() block.
$( document ).ready(function() {
    addStates("#state-input");
    addCities("#city-input");
    addLocations("#poi-input");
});

function searchPOI(){
    console.log("Searching POIs...");

    $.get('/city-official/poi-search/get-results', $("#search-form :input[value!='']").filter(function(index, element) {
        return $(element).val() != "";
    }).serialize()).done(function (data){
        console.log(data)

        $(".result").remove();

        data.msg.forEach(function(poi){
            addSearchResult(poi);
        });

        $('#search-table').DataTable();
    }).fail(function(res){
        console.log(res.responseText);
    });   
}

function addSearchResult(poi) {

    flagged = poi.Flagged ? "Yes" : "No";

    $("#search-results").append(`
        <tr class="result">
        <th> <a href="/city-official/poi-detail?poi=`+ poi.Location_Name +`">`+ poi.Location_Name +`</a></th>
            <th>`+ poi.City +`</th>
            <th>`+ poi.State +`</th>
            <th>`+ poi.Zip_Code +`</th>
            <th>`+ flagged +`</th>
            <th>`+ poi.Date_Flagged +`</th>
        </tr>
    `);
}


