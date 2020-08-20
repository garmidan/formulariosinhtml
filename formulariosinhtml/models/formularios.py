from django import forms
ciudades= [
    ('Seleccione','Seleccione'),
    ('Bogota', 'Bogotá'),
    ('Medellin', 'Medellin'),
    ('Ibague', 'Ibague'),
    ('Cali', 'Cali'),
    ('Cartagena', 'Cartagena'),
    ]

class FormularioRegistro(forms.Form):
    nombres = forms.CharField(required=True)
    apellidos = forms.CharField(required=True)
    cedula = forms.CharField(required=True)
    telefono = forms.CharField(required=True)
    correo = forms.EmailField(required=True)
    ciudad = forms.ChoiceField(choices=ciudades, required=True, label="Seleccione su ciudad")
