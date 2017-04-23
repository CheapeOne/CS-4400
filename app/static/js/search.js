// A $( document ).ready() block.
$( document ).ready(function() {
    addStates("#state-input");
    addCities("#city-input");
    addLocations("#poi-input");
});

function searchPOI(){
    console.log("Searching POIs...");
    $.get( '/city-official/poi-search/get-results', $('#search-form').serialize()).done(function (data){
        console.log(data);
    }).fail(function(res){
        console.log(res.responseText);
    });   
}

function addPendingAccount(account) {
    $("#pending-accounts").append(`
        <tr>
            <th>` + account.Username + `</th>
            <th>` + account.Email + `</th>
            <th>` + account.City + `</th>
            <th>` + account.State + `</th>
            <th>` + account.Title + `</th>
            <th><a href="/admin/pending-accounts/accept?user=` + account.Username + `" class="card-link btn btn-success">Accept</a></th>
            <th><a href="/admin/pending-accounts/reject?user=` + account.Username + `" class="card-link btn btn-danger">Reject</a></th>
        </tr>
    `);
}


