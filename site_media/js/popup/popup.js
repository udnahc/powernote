/***************************/
//@Author: Adrian "yEnS" Mato Gondelle
//@website: www.yensdesign.com
//@email: yensamg@gmail.com
//@license: Feel free to use it, but keep this credits please!
/***************************/

//SETTING UP OUR POPUP
//0 means disabled; 1 means enabled;
var popupStatus = 0;

//loading popup with jQuery magic!
function loadPopup(){
    //loads popup only if it is disabled
    if(popupStatus==0){
        $("#backgroundPopup").css({
            "opacity": "0.7"
        });
        $("#backgroundPopup").fadeIn("slow");
        $("#popupContact").fadeIn("slow");
        popupStatus = 1;
    }
}

//disabling popup with jQuery magic!
function disablePopup(){
    //disables popup only if it is enabled
    if(popupStatus==1){
        $("#backgroundPopup").fadeOut("slow");
        $("#popupContact").fadeOut("slow");
        $('.jSticky-medium').show()
        popupStatus = 0;
    }
}

function processPopup(note_idn) {
    $('.jSticky-medium').hide();
    $('.jSticky-medium[note_id=' + note_idn + ']').show();
    centerPopup();
    loadPopup();
}

//centering popup
function centerPopup(){
    //request data for centering
    var windowWidth = document.body.clientWidth;
    var windowHeight = document.body.clientHeight;
    var popupHeight = $("#popupContact").height();
    var popupWidth = $("#popupContact").width();
    //centering
    $("#popupContact").css({
        "position": "absolute",
        "top": windowHeight/2-popupHeight/2,
        "left": windowWidth/2-popupWidth/2
    });
    //only need force for IE6
    
    $("#backgroundPopup").css({
        "height": windowHeight
    });
    
}


//CONTROLLING EVENTS IN jQuery
$(document).ready(function(){
    
    //CLOSING POPUP
    //Click the x event!
    $("#popupContactClose").click(function(){
        disablePopup();
    });
    //Click out event!
    $("#backgroundPopup").click(function(){
        disablePopup();
    });
    //Press Escape event!
    $(document).keypress(function(e){
        if(e.keyCode==27 && popupStatus==1){
            disablePopup();
        }
    });

});