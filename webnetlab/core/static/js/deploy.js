function isDone(timestamp) {
	timestamp = timestamp || null;
}

function lock_deploy_button() {
	$("#deploy").addClass('disabled');
}

function unlock_deploy_button() {
	$("#deploy").removeClass('disabled');
}

$(function(){
	$("#deploy").on("click", function(){
		lock_deploy_button();
        let lab_name = window.location.pathname.split("/").pop()
		$.ajax({
			url: "/lab/" + lab_name + "/deploy",
			type: "POST",
			success: function(response) {
                if (response.done === false) {
                    isDone(Date.now());
                } else {
                    console.log(response);
					unlock_deploy_button();
                }
            },
			error: function(error){
				unlock_deploy_button();
				console.log(error);
			}
		});
	});
});