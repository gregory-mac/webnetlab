function isDone(timestamp) {
	timestamp = timestamp || null;
}

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