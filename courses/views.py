from django.shortcuts import render
from django.views.generic import ListView, DetailView,View
from .models import Course
from memberships.models import UserMemberShip, Membership, Subscription

class CourseListView(ListView):
    model = Course
    context_object_name = "courses"

class CourseDetailView(DetailView):
    model = Course

class LessonDetailView(View):
    def get(self,request, course_slug, lesson_slug, *args, **kwargs):
        course_qs = Course.objects.filter(slug=course_slug)
        if course_qs.exists():
            course=course_qs.first()
        lesson_qs = course.lessons.filter(slug=lesson_slug)
        if lesson_qs.exists():
                lesson=lesson_qs.first()
        user_membership = UserMemberShip.objects.filter(user=request.user).first()
        user_membership_type = user_membership.membership.membership_type
        course_allowed_membership_type = course.allowed_membership.all()
        context={
            'object':lesson,
            'course':course
        }
        if course_allowed_membership_type.filter(membership_type=user_membership).exists():
            context={
                'object':lesson
            }
        return render(request,'courses/lesson-detail.html', context)
        