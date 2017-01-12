$(document).ready(function() {
  $('#deleteEvent').on('click', function(e){
 	$('#fullCalModal').modal("hide");
 	e.preventDefault();
 	$.ajax({
 	   url : "/delete",
 	   type: "POST",
 	   beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    	},
       data: {
       	id : $("#deleteEvent").attr("event-id")
       },
       success: function () {
       	  $('#calendar').fullCalendar( 'refetchEvents' );
          $('#calendar').fullCalendar('removeEvents', parseInt($("#deleteEvent").attr("event-id")));
       }
   });
 });
 $('#submitButton').on('click', function(e){
 	$("#createEventModal").modal('hide');
 	e.preventDefault();
    var csrftoken = getCookie('csrftoken');
    var title =  $('#eventName').val();
	var start = $('#apptStartTime').val();
	var end = $('#apptEndTime').val();
	var startDate = $('#apptStartDate').val();
	var endDate = $('#apptEndDate').val();
	var allDay = ($('#apptAllDay:checked').val() == "on");
   
 $.ajax({
 url : "/create", // the endpoint,commonly same url
 type : "POST", // http method
 data : { csrfmiddlewaretoken : csrftoken, 
 title : title,
 start : start,
 startdate : startDate,
 end: end,
 enddate: endDate,
 allDay: allDay
 }, // data sent with the post request

        // handle a successful response
        success : function(json) {
        	$('#calendar').fullCalendar( 'refetchEvents' );
            console.log("Done");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
	});
 	function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
});