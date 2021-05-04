from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from rest_framework.generics import (GenericAPIView, ListAPIView, CreateAPIView)
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from .models import Message
#from .forms import MessageForm

from .serializers import (MessageSerializer, MessageListSerializer)

class MessageListApiView(ListAPIView):
    serializer_class = MessageListSerializer
    def get_queryset(self):
        return Message.objects.all()


class MessageCreateApiView(CreateAPIView, CreateModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def post(self, request, *args, **kwargs):
        print(request.POST)
        return self.create(request, *args, **kwargs)

class MessageDestroyApiView(GenericAPIView, DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def delete(self, request, *args, **kwargs):
        print(request.POST)
        return self.destroy(request, *args, **kwargs)

# class MessageCreateView(LoginRequiredMixin, CreateView):

#     model = Message
#     form_class = MessageForm
#     success_url = reverse_lazy('home_app:panel')

#     def form_valid(self, form):
#         message = form.save(commit=False)
#         message.success(self.request, "Message Ok")
#         return super(MessageCreateView, self).form_valid(form)