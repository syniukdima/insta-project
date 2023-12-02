// зберігаєм textarea що є на сторінці
var textarea = document.querySelector('textarea');

// якщо користувач вводить текст який не влазить в textarea, то поле розширюється
textarea.addEventListener('keyup', function () {
    if (this.scrollTop > 0) {
        this.style.height = this.scrollHeight + "px";
    }
});







