/*const carousel = document.querySelector(".myCarousel");
let isDragging = false, startX, startScrollLeft;

const dragStop = () => {
    isDragging = false;
    carousel.classList.remove("dragging")
}
const dragStart = () => {
    isDragging = True;
    carousel.classList.add("dragging");
    startX = e.pageX;
    startScrollLeft = carousel.scrollLeft;
}
const dragging = (e) => {
    if(!isDragging) return; //Si isDragging = False, regresa a este punto
    carousel.scrollLeft = startScrollLeft -  (e.pageX - startX ); 
}
/*carousel.addEventListener("mousedown", dragStart);
carousel.addEventListener("mouseup", dragging);
document.addEventListener("mouseup", dragStop);*/

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function notifAction() {
    document.getElementById("notification-content").classList.toggle("notification-show");
    if (document.getElementById("noti-count") !== null) {
      document.getElementById("noti-count").classList.add("noti-none")
    }
    
  }

  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.notification-btn')) {
      var dropdowns = document.getElementsByClassName("notification-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('notification-show')) {
          openDropdown.classList.remove('notification-show');
        }
      }
    }
  };

  // Agregar un evento de clic al botón
  document.getElementById("noti-btn").addEventListener("click", function() {
    // Crear una instancia de XMLHttpRequest
    var xhr = new XMLHttpRequest();
    
    // Configurar la solicitud AJAX
    xhr.open("GET", "/marcar_notificaciones_vistas/", true);  // Reemplaza "/mi-url/" con la URL de tu vista en Django
    
    // Manejar la respuesta de la solicitud AJAX
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        // La solicitud se ha completado y se ha recibido una respuesta válida
        console.log(xhr.responseText);  // Puedes realizar acciones adicionales con la respuesta aquí
      }
    };
    
    // Enviar la solicitud AJAX
    xhr.send();
  });
  
  
  