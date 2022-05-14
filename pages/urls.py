from django.urls import path

from . import views

# app_name differentiates between apps that might be clustered together on this page
app_name = 'pages'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# Converting to use generic views or a templating system

urlpatterns = [
    path('', views.index, name='index'),
]
