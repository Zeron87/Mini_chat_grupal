from django.urls import path
from .views import (MessageListApiView, MessageCreateApiView, 
                    MessageDestroyApiView)


app_name = 'message_app'

urlpatterns = [
    path('api/messages/list/', MessageListApiView.as_view()),
    path('api/messages/create/', MessageCreateApiView.as_view()),
    path('api/messages/delete/<int:pk>/', MessageDestroyApiView.as_view()),

]