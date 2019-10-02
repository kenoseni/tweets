from django.urls import path

from . import views

urlpatterns = [
    path('', views.TipView.as_view(), name='python_tips'),
    path('<str:pk>', views.SingleTipView.as_view(), name='single_python_tip'),
    # path('search/<str:search_param>/', views.SearchResultsView.as_view(), name='search_python_tip'),
]
