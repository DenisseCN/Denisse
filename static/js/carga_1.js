$("#btn-cargar").click(function (event) {
    event.preventDefault();
  
    var url = "https://www.thecocktaildb.com/api/json/v1/1/random.php";
  
  
      fetch(url)
          .then(response => response.json())
          .then(data => 
              {
                var $nombre_cocktail = $('<h1>').text(data.drinks[0].strDrink);
                var $id = $('<p>').text(data.drinks[0].idDrink);
                var $foto_cocktail = $("<p><img src='"+ data.drinks[0].strDrinkThumb+"'>");
  
  
                  // para limpiar el contedor antes de desplegar
                  $("#info").empty();
                  $('#info')
                      .append($nombre_cocktail)
                      .append($id)
                      .append($foto_cocktail)
              })
          .catch(error => console.error(error));
  
  });
