console.log("Getting pending accounts...");

$.get( '/admin/pending-accounts/get').done(function (data){
    data.accounts.forEach(function(account){
        addPendingAccount(account);
    });

    console.log("Got pending accounts!");
}).fail(function(res){
    console.log(res.responseText);
});

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
