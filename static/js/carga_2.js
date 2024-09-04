$('#submit-form').click(function(event) {
   event.preventDefault();
   var nombre = $("#nombre").val();

   $.ajax({
     url: 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='+nombre,
     data: {
        format: 'json'
     },
     error: function() {
        $('#info').html('<p>Un error ha ocurrido!!!!</p>');
     },
     dataType: 'json',
     success: function(data) {
        console.log(data);
        var $nombre_coctel = $('<h1>').text(data.drinks[0].strDrink);
        var $id = $('<p>').text(data.drinks[0].idDrink);
        var $instru = $('<p>').text(data.drinks[0].strInstructions);
        var $imagen = $("<img>").attr("src", data.drinks[0].strDrinkThumb);
        
        $("#info").empty();
        $('#info')
           .append($nombre_coctel)
           .append($id)
           .append($instru)
           .append($imagen)
           

     },
     type: 'GET'
  });
});



