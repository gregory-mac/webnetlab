function isDone(timestamp) {
	timestamp = timestamp || null;
}

function lock_button() {
	$("button[name='deploy']")
		.prop('disabled', true)
		.addClass('is-loading');
}

function unlock_button() {
	$("button[name='deploy']")
		.prop('disabled', false)
		.removeClass('is-loading');
}

$(function(){
	$("button[name='deploy']").on("click", function(){
		lock_button();
        let lab_name = window.location.pathname.split("/").pop()
		$.ajax({
			url: "/lab/" + lab_name + "/deploy",
			type: "POST",
			success: function(response) {
                if (response.done === false) {
                    isDone(Date.now());
                } else {
                    console.log(response);
					unlock_button();
                }
            },
			error: function(error){
				console.log(error);
				unlock_button();
			}
		});
	});
});