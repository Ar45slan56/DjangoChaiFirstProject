from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_home, name="all_home"),
    path('ChaiStore/', views.chai_store_view, name="chai_store"),
    path('<int:chai_id>/', views.chai_detail, name="chai_detail"),
]
