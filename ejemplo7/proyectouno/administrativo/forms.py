from django.forms import ModelForm
from django import forms

from administrativo.models import Matricula, Modulo, Estudiante

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo']
        widgets = {
            'estudiante': forms.Select(attrs={
                'class': 'form-select',
            }),
            'modulo': forms.Select(attrs={
                'class': 'form-select',
            }),
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe aquí tu comentario...',
                'style': 'height: 120px'
            }),
            'costo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Costo'
            }),
        }
        labels = {
            'estudiante': 'Selecciona un estudiante',
            'modulo': 'Selecciona un módulo',
            'comentario': 'Comentario Adicional',
            'costo': 'Costo de la matrícula',
        }



class MatriculaEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MatriculaEditForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = self.instance.estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        self.initial['modulo'] = self.instance.modulo
        self.fields["modulo"].widget = forms.widgets.HiddenInput()

    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Escribe aquí tu comentario...'
            }),}

# NUEVOS FORMULARIOS
class ModuloForm(ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre']
        widgets = {
            'nombre': forms.Select(attrs={
                'class': 'form-select',
            })
        }
        labels = {
            'nombre': 'Nombre del Módulo',
        }

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Apellido'
            }),
            'cedula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cédula'
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad'
            }),
            'tipo_estudiante': forms.Select(attrs={
                'class': 'form-select',
            })
        }

        labels = {
            'nombre': 'Nombre Completo',
            'apellido': 'Apellido',
            'cedula': 'Cédula de Identidad',
            'edad': 'Edad',
            'tipo_estudiante': 'Tipo de Estudiante',
        }