from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
#-------------------- Generales -------------------------------------
 	url(r'^$',login_required(Home.as_view() ,login_url='/Ingresar'), name='inicio'),
	url(r'^MostrarSaldo/$',login_required(MostrarSaldo.as_view() ,login_url='/Ingresar'), name='MosSaldo'),
	url(r'^Ingresar/$',Ingresar.as_view() , name='login'),
	url(r'^Cerrar/$',Cerrar , name='Cerrar'),
#-------------------- Movimientos -------------------------------------
 	
	url(r'^RegistrarMovimiento$',login_required(RegistrarMovimiento.as_view() ,login_url='/Ingresar'), name='addmov'),
	url(r'^ListarMovimiento$',login_required(ListarMovimiento.as_view() ,login_url='/Ingresar'), name='Listmov'), 	
	url(r'^EditarMovimiento/(?P<pk>\d+)$',login_required(EditarMovimiento.as_view() ,login_url='/Ingresar'), name='Editmov'),
	url(r'^BorrarMovimiento/(?P<pk>\d+)$',login_required(BorrarMovimiento.as_view() ,login_url='/Ingresar'), name='delmov'),

#-------------------- Tipos -------------------------------------

	url(r'^RegistrarTipo$',login_required(RegistrarTipo.as_view() ,login_url='/Ingresar'), name='addtip'),
	url(r'^ListarTipo$',login_required(ListarTipo.as_view() ,login_url='/Ingresar'), name='Listtip'), 	
	url(r'^EditarTipo/(?P<pk>\d+)$',login_required(EditarTipo.as_view() ,login_url='/Ingresar'), name='Edittip'),
	url(r'^BorrarTipo/(?P<pk>\d+)$',login_required(BorrarTipo.as_view(),login_url='/Ingresar') , name='deltip'),

#-------------------- Categorias -------------------------------------

	url(r'^RegistrarCategoria$',login_required(RegistrarCategoria.as_view() ,login_url='/Ingresar'), name='addcat'),
	url(r'^ListarCategoria$',login_required(ListarCategoria.as_view() ,login_url='/Ingresar'), name='Listcat'), 	
	url(r'^EditarCategoria/(?P<pk>\d+)$',login_required(EditarCategoria.as_view() ,login_url='/Ingresar'), name='Editcat'),
	url(r'^BorrarCategoria/(?P<pk>\d+)$',login_required(BorrarCategoria.as_view() ,login_url='/Ingresar'), name='delcat'),
)
