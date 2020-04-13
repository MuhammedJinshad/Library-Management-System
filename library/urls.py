from django.urls import path
from .import views


urlpatterns = [

    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('addstudent/',views.addstudent, name='addstudent'),
    path('profile_view/',views.profile_view, name='profile_view'),
    path('view_books/',views.view_books, name='view_books'),
    path('issuebook/',views.issuebook, name='issuebook'),
    path('returnbook/',views.returnbook, name='returnbook'),
    path('mybooks/',views.mybooks,  name='mybooks'),
    path('myhistory/',views.myhistory, name='myhistory'),
    path('updateprofile/',views.updateprofile, name='updateprofile'),
    path('allhistorys/',views.allhistorys, name='allhistorys'),
    path('answer_me/', views.answer_me, name='get_response'),
    path('selected_book_stock/',views.selected_book_stock, name='selected_book_stock'),

  

]