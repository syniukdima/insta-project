var username = document.getElementById("id_username");
var id_password1 = document.getElementById("id_password1");
var id_password2 = document.getElementById("id_password2");

username.setAttribute("autocapitalize", "none");
username.setAttribute("autocomplete", "username");
username.setAttribute("placeholder", "username");

id_password1.setAttribute("placeholder", "пароль");
id_password2.setAttribute("placeholder", "повтори пароль");