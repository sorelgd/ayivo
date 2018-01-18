from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profiluser$', views.profiluser, name='profiluser'),
    url(r'^credits/$', views.credits, name='credits'),
    url(r'^datas/$', views.datas, name='datas'),
    url(r'^moneys/$', views.moneys, name='moneys'),
    url(r'^profiluser/contactsuser/$', views.contactsuser, name='contactsuser'),
    url(r'^profiluser/historiquesuser/$', views.historiquesuser, name='historiquesuser'),
    url(r'^profiluser/infospersonel/$', views.infospersonel, name='infospersonel'),
    url(r'^profiluser/faireunachat/$', views.faireunachat, name='faireunachat'),
   # url(r'^sign_in/$', views.sign_in, name='sign_in'),
    #url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
    #url(r'^pays$', views.test, name='test'),

]