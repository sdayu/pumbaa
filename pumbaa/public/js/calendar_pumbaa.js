/**
 * calendarDemoApp - 0.1.3
 */
angular.module('calendarPumbaaApp', ['ui.calendar', 'ui.bootstrap']);

function CalendarCtrl($scope, $http) {
    var date = new Date();
    var d = date.getDate();
    var m = date.getMonth();
    var y = date.getFullYear();
    
    /* event source that pulls from google.com */
    $scope.holidaySource = {
            url: "//www.google.com/calendar/feeds/th__th%40holiday.calendar.google.com/public/basic",
            // className: 'gcal-event',           // an option!
            currentTimezone: 'Thailand/Bangkok', // an option!
            color:'#d2322d'
    };
    
    /* event source that contains custom events on the scope */
    $scope.pumbaaSources={}

    $scope.init = function(eventConfs){
    	eventConfs.forEach(function(conf){
    		name = conf.name;
    		$scope.pumbaaSources[name] = {
    		    	url:"/apis/events?render=fullcalendar&event_type="+name,
    		    	dataType: 'json',
    		    	cache: true
    		};
    		
    		angular.forEach(conf, function(value, key) {
    		   if (key != 'name'){
    			 $scope.pumbaaSources[name][key] = value;
    		   }
    		});
    		
    		$scope.eventSources.push($scope.pumbaaSources[name]);
    	});
    };
    
    /* alert on eventClick */
    $scope.alertOnEventClick = function( event, allDay, jsEvent, view ){
        $scope.alertMessage = (event.title + ' was clicked ');
    };
    /* alert on Drop */
     $scope.alertOnDrop = function(event, dayDelta, minuteDelta, allDay, revertFunc, jsEvent, ui, view){
       $scope.alertMessage = ('Event Droped to make dayDelta ' + dayDelta);
    };
    /* alert on Resize */
    $scope.alertOnResize = function(event, dayDelta, minuteDelta, revertFunc, jsEvent, ui, view ){
       $scope.alertMessage = ('Event Resized to make dayDelta ' + minuteDelta);
    };
    /* add and removes an event source of choice */
    $scope.addRemoveEventSource = function(sources,source) {
      var canAdd = 0;
      angular.forEach(sources,function(value, key){
        if(sources[key] === source){
          sources.splice(key,1);
          canAdd = 1;
        }
      });
      if(canAdd === 0){
        sources.push(source);
      }
    };
    /* add custom event*/
    $scope.addEvent = function() {
      $scope.events.push({
        title: 'Open Sesame',
        start: new Date(y, m, 28),
        end: new Date(y, m, 29),
        className: ['openSesame']
      });
    };
    /* remove event */
    $scope.remove = function(index) {
      $scope.events.splice(index,1);
    };
    /* Change View */
    $scope.changeView = function(view,calendar) {
      calendar.fullCalendar('changeView',view);
    };
    /* Change View */
    $scope.renderCalender = function(calendar) {
      if(calendar){
        calendar.fullCalendar('render');
      }
    };
    /* config object */
    $scope.uiConfig = {
      calendar:{
        height: 450,
        editable: false,
        timeFormat: 'H:mm',
        header:{
          left: 'title',
          center: '',
          right: 'today prev,next'
        },
        // eventClick: $scope.alertOnEventClick,
        // eventDrop: $scope.alertOnDrop,
        // eventResize: $scope.alertOnResize
      }
    };

    /* event sources array*/
    $scope.eventSources = [$scope.holidaySource];
    // $scope.eventSources = [$scope.events, $scope.eventSource, $scope.eventsF];
    // $scope.eventSources2 = [$scope.calEventsExt, $scope.eventsF, $scope.events];
}
/* EOF */
