from django.urls import path
from .views import (
    CourseView,
    CourseListView
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='cources-list'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail')
]