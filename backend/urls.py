from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('province/', views.province),
    path('situation/', views.situation),
    path('message/', views.message),
    path('message/prov/<int:prov>', views.message_by_province),
    path('message/sit/<int:sit>', views.message_by_situation),
    path('message/sit/<int:sit>/prov/<int:prov>', views.message_by_situation_province)
]

urlpatterns = format_suffix_patterns(urlpatterns)
