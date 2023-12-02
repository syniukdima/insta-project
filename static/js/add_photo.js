function add_photo(input_element, id_photo, img_id) {
    $(input_element).on('change', function () {
        var input = $(this)
        if (input[0].files && input[0].files[0]) {
            let f = input[0].files[0];
            img = document.getElementById(id_photo);
            if (f) {
                img.src = URL.createObjectURL(f);
                localStorage.setItem('myImage', img.src);
            }
            img.classList.add(id_photo);
        }
        var img = document.getElementById(img_id);
        img.style.display = 'block';
    })
}

function hide(id_input){
        var el = $(id_input);
        el[0].value = "";
}
 

function hideAvatar() {
    var drop = document.getElementById('id_avatar-hide-img');
    drop.style.display = 'none';
    var img = document.getElementById('id_avatar_show-photo');
    img.classList.remove('id_avatar_show-photo');
    img.src = "";
    hide('input[id="id_avatar"]');
}

function hideBackground() {
    var drop = document.getElementById('id_background-hide-img');
    drop.style.display = 'none';
    var img = document.getElementById('id_background_show-photo');
    img.classList.remove('id_background_show-photo');
    img.src = "";
    hide('input[id="id_background"]');
}

add_photo('input[id="id_avatar"]', 'id_avatar_show-photo', 'id_avatar-hide-img');
add_photo('input[id="id_background"]', 'id_background_show-photo', 'id_background-hide-img');