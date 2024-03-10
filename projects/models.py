from django.db import models
import uuid
from django.utils.text import slugify
from accounts.models import CustomUser


# Create your models here.
class Projects(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length = 300)
    description = models.TextField()
    project_link = models.URLField(max_length = 300,null = True,blank =  True)
    image = models.ImageField(upload_to='projects/images')
    slug = models.CharField(max_length = 250,unique = True,blank=True)
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE,related_name = 'projects')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)+'-'+str(self.user.username)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)
