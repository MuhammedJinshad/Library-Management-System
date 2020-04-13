from django.urls import path
from .import views


from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns     =   [
    path('bookapi/',views.BookList.as_view()),
    path('bookapi/<int:id>/',views.BookList.as_view()),
    path('bookpage/',views.BookPage.as_view()),

    path('cususerapi/',views.CususerList.as_view()),
    path('cususerapi/<int:id>',views.CususerList.as_view()),

    path('issuedbooksapi/',views.IssuedbookList.as_view()),
    path('issuedbooksapi/<int:id>/',views.IssuedbookList.as_view())
]