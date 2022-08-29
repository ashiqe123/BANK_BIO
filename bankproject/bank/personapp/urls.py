from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('person/',views.person,name='person'),
    path('',views.home,name='home'),
    path('head/',views.page,name='page')
]