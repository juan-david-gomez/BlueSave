from django.views.generic import CreateView,TemplateView,ListView,UpdateView,DeleteView,DetailView,View,FormView
from django.template.response import TemplateResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .models import *
#----------------------- Generales ----------------------------------

class Home(TemplateView):
	template_name = 'dinero/index.html'


class Ingresar(FormView):
	template_name = "usuarios/login.html"
	success_url = '/'
	form_class = AuthenticationForm

	def post(self, request, *args, **kwargs):
	    form_class = self.get_form_class()
	    form = self.get_form(form_class)

	    if form.is_valid():
	    	nom = form.cleaned_data['username']
	    	clav = form.cleaned_data['password']
	    	print "Estoy valido"
	    	acceso = authenticate(username = nom, password = clav)
	    	if acceso is not None:
	    		print "Estoy accesado"
	    		if acceso.is_active:
	    			print "Estoy permitido"
	    			login(request,acceso)
	    			print "Estoy logeado"
	      			return self.form_valid(form)
	    else:
	        return self.form_invalid(form)

@login_required(login_url="/")
def Cerrar(request):
	logout(request)
	return HttpResponseRedirect("/")
	

class MostrarSaldo (View):

	def get(self, request, *args, **kwargs):

		for p in movimiento.objects.raw('SELECT * FROM dinero_movimiento where tipo_id = 1'):
 		 	self.entrada = self.entrada + p.valor
	 	for p in movimiento.objects.raw('SELECT * FROM dinero_movimiento where tipo_id = 2'):
	 		 	self.salida = self.salida + p.valor
	  	self.saldo = self.entrada - self.salida


		return TemplateResponse(request, self.get_template_name(),
                                self.get_context_data())


	def get_template_name(self):
		return "dinero/MostrarSaldo.html"

	entrada = 0
	salida = 0	

	


	def get_context_data(self):
		datos = {"saldo": self.saldo,}
		return datos
#----------------------- Movimientos ---------------------------------------
class RegistrarMovimiento (CreateView):
	template_name = "dinero/Movimientos/registrarMovimiento.html"
	model = movimiento
	success_url = "/ListarMovimiento" 

class ListarMovimiento (ListView):
	template_name = "dinero/Movimientos/ListarMovimiento.html"
	
	queryset = movimiento.objects.all()
	context_object_name = "movimientos"

class EditarMovimiento (UpdateView):
	template_name = "dinero/Movimientos/EditarMovimiento.html"
	model = movimiento
	success_url = "/ListarMovimiento" 

class BorrarMovimiento (DeleteView):
	template_name = "dinero/Movimientos/BorrarMovimiento.html"
	model = movimiento
	success_url = "/ListarMovimiento" 

#----------------------- Tpos ---------------------------------------

class RegistrarTipo (CreateView):
	template_name = "dinero/tipos/registrarTipo.html"
	model = tipo
	success_url = "/ListarTipo"

class ListarTipo (ListView):
	template_name = "dinero/Tipos/ListarTipo.html"
	#model = movimiento
	queryset = tipo.objects.all()
	context_object_name = "Tipos"

class EditarTipo (UpdateView):
	template_name = "dinero/Tipos/EditarTipo.html"
	model = tipo
	success_url = "/ListarTipo" 

class BorrarTipo (DeleteView):
	template_name = "dinero/Tipos/BorrarTipo.html"
	model = tipo
	success_url = "/ListarTipo" 

#----------------------- Categorias ---------------------------------------

class RegistrarCategoria (CreateView):
	template_name = "dinero/Categorias/registrarCategoria.html"
	model = categoria
	success_url = "/ListarCategoria"

class ListarCategoria (ListView):
	template_name = "dinero/Categorias/ListarCategoria.html"
	#model = movimiento
	queryset = categoria.objects.all()
	context_object_name = "Categorias"

class EditarCategoria (UpdateView):
	template_name = "dinero/Categorias/EditarCategoria.html"
	model = categoria
	success_url = "/ListarCategoria" 

class BorrarCategoria (DeleteView):
	template_name = "dinero/Categorias/BorrarCategoria.html"
	model = categoria
	success_url = "/ListarCategoria" 