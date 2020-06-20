from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path('loginPage/', views.loginPage,name="loginPage"),
    path('profile/<int:pk>', views.profile,name="profile"),
    path('delete/<int:pk>', views.delete,name="delete"),
    path('deleteSubject/<int:pk>', views.deleteSubject,name="deleteSubject"),
    path('importFile', views.importFile,name="importFile"),
    path('search', views.search,name="search"),
    path('add', views.add,name="add"),
    path('upload_csv', views.upload_csv,name="upload_csv"),
    path('search_re', views.search_re,name="search_re"),

    ]