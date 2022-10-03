from django import forms
from django.forms import ModelForm

from aplicaciones.core.models import Pais
from aplicaciones.ficha_personal.models import Cargo,Departamento,Empleado,Sueldo,ContactoEmergencias,InfoAcademica,Capacitaciones

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Ingrese Cargo','required': True}),
        }

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Ingrese Departamento','required': True}),
        }

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Ingrese Nombre Completo'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Cédula'}),
            'fecha_nacimiento': forms.DateInput(format=('%d/%m/%Y'),
                                                attrs={'class': 'form-control', 'placeholder': 'Ingrese su Fecha de Nacimiento', 'type': 'date'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Ingrese Email'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Dirección'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Teléfono'}),
            'fecha_IESS': forms.DateInput(format=('%d/%m/%Y'),
                                                attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha','type': 'date'}),
            'tipo_Contrato': forms.Select(attrs={'class': 'form-control'}),
            'fecha_Ingreso': forms.DateInput(format=('%d/%m/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha','type': 'date'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
        }

        # def clean_cedula(self):
        #     try:
        #         sc = Empleado.object.get(
        #             ced = self.cleaned_data['cedula']
        #             )
        #         if not self.instance.pk:
        #             print('Ya existe Registro con esa cedula')
        #             raise forms.ValidationError("Ya existe empleado con esa cedula")
        #         elif self.instance.pk!= sc.pk:
        #             print("Ingreso no permitido")
        #             raise forms.ValidationError("Ingreso no permitido, cedula en uso")
        #     except Empleado.DoesNotExist:
        #         pass
        #     return self.cleaned_data['cedula']

        def clean_cedula(self):
            ced = self.cleaned_data['cedula']
            msg = "La Cédula introducida no es válida"
            valores = [int(ced[x]) * (2 - x % 2) for x in range(9)]
            suma = sum(map(lambda x: x > 9 and x - 9 or x, valores))
            veri = 10 - (suma - (10 * (suma / 10)))
            if int(ced[9]) == int(str(veri)[-1:]):
                return ced
            else:
                raise forms.ValidationError(msg)

        def clean_email(self):
            email = self.cleaned_data['email']
            if Empleado.objects.filter(email=email).exists():
                # elevar
                forms.ValidationError('El buzón ya existe')
            return email


class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

        widgets = {
           'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SueldoForm(ModelForm):
    class Meta:
        model = Sueldo
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(format=('%d/%m/%Y'),attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha inicial','type': 'date'}),
            'sueldo': forms.TextInput(attrs={'placeholder': 'xx,xx', 'value': '0'}),
        }

class ContactoEmergenciasForm(ModelForm):
    class Meta:
        model = ContactoEmergencias
        fields = '__all__'
        widgets = {
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Ingrese nombre'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su número de cédula'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control','placeholder':'Número celular'}),
            'parentesco': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Dirección'}),
        }

class InfoAcademicaForm(ModelForm):
    class Meta:
        model = InfoAcademica
        fields = '__all__'
        widgets = {
            'fecha_Inicio': forms.DateInput(format=('%d/%m/%Y'),attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha','type': 'date'}),
            'fecha_Fin': forms.DateInput(format=('%d/%m/%Y'),attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha','type': 'date'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su institución'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titulo obtenido'}),
        }

class CapacitacionesForm(ModelForm):
    class Meta:
        model = Capacitaciones
        fields = '__all__'
        widgets = {
            #'certificado': forms.FileField(),
            'fecha_Inicio': forms.DateInput(format=('%d/%m/%Y'),attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha inicial','type': 'date'}),
            'fecha_Fin': forms.DateInput(format=('%d/%m/%Y'),attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha final','type': 'date'}),
            'duracion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese cuanto tiempo duro su capacitacion'}),
        }

