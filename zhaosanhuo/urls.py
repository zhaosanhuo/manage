from django.urls import path
from zhaosanhuo.views import current_datetime, my_custom_page_not_found_view

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

handler404 = 'zhaosanhuo.views.my_custom_page_not_found_view'

urlpatterns = [
    path('1/', current_datetime ),
]