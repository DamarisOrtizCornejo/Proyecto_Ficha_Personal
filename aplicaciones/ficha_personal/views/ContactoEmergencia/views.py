from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.ficha_personal.forms import ContactoEmergenciasForm
from aplicaciones.ficha_personal.models import ContactoEmergencias

class ContactoEmergenciaListView(ListView):
    template_name = "ContactoEmergencia/listContactoEmergencia.html"
    context_object_name = 'contactoEmergencia'
    model = ContactoEmergencias
    paginate_by = 3
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(empleado__nombres=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/fichaPersonal/fichaPersonal'
        context['listar_url']= '/fichaPersonal/contactoEmergencia'
        context['crear_url'] = '/fichaPersonal/crearContactoEmergencias/'
        context['titulo'] = 'LISTADO DE CONTACTO EMERGENCIAS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class RegistroContactoEmergenciaListView(ListView):
    template_name = "ContactoEmergencia/registroContacto.html"
    model = ContactoEmergencias
    context_object_name = 'contactoEmergencias'
    paginate_by = 3
    # queryset = ContactoEmergencias.objects.filter(id=1)

    def get_queryset(self):
        # print("mira",type(self.kwargs['pk']),self.kwargs['pk'])
        return self.model.objects.filter(empleado__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/fichaPersonal/contactoEmergencia'
        context['listar_url']= '/fichaPersonal/registroContactoEmergencia'
        context['crear_url'] = '/fichaPersonal/crearContactoEmergencias/'
        context['titulo'] = 'REGISTRO DE CONTACTO EMERGENCIAS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearContactoEmergencia(CreateView):
    model = ContactoEmergencias
    template_name = "ContactoEmergencia/form.html"
    success_url = reverse_lazy('ficha_Personal:contactoEmergencia')
    form_class = ContactoEmergenciasForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/fichaPersonal/crearContactoEmergencias/'
        context['titulo'] = 'CREAR CONTACTO EMERGENCIA'
        context['url_anterior'] = '/fichaPersonal/contactoEmergencia'
        context['listar_url'] = '/fichaPersonal/contactoEmergencia'
        context['action'] = 'add'
        return context

class ActualizarContactoEmergencia(UpdateView):
    model = ContactoEmergencias
    template_name = "ContactoEmergencia/form.html"
    # success_url = reverse_lazy('ficha_Personal:registroContactoEmergencia')
    success_url = reverse_lazy('ficha_Personal:contactoEmergencia')
    form_class = ContactoEmergenciasForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DE CONTACTO EMERGENCIA'
        context['url_anterior'] = '/fichaPersonal/contactoEmergencia'
        context['listar_url'] = '/fichaPersonal/contactoEmergencia'
        return context


class EliminarContactoEmergencia(DeleteView):
    model = ContactoEmergencias
    template_name = "ContactoEmergencia/delete.html"
    success_url = reverse_lazy('ficha_Personal:contactoEmergencia')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE CONTACTO EMERGENCIA'
        context['url_anterior'] = '/fichaPersonal/contactoEmergencia'
        context['listar_url'] = '/fichaPersonal/contactoEmergencia'
        return context

