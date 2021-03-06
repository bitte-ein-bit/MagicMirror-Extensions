//connect do Call monitor
//localStorage.debug = '*';

//Add callmonitor CSS 
$('body').append('<link rel="stylesheet" href="js/extensions/paviro/css/style.css">')

//Add call alert
$('body').append(`

<div class="center-ver center-hor">

<div id="call" class="light"><img src="img/phone.png" height="80px"><h2>Incoming call</h2><div id="caller"></div></div>

<div id="anmeldung" class="light"><h2>Welcome</h2><div id="anmelde_name"></div></div>

</div>

`);


function switchview(person) {
    if (person !="Abgemeldet" && person !="Unbekannt"){
        //Set calender URL for logged in user currently only one URL is supported.
        config.calendar.url = "https://p01-calendars.icloud.com/published/2/VKQg_p6ix87HS6MvIjlTei4qNezXSJqqDGc0WtYJYDZ9qY5hpNYfZyS_NrQ1M-JeXgrrce6DsYqGwIVmG6JstCoDgdHfgj5VhWrFatFQG_w"
        calendar.updateData()
    }
    if (person == "Abgemeldet"){
        //set URL for not logged in user.
        config.calendar.url = "http://ifeiertage.de/bw-sk.ics"
        calendar.updateData()
    };
};


var socket = io.connect('http://localhost:1234');

socket.on('anruf', function (data){
    if (data != 'clear'){
            $('#call').fadeIn(700);
            $('.lower-third').fadeOut(700);
            $('#caller').text(data);
    }
    if (data == 'clear'){
    $('#call').fadeOut(700);
    $('.lower-third').fadeIn(700);
    }
});

socket.on('Gesicht', function (data) {
    if (data != "Abgemeldet"){
        $('#anmeldung').fadeIn(700);
        $('.lower-third').fadeOut(700);
        $('#anmelde_name').text(data);
        $('#anmeldung').delay(5000).fadeOut(700);
        $('.lower-third').delay(5000).fadeIn(700);
    };
    switchview(data)
});