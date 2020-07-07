from django.db import models
from django.urls import reverse
from memberships.models import Membership

class Course(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail   = models.ImageField(upload_to='course-images')
    slug        = models.SlugField()
    allowed_membership = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-details', kwargs={
            'slug':self.course.slug,
        })

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('-date')

class Lesson(models.Model):
    course      = models.ForeignKey(Course, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail   = models.ImageField(upload_to='lesson-images')
    date        = models.DateTimeField(auto_now_add=True)
    slug        = models.SlugField()
    video_url   = models.FileField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-details', kwargs={
            'course_slug':self.course.slug,
            "lesson_slug":self.slug
        })

