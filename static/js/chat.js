// отримую айді користувача якому пишуть
const id = JSON.parse(document.getElementById('json-username').textContent);
// отримую юзернейм користувача якиий пише повідомлення
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);

const avatar_user = JSON.parse(document.getElementById('json-avatar').textContent)

// створюю новий об'єкт вебсокету
const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + id
    + '/'
);

// відкрите
socket.onopen = function (e) {
    console.log("CONNECTION ESTABLISHED");
}

// закрите
socket.onclose = function (e) {
    console.log("CONNECTION LOST");
}

// помилки
socket.onerror = function (e) {
    console.log("ERROR OCCURED");
}

// відправка
socket.onmessage = function (e) {
    // отримуємо дату
    var currentdate = new Date();
    // створюємо шаблон за яким дата буде виводитися в потрібному нам вигляді
    var datetime =
        + ((currentdate.getHours()) < 10 ? "0" + currentdate.getHours() : currentdate.getHours()) + ":"
        + ((currentdate.getMinutes()) < 10 ? "0" + currentdate.getMinutes() : currentdate.getMinutes());

    var new_day_date = months[currentdate.getMonth()] + " " + currentdate.getDate()
   
    // отримуємо данні з chats.consumers.py
    const data = JSON.parse(e.data);

    // перевірка на тип повідомлення (текст або голосове)
    // 1 - голосове
    // 0 - текст
    if (data.base64 === "1") {
        if (data.new_day){
            document.querySelector('#chat').innerHTML += `<div class="data_up"><span class="data_up-text">${new_day_date}</span></div>`
        }
        // перевірка на користувача який відправляє повідомлення
        if (data.username == message_username) {
            // виводить повідомлення справа, оскільки користувач відправив його
            document.querySelector('#chat').innerHTML += `<div class="right for_audio">
            <audio controls="controls" autobuffer="autobuffer" class="my_audio">
              <source src="data:audio/wav;base64, ${data.message}" />
            </audio> 
            <span class="time_message">${datetime}</span>
          </div>`
            scrollToDown("chat");

        } else {
            // виводить повідомлення зліва, оскільки користувач отримав повідомлення
            document.querySelector('#chat').innerHTML += `<div class="left ">
            <audio controls="controls" autobuffer="autobuffer" class="my_audio">
              <source src="data:audio/wav;base64, ${data.message}" />
            </audio> 
            <span class="time_message">${datetime}</span>
          </div>`
        }
    }
    else {
        // перевірка на пустий рядок
        if (data.message != "") {
            if (data.new_day){
                document.querySelector('#chat').innerHTML += `<div class="data_up"><span class="data_up-text">${new_day_date}</span></div>`
            }
            // перевірка на користувача який відправляє повідомлення
            if (data.username == message_username) {
                // виводить повідомлення справа, оскільки користувач відправив його
                document.querySelector('#chat').innerHTML += `<div class="chat_message right">
            <span class="chat_message-text">${data.message}</span>
            <span class="time_message">${datetime}</span>
        </div>`
                scrollToDown("chat");
            } else {
                
                // виводить повідомлення зліва, оскільки користувач отримав повідомлення
                document.querySelector('#chat').innerHTML += `<div class="chat_message">
            <img class="title_chat_avatar" src="${avatar_user}" alt="avatar">
            <span class="chat_message-text">${data.message}</span>
            <span class="time_message">${datetime}</span>
        </div>`
            }
        }
    }
}

// спрацьовує при натисненні на кнопку відправити повідомлення (текстове)
// відправляє повідомленяя в json для обробки в chats.consumers.py за допомогою сокетів
document.querySelector('#chat-message-submit').onclick = function (e) {
    // отримання даних з поля вводу
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;

    socket.send(JSON.stringify({
        'message': message,
        'username': message_username,
        'base64': "0"
    }));

    // заміняємо значення введеного тексту на пустий рядок
    message_input.value = '';
}

// запис голосового повідомлення
jQuery(document).ready(function () {
    var $ = jQuery;
    var myRecorder = {
        objects: {
            context: null,
            stream: null,
            recorder: null
        },
        // функція ініціалізації
        init: function () {
            if (null === myRecorder.objects.context) {
                myRecorder.objects.context = new (
                    window.AudioContext || window.webkitAudioContext
                );
            }
        },
        // почати запис
        start: function () {
            // вибираємо тільки аудіо
            var options = { audio: true, video: false };
            navigator.mediaDevices.getUserMedia(options).then(function (stream) {
                myRecorder.objects.stream = stream;
                myRecorder.objects.recorder = new Recorder(
                    myRecorder.objects.context.createMediaStreamSource(stream),
                    { numChannels: 1 }
                );
                myRecorder.objects.recorder.record();
            }).catch(function (err) { });
        },
        // зупинка запису
        stop: function (listObject) {
            if (null !== myRecorder.objects.stream) {
                // зупиняємо запис
                myRecorder.objects.stream.getAudioTracks()[0].stop();
            }
            if (null !== myRecorder.objects.recorder) {
                // зупиняємо запис
                myRecorder.objects.recorder.stop();

                // Перевірте об'єкт
                if (null !== listObject
                    && 'object' === typeof listObject
                    && listObject.length > 0) {

                    // передаємо blob файл з голосовим в json для подальшої обробки в c
                    myRecorder.objects.recorder.exportWAV(function (blob) {

                        var reader = new window.FileReader();
                        reader.readAsDataURL(blob);
                        // перетворюємо blob файл в base64 
                        reader.onloadend = function () {
                            base64 = reader.result;
                            base64 = base64.split(',')[1];


                            socket.send(JSON.stringify({
                                'message': base64,
                                'username': message_username,
                                'base64': "1",
                            }));

                        }
                    });
                }
            }
        }
    };

    // Підготуйте список записів
    var listObject = $('[data-role="recordings"]');

    // Підготуйте кнопку запису
    $('[data-role="controls"] > button').click(function () {
        // Ініціалізуйте рекордер
        myRecorder.init();

        // Отримати стан кнопки
        var buttonState = !!$(this).attr('data-recording');

        // Перемикач
        if (!buttonState) {
            $(this).attr('data-recording', 'true');
            myRecorder.start();
        } else {
            $(this).attr('data-recording', '');
            myRecorder.stop(listObject);
            scrollToDown("chat");
        }
    });
});

function scrollToDown(idElement) {
    const element = document.getElementById(idElement);
    const h = element.scrollHeight;
    element.scrollTo({
        top: h,
        left: 0,
        behavior: 'smooth'
      });
}

const months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
  ]

var chat = document.getElementById('chat');
chat.scrollTop = chat.scrollHeight;
