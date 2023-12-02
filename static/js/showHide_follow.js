$(document).ready(function(){   
    FollowingHide(false);
    FollowedHide(false);
    EditHide(false);
});

function FollowingShow(){
    var inp = document.getElementById("user_form");
    $("#user_form-back").show();
    inp.style.opacity = '1';
    document.getElementById("user_form").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    document.getElementById("user_form").style.visibility = "inherit";
    $("body").css("overflow","hidden"); 
}

function FollowingHide(second=true){
    var inp = document.getElementById("user_form");
    $("#user_form-back").hide();
    inp.style.opacity = '0';
    if (second) {
       document.getElementById("user_form").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s"; 
    }
    document.getElementById("user_form").style.visibility = "hidden";
    $("body").css("overflow","auto");
}

function FollowedShow(){
    var inp = document.getElementById("userFollower_form");
    $("#userFollower_form-back").show();
    inp.style.opacity = '1';
    document.getElementById("userFollower_form").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    document.getElementById("userFollower_form").style.visibility = "inherit";
    $("body").css("overflow","hidden"); 
}

function FollowedHide(second=true){
    var inp = document.getElementById("userFollower_form");
    $("#userFollower_form-back").hide();
    inp.style.opacity = '0';
    if (second) {
        document.getElementById("userFollower_form").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    }
    document.getElementById("userFollower_form").style.visibility = "hidden";
    $("body").css("overflow","auto");
}

function EditShow(){
    var inp = document.getElementById("user_form_edit");
    $("#user_form_edit-back").show();
    inp.style.opacity = '1';
    document.getElementById("user_form_edit").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    document.getElementById("user_form_edit").style.visibility = "inherit";
    $("body").css("overflow","hidden"); 
}

function EditHide(second=true){
    var inp = document.getElementById("user_form_edit");
    $("#user_form_edit-back").hide();
    inp.style.opacity = '0';
    if (second) {
        document.getElementById("user_form_edit").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    }
    document.getElementById("user_form_edit").style.visibility = "hidden";
    $("body").css("overflow","auto");
}