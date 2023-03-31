from django import forms
from .models import Productos, Comentario

class FormularioNuevoProducto(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('usuario', 'titulo', 'producto', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'emailContacto', 'imagenProducto')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'producto' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class ActualizarProducto(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('titulo', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'emailContacto', 'imagenProducto')

        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }



      #nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
      #precio = forms.IntegerField(label='Precio', widget=forms.NumberInput(attrs={'placeholder': 'Precio'}))
      #seccion = forms.CharField(label='Seccion', widget=forms.NumberInput(attrs={'placeholder': 'Seccion'})) 

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }