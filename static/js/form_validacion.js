$(document).ready(function() {
    $("#contact-form").validate({
      rules: {
        name : {
          required: true,
          minlength: 3
        },
        email: {
          required: true,
          email: true
        },
        fruit: {
            required: true,
        },
        instrument: {
            required: true,
        },
        cmbEdades:{
            required: true,
            number: true,
        },
        subjet: {
            required: true,
            minlength: 3
        },
        message: {
            required: true,
            minlength: 3
        }
      },
      messages : {
        name: {
          minlength: "Name should be at least 3 characters"
        },
        email: {
            email: "Debe tener sintaxis de email"
        },
        fruit: {
          required: "Por favor seleciona una fruta",

        },
        instrument: {
            required: "Ingresa el instrumento",
        },
        cmbEdades:{
            required: "Debe seleccionar edad",
            number: true,
        },
        subjet: {
            required: "Ingrese titulo mensaje",
            minlength: "Largo min 3 caracteres"
        },
        message: {
            required: "Ingrese texto del mensaje",
            minlength: "Largo min 3 caracteres"
        }
      }
    });
  });