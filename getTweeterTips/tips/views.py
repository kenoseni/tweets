"""Views for python tips tweets"""

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .models import Tip
from .filters import TipsSearchFilter
from .serializers import TipSerializer

# Create your views here.
class TipView(LoginRequiredMixin, ListCreateAPIView):
    """Class view to get, create and search all python tips"""
    filter_backends = (TipsSearchFilter,)
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

 
class SingleTipView(LoginRequiredMixin, RetrieveUpdateDestroyAPIView):
    """Class view to retrieve, update and destroy a single python tip"""
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
