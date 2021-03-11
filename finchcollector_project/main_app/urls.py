from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('accounts/signup/', views.signup, name='signup'),
    path('finches/', views.finches_index, name="finches"),
    path('finches/new', views.finches_new, name="new"),
    path('finches/<int:finch_id>/delete/', views.finches_delete, name="delete"),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]
