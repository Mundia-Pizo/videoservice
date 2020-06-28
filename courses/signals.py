from django.utils.text import slugify
from .models import Course
from django.db.models.signals import pre_save


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug=new_slug
	qs =Course.objects.filter(slug=slug).order_by('-id')
	exists=qs.exists()
	if exists:
		new_slug="%s-%s"%(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def course_receiver(sender, instance,*args, **kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)
 

pre_save.connect(course_receiver, sender=Course)