from django.conf.urls import url,include
from . import views


urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/', views.about, name='about us'),
    url(r'^download/', views.generate_view, name='download'),
    # url(r'^newsletter/', views.newsletter, name='newsletter'),
    url(r'^news/', views.news, name='news'),

    url(r'^offer/', views.offer, name='offer'),
    url(r'^great/', views.great, name='great'),
    url(r'^touch/', views.touch, name='touch'),
    url(r'^cert/', views.cert, name='cert'),


    # url(r'^ajax/news/$', views.news, name='news'),



]



