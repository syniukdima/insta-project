var id = JSON.parse(document.getElementById('json-posts').textContent);
const comment_username = JSON.parse(document.getElementById('json-comment-username').textContent);
const comment_realusername = JSON.parse(document.getElementById('json-comment-realusername').textContent);
const imgUrl = JSON.parse(document.getElementById('json-img').textContent);
const imgUrl_no = JSON.parse(document.getElementById('json-img-no').textContent);
const url_dell = JSON.parse(document.getElementById('json-url_dell').textContent);

// створюємо новий об'єкт вебсокету
const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + 'comment/'
    + id
    + '/'
);

// відкриває
socket.onopen = function (e) {
    console.log("CONNECTION ESTABLISHED");
}

// закриває
socket.onclose = function (e) {
    console.log("CONNECTION LOST");
}

// помилки
socket.onerror = function (e) {
    console.log("ERROR OCCURED");
}

// повідомлення
socket.onmessage = function (e) {
    // отримуємо дату
    var currentdate = new Date();
    // створюємо шаблон за яким дата буде виводитися в потрібному нам вигляді
    var datetime =
        + ((currentdate.getHours()) < 10 ? "0" + currentdate.getHours() : currentdate.getHours()) + ":"
        + ((currentdate.getMinutes()) < 10 ? "0" + currentdate.getMinutes() : currentdate.getMinutes());
    // отримуємо данні з chats.consumers.py    
    const data = JSON.parse(e.data);
    
    // перевірка на пустий рядок
    if (data.message != "") {
        active_img = ``;
        if (data.is_superuser) {
            active_img = `<img src="${imgUrl}" alt="premium" class="premium-img" />`
        }
        
        // виводить коментарій
        document.querySelector('#comment_for_post').innerHTML += `<div class="user_post">
            <img
              class="avatar online"
              src="${data.avatar}"
              alt="avatar"
            />
              <div class="about_user">
                
                <a href="${data.url}" class="nickname_post">${data.username}
                    ${active_img}
                </a>
                <span class="comment_text post_subtitle">${data.comment}</span>
                <a href="${url_dell+data.id_comment}" class="delete_comment-link">
                    <img id="delete_comment" class="delete_comment" src="${imgUrl_no}" alt="delete_comment">
                </a
              </div>               
          </div>`
    }
    if (data.username == comment_realusername) { 
        window.scrollTo(0, document.body.scrollHeight);
    }
    
}




// при натисканні на кнопку відправляємо json за допомогою сокетів в social_network.consumers.py 
document.querySelector('#post-comment-submit').onclick = function (e) {
     // отримання даних з поля вводу
    
    const comment_input = document.querySelector('#comment_input');
    const comment = comment_input.value;
    
    socket.send(JSON.stringify({
        'comment': comment,
        'username': comment_username,
    }));

    // заміняємо значення введеного тексту на пустий рядок
    comment_input.value = '';
}