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

// $(window).on("load", function () {
//     let status = check_status();
// 	console.log(status)
// });

// $(function(){
// 	$("button[name='deploy']").on("click", function(){
// 		lock_button();
//         let lab_name = window.location.pathname.split("/").pop()
// 		$.ajax({
// 			url: "/lab/" + lab_name + "/deploy",
// 			type: "POST",
// 			success: function(response) {
//                 if (response.done === false) {
//                     isDone(Date.now());
//                 } else {
//                     console.log(response);
// 					unlock_button();
//                 }
//             },
// 			error: function(error){
// 				unlock_button();
// 				console.log(error);
// 			}
// 		});
// 	});
// });