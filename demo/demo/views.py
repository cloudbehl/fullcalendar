from django.shortcuts import render
from django.http import HttpResponse
from dateutil import parser
from fullcalendar.models import CalendarEvent
from fullcalendar.util import events_to_json, calendar_options



# This is just an example for this demo. You may get this value
# from a separate file or anywhere you want

OPTIONS = """{  timeFormat: "H:mm",
                header: {
                    left: 'today',
                    center: 'prev,title,next',
                    right: 'month',
                },
                allDaySlot: false,
                firstDay: 0,
                weekMode: 'liquid',
                slotMinutes: 15,
                defaultEventMinutes: 30,
                minTime: 8,
                maxTime: 20,
                editable: true,
                selectable: true,
                contentHeight: '900',
                dayClick: function(date, allDay, jsEvent, view) {
                    if (allDay) {       
                        $('#calendar').fullCalendar('gotoDate', date)
                    }
                },
                eventMouseover: function(event, jsEvent, view) {
                      if (view.name !== 'agendaDay') {
                          $(jsEvent.target).attr('title', event.title);
                      }
                },
                eventClick: function(calEvent, jsEvent, view)
                {
                    var r=confirm("Delete " + calEvent.title);
                    if (r===true)
                      {
                          $('#calendar').fullCalendar('removeEvents', calEvent._id);
                      }
                },
                eventClick:  function(calEvent, jsEvent, view) {
                    console.log(calEvent)
                    $('#modalTitle').html(calEvent.title);
                    $('.show-modal').html(String(calEvent.start)+"<br/>"+String(calEvent.end));
                    $('#eventUrl').attr('href',event.url);
                    $('#deleteEvent').attr('event-id', calEvent.id);
                    $('#fullCalModal').modal();
                },
                select: function(start, end) {
                    enddate = $.fullCalendar.formatDate(end,'yyyy-MM-dd');
                    startdate = $.fullCalendar.formatDate(start,'yyyy-MM-dd');
                    console.log(startdate)
                    var mywhen = startdate + ' - ' + enddate;
                    $('#createEventModal #eventName').val("");
                    $('#createEventModal #apptStartDate').val(startdate);
                    $('#createEventModal #apptEndDate').val(enddate);
                    $('#createEventModal #apptStartTime').val("07:00");
                    $('#createEventModal #apptEndTime').val("08:00");
                    $('#createEventModal #when').text(mywhen);
                    $('#createEventModal').modal('show');
                },

        }"""

def index(request):
    event_url = 'all_events/'
    return render(request, 'demo/index.html', {'calendar_config_options': calendar_options(event_url, OPTIONS)})

def all_events(request):
    events = CalendarEvent.objects.all()
    return HttpResponse(events_to_json(events), content_type='application/json')

def delete(request):
    delete_id = request.POST.get('id')
    if delete_id:
        delete_event = CalendarEvent.objects.get(id = delete_id)
        delete_event.delete()
    event_url = 'all_events/'
    return render(request, 'demo/index.html', {'calendar_config_options': calendar_options(event_url, OPTIONS)})

def create(request):
    title = request.POST.get('title')
    start = request.POST.get('startdate') +" "+ request.POST.get('start') 
    end = request.POST.get('enddate') +" "+ request.POST.get('end')
    allDay = True if request.POST.get('allDay')=="true" else False
    calenderobj = CalendarEvent(title=title,start = parser.parse(start),end = parser.parse(end),all_day = allDay)
    calenderobj.save()
    event_url = 'all_events/'
    return render(request, 'demo/index.html', {'calendar_config_options': calendar_options(event_url, OPTIONS)})

