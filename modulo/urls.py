from django.urls import path
from . import views

urlpatterns = [
    path('<int:ord>', views.index_view, name='index'),
    path('descripcion/<int:id>', views.descripcion_view, name='descripcion'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create', views.create, name='create'),
    

]
