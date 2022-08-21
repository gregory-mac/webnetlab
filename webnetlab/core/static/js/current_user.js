$(window).on("load", function () {
    $.ajax({
        url: "/auth/me",
        type: "GET",
        dataType: "json",
        success: function(response) {
            document.getElementById("current-user").innerHTML = "Logged in as " + response["login"];
        },
        error: function(error){
            console.log(error);
        }
    });
});
