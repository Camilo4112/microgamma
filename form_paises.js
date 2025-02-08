// Hacer una solicitud GET a la API para obtener la lista de países
fetch('https://restcountries.com/v3.1/all')
  .then(response => {
    // Verificar si la respuesta es exitosa (código de estado 200)
    if (!response.ok) {
      throw new Error('Error al obtener la lista de países');
    }
    // Convertir la respuesta a formato JSON
    return response.json();
  })
  .then(data => {
    // Aquí tienes acceso a los datos de los países
    console.log(data);

    // Puedes procesar los datos como desees, por ejemplo:
    data.forEach(country => {
      console.log(country.name.common);
    });
  })
  .catch(error => {
    console.error('Error al obtener la lista de países:', error);
  });
