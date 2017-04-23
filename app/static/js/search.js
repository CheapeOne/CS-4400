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
        data.results.forEach(function(poi){
            addSearchResult(poi);
        });
    }).fail(function(res){
        console.log(res.responseText);
    });   
}

function addSearchResult(poi) {
    $("#search-results").append(`
        <tr>
            <th>`+ row.Location_Name +`</th>
            <th>`+ row.City +`</th>
            <th>`+ row.State +`</th>
            <th>`+ row.Zip_Code +`</th>
            <th>`+ row.Flagged +`</th>
            <th>`+ row.Date_Flagged +`</th>
        </tr>
    `);
}


