from django.db import models
import uuid
from django.utils.text import slugify
from accounts.models import CustomUser

# Create your models here.

class Blogs(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length = 300)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/images')
    slug = models.CharField(max_length = 250,unique = True,blank=True)
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE,related_name = 'blogs')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)+'-'+str(self.user.username)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)
