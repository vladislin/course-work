from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('schools', views.SchoolsListView.as_view(), name='schools'),
    path('school/<int:pk>/', views.SchoolDetailView.as_view(), name='school-details'),
    path('school/add', views.SchoolCreateView.as_view(), name='school-add'),
    path('universities', views.UniversityListView.as_view(), name='universities'),
    path('university/<int:pk>/', views.UniversityDetailView.as_view(), name='university-details'),
    path('university/add', views.UniversityCreateView.as_view(), name='university-add'),
]