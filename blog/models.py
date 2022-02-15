from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


@receiver(post_save)
def create_post(sender,instance,created,**kwargs): 
    if created:   
        print("Post created")
        print(instance.title)
        print(instance.content)
    else :
        old = Post.objects.get(id=instance.id)
        print("This is The Old")
        print(old.title)
        print(old.content)
        print("This is the New")
        print(instance.title)
        print(instance.content)


# pre_save.connect(create_post,sender=Post)


