from django.urls import path
from .views import CourseListView, CourseDetailView, LessonDetailView

urlpatterns=[
    path('', CourseListView.as_view(), name='courses'),
    path('<slug>/', CourseDetailView.as_view(), name='course-details'),
    path('<course_slug>/<lesson_slug>/', LessonDetailView.as_view(), name='lesson-details')
]