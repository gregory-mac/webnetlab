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

function lock_destroy_button() {
	$("#destroy").addClass('disabled');
}

function unlock_destroy_button() {
	$("#destroy").removeClass('disabled');
}

$(function(){
	$("#destroy").on("click", function(){
		lock_destroy_button();
        let lab_name = window.location.pathname.split("/").pop()
		$.ajax({
			url: "/lab/" + lab_name + "/destroy",
			type: "POST",
			success: function(response) {
                if (response.done === false) {
                    isDone(Date.now());
                } else {
                    console.log(response);
					unlock_destroy_button();
                }
            },
			error: function(error){
				unlock_destroy_button();
				console.log(error);
			}
		});
	});
});

function check_status() {
	$.ajax({
		url: "/lab/status",
		type: "POST",
		success: function(response) {
			return response;
		},
		error: function(error){
			console.log(error);
			return error;
		}
	});
}
