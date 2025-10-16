from django.urls import path
from snippets import views

urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),

    # path('snippets/', views.snippet_list_apiview),
    # path('snippets/<int:pk>/', views.snippet_detail_apiview),

    path('snippets/', views.SnippetList_apiviewclass.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail_apiviewclass.as_view()),

]