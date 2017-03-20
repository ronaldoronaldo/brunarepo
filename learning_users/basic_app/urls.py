from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^opcoes/$',views.opcoes,name='opcoes'),
    url(r'^aba_registrado/$',views.aba_registrado,name='aba_registrado'),
    url(r'^fotos_cafe/$',views.fotos_cafe,name='fotos_cafe'),
]
