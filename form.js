document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto

        // Mostrar un mensaje de confirmación
        alert('El registro fue exitoso');

        // Limpiar los campos del formulario
        form.reset();

        // Redirigir a la página de inicio de sesión
        window.location.href = "login.html";
    });
});
