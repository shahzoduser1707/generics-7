from django.urls import path
from .views import GetPhone,CreatePhone,GetCreatePhone,DetailUpdateDestroy


urlpatterns = [
    path('getPhone/',GetPhone.as_view()),
    path('createPhone/',CreatePhone.as_view()),
    path('getcreatePhone/',GetCreatePhone.as_view()),
    path('<int:pk>/',DetailUpdateDestroy.as_view())
]