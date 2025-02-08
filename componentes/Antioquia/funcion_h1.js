document.addEventListener('DOMContentLoaded', function() {
    // Obtenemos todos los elementos con la clase 'menu-link'
    var menuLinks = document.querySelectorAll('.menu-link');
    
    // Iteramos sobre cada elemento y le agregamos un event listener para el clic
    menuLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            // Obtenemos la URL de la página a la que queremos redirigir
            var url = obtenerURLSegunTitulo(link.innerText);
            
            // Redirigimos a la nueva página
            window.location.href = url;
        });
    });
    
    // Función para obtener la URL según el título del enlace
    function obtenerURLSegunTitulo(titulo) {
        // Define las URLs para cada título aquí
        // Por ejemplo:
        switch (titulo) {
            case 'Lugares Turisticos':
                return 'lugares_turisticos.html';
            case 'Festivales y Fiestas':
                return 'Fiesta_Festivales_Antioquia.html';
            case 'Deportistas':
                return 'deportistas_Atioquia.html';
            case 'Artistas':
                return 'artistas_Atioquia.html';
            default:
                return ''; // URL de fallback si no se encuentra ninguna coincidencia
        }
    }
});
