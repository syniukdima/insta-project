$(document).ready(function(){   
    UserHide();
});

function UserShow(){
    var inp = document.getElementById("user_create-in-a-mobile");
    document.getElementById("user_create-in-a-mobile").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    if (document.getElementById("user_create-in-a-mobile").style.visibility != "hidden"){
        inp.style.opacity = '0';
        document.getElementById("user_create-in-a-mobile").style.visibility = "hidden";
    }
    else {
        inp.style.opacity = '1';
        document.getElementById("user_create-in-a-mobile").style.visibility = "inherit";
    }
    
}

function UserHide(){
    var inp = document.getElementById("user_create-in-a-mobile");
    inp.style.opacity = '0';
    // if (!second) {
    //     console.log("aboba");
    //    document.getElementById("user_create-in-a-mobile").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s"; 
    // }
    document.getElementById("user_create-in-a-mobile").style.visibility = "hidden";
}