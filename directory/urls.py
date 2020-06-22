from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('registerPage', views.registerPage,name="registerPage"),
    path('registeradmin', views.registeradmin,name="registeradmin"),
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
    path('bulk_upload', views.bulk_upload,name="bulk_upload"),
    path('upload_csv_bulk', views.upload_csv_bulk,name="upload_csv_bulk"),
    path('row_wise', views.row_wise,name="row_wise"),
    # path('bilk_search_re', views.bilk_search_re,name="bilk_search_re"),
    path('bulk_profile/<int:pk>', views.bulk_profile,name="bulk_profile"),
    path('bulk_delete/<int:pk>', views.bulk_delete,name="bulk_delete"),

    ]