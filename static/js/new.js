var refreshTimer = 0;
var firsttime = 0;

$('.stopsearch, .esfnp').on('click', function(event){
    clearInterval(refreshTimer);
    $(".stopsearch, .searchingforpartner, .partnerleft, .connected, .newchat, .esfnp").addClass("hide");
    $(".startchat, .notconnected").removeClass("hide");
    $.ajax({
        url : "stop",
        type : "GET",
        data: {sess:  $('#session').attr('class')},
        success : function(data){
        },error: function(data) 
        {}
    });
});


$('.startchat, .esfnp, .newchat').on('click', function(event){
    firsttime = 0;
    $(".startchat, .newchat").addClass("hide");
    $(".chat-history").addClass("disabled");
    $(".sendbutton").addClass("unactive");
    document.getElementById("message-to-send").value = "";
    $("textarea").attr("disabled","disabled");
    $("#messages").empty();
    clearInterval(refreshTimer);
    $.ajax({
        url : "connect",
        type : "GET",
        success : function(data){
            toastr.clear();
            $(".partnerleft, .connected, .notconnected, .startchat, .newchat, .esfnp").addClass("hide");
            $(".stopsearch,  .searchingforpartner").removeClass("hide");
            $("#session").removeClass();
            $("#session").addClass(data.session_id);
            refreshTimer = setInterval(getMessages, 2000);
        },error: function(data) 
            {           toastr.clear();
                        toastr.options.positionClass = 'toast-top-right';
                        toastr.options.preventDuplicates = 'true';
                        toastr.error("Something went wrong");
                        $(".startchat").removeClass("hide");     

            }
    });
});




function gettime() {
var dt = new Date();
var hours = dt.getHours();
var minutes  = dt.getMinutes();
var hours = (hours+24)%24; 
var mid='AM';
if(hours==0){ //At 00 hours we need to show 12 am
hours=12;
}
else if(hours>12)
{
hours=hours%12;
mid='PM';
}
return(hours +':' +minutes + ' '+ mid);       
}





$('#sendbutton').on('click', function(event){
    var message = $('#message-to-send').val().trim();
    if (message !== '')
    {
        $.ajax({
            url : "/send/",
            type : "GET",
            data : { msgbox : message, session : $('#session').attr('class') },
            dataType: "json",
            success : function(data){
                var newhtml =  '<li class="clearfix">\
                <div class="message-data align-right" >\
                <span class="message-data-time" >' + gettime() +', Today</span> &nbsp; &nbsp;\
                <span class="message-data-name" >You</span> <i class="fa fa-circle me"></i>\
                </div><div class="message other-message float-right">' +    message +    '</div></li>';
                $('#messages').append(newhtml); 
                $('#message-to-send').val('');

                element = $("#messages")[0];
                $('.chat-history').animate({scrollTop: element.scrollHeight});     
            },        
            error: function(data) 
            {           toastr.clear();
                        toastr.options.positionClass = 'toast-top-right';
                        toastr.options.preventDuplicates = 'true';
                        toastr.error("Something went wrong");                                                
            }
        });
    }
});



$("#message-to-send").keyup(function(event){
    if(event.keyCode == 13){
        $("#sendbutton").click();
    }
});

function getMessages(){
    var session = $('#session').attr('class');

    $.ajax({
        type: "GET",
        url:"/check/",
        dataType: "json",
        data: {sess: session},
        success: function(data) 
        { 
            if (data.flag==0 || data.flag ==1)
            {
                $(".stopsearch, .searchingforpartner, .partnerleft, .notconnected, .startchat, .newchat").addClass("hide");
                $(".connected, .esfnp").removeClass("hide");
                $(".chat-history").removeClass("disabled");
                $(".sendbutton").removeClass("unactive");
                $("textarea").removeAttr("disabled");
                if (firsttime == 0)
                {
                        toastr.clear();
                        toastr.options.positionClass = 'toast-top-right';
                        toastr.options.preventDuplicates = 'true';
                        toastr.success("You're now chatting with a random stranger. Say hi!");
                        firsttime = 1;
                }

                if (data.flag == 0)
                {
                    var newhtml = '<li>\
                    <div class="message-data">\
                    <span class="message-data-name"><i class="fa fa-circle online"></i> Anonymous</span>\
                    <span class="message-data-time">'+ gettime() +', Today</span></div>\
                    <div class="message my-message">' + data.message + '</div></li>';
                    $('#messages').append(newhtml); 
                    $('#message-to-send').val('');
                    element = $("#messages")[0];
                    $('.chat-history').animate({scrollTop: element.scrollHeight});     
                }
            }

            else if (data.flag == 2)
            {
                $(".stopsearch, .searchingforpartner, .connected, .notconnected, .startchat, .esfnp").addClass("hide");
                $(".partnerleft, .newchat").removeClass("hide");
                $(".chat-history").addClass("disabled");
                $(".sendbutton").addClass("unactive");
                document.getElementById("message-to-send").value = "";
                $("textarea").attr("disabled","disabled");
                clearInterval(refreshTimer);
                if (firsttime == 1)
                {
                    firsttime = 0;
                    toastr.clear();
                    toastr.options.positionClass = 'toast-top-right';
                    toastr.options.preventDuplicates = 'true';
                    toastr.info("Partner left");
                }
            }
            else
            {}
        },
        error: function(data) 
        {                                                    
        }
    });
}


function getOnline(){
    $.ajax({
    url : "/count/",
    type : "GET",
    dataType: "json",
    success : function(data){
        var newhtml = '<i class="fa fa-circle online"></i> online : ' + data.online;
        $( ".totalonline" ).empty();
        $('.totalonline').append(newhtml); 
    }
    });
}
setInterval(getOnline, 5000);


