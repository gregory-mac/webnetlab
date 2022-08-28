function isDone(timestamp) {
	timestamp = timestamp || null;
}

function lock_deploy_button() {
	$("#deploy").addClass('disabled');
}

function unlock_deploy_button() {
	$("#deploy").removeClass('disabled');
}

function lock_destroy_button() {
	$("#destroy").addClass('disabled');
}

function unlock_destroy_button() {
	$("#destroy").removeClass('disabled');
}

function lock_status_button() {
	$("#lab-status").addClass('disabled');
}

function unlock_status_button() {
	$("#lab-status").removeClass('disabled');
}

function update_status() {
	let current_status = $("#lab-status");
	let current_status_indicator = current_status.children();

	$.ajax({
		url: "/lab/status",
		type: "POST",
		dataType: "json",
		success: function(response) {
			if (response["is_running"]===true){
				current_status.text("\xa0Lab status: online (" + response["lab_name"] + ")");
				current_status.prepend(current_status_indicator);
				$("#lab-status-indicator")
					.css('color', 'ForestGreen')
					.addClass("tada animated infinite");
			} else {
				current_status.text("\xa0Lab status: offline");
				current_status.prepend(current_status_indicator);
				$("#lab-status-indicator")
					.css('color', 'coral')
					.removeClass("tada animated infinite");
			}
			return response;
		},
		error: function(error){
			console.log(error);
			current_status.text("\xa0Lab status: unknown");
			current_status.prepend(current_status_indicator);
			$("#lab-status-indicator")
				.css('color', 'gray')
				.removeClass("tada animated infinite");
			return error;
		}
	});
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
					unlock_deploy_button();
					update_status();
                }
            },
			error: function(error){
				unlock_deploy_button();
				console.log(error);
			}
		});
	});
});

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
					unlock_destroy_button();
					update_status();
                }
            },
			error: function(error){
				unlock_destroy_button();
				console.log(error);
			}
		});
	});
});

$(function(){
	$("#lab-status").on("click", function(){
		lock_status_button();
		update_status();
		unlock_status_button();
	});
});
