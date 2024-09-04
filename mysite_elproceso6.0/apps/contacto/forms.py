from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=200, required=True)
    email = forms.EmailField(label='Correo electrónico', max_length=200, required=True)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea, required=True)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('Este campo es obligatorio.')
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Este campo es obligatorio.')
        return email

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        if not mensaje:
            raise forms.ValidationError('Este campo es obligatorio.')
        return mensaje
