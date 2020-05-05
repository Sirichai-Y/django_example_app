from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('province/', views.province),

    path('situation/', views.situation),

    path('comment/', views.comment),
    path('comment/manage/<int:cid>', views.manage_comment),

    path('message/', views.message),
    path('message/heart/<int:mid>', views.give_heart_message),
    path('message/manage/<int:mid>', views.manage_message),
    path('message/prov/<int:prov>', views.message_by_province),
    path('message/sit/<int:sit>', views.message_by_situation),
    path('message/sit/<int:sit>/prov/<int:prov>', views.message_by_situation_province)
]

urlpatterns = format_suffix_patterns(urlpatterns)
