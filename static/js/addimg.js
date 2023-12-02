// додає до посту до п'яти фотографій
document.querySelector("#file").addEventListener("change", (e) => { 
    if (window.File && window.FileReader && window.FileList && window.Blob) { 
      // отримання файлів
      const files = e.target.files;   
      // проходження файлами
      for (let i = 0; i < files.length; i++) { 
        var error = document.getElementById("error");
        // якщо вибрано більше 5 фотографій
          if (files.length >= 5) {
            setTimeout(() => {
              error.style.display = "none";
            }, "5000")
            // виводить на 5 секунд повідомлення про помилку
            error.textContent = "Будь ласка, додайте до 4 фотографій."
            error.style.display = "flex";
            continue;
          }
          // якщо тип файлу не фотографія
          else if (!files[i].type.match("image")){
            setTimeout(() => {
              error.style.display = "none";
            }, "5000")
            // виводить на 5 секунд повідомлення про помилку
            error.textContent = "Підтримуються лише файли типу png, jpeg або jpg."
            error.style.display = "flex";
            continue;
          }
          
          //отримання url фотографій
          const picReader = new FileReader(); 

          // видаляє всі завантаженні фотографії в елемент contentBox
          var element = document.getElementById("contentBox");
          while (element.firstChild) {
            element.removeChild(element.firstChild);
          }

          // створення доданих фотографій
          picReader.addEventListener("load", function (event) { 
  
            var img = document.createElement("img");
            var src = document.getElementById("contentBox");
            const picFile = event.target;

            // отримання потрібного url для фотографії
            img.src = picFile.result

            img.classList.add("col-6");
            // додавання елементу до contentBox
            src.appendChild(img);
          });
          // причитати url
          picReader.readAsDataURL(files[i]); 
      }
    } else {
      // браузер не підтримує дану функцію
      alert("Your browser does not support File API");
    }
  });