from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from .roles import roles_data,roles_data_dict
from .import roles
import uuid
from tenant.models import Domain

class CustomUser(AbstractUser):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    phone = models.CharField(max_length=15 ,unique=True,null=True , default = '')
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255,unique=True)  
    country = models.CharField(max_length=255,default = '')  
    last_name = models.CharField(max_length=255,null = True,default = '')  
    dob = models.DateField(null= True,blank= True ) 

    is_active = models.BooleanField(default=True)
    remarks = models.CharField(max_length=200,null=True,default = '')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
 
    image = models.ImageField(upload_to="profiles/images",default=None,null=True,blank=True)
    role = models.PositiveSmallIntegerField(choices=roles_data, blank=True, null=True)

    system_provider = 1
    google_provider = 2
    facebook_provider = 3

    old_password_change_case = models.BooleanField(default=True) 

    provider_CHOICES = (
        (system_provider, 'system'),
        (google_provider, 'google'),
        (facebook_provider, 'facebook'), 
    )
    provider = models.PositiveSmallIntegerField(choices=provider_CHOICES,default = system_provider)
    # tenant = models.ForeignKey(Domain, related_name="users",on_delete=models.DO_NOTHING,default=None,blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def getRoleName(self):
        if self.role==roles.SUPER_ADMIN:
            return roles_data_dict[roles.SUPER_ADMIN]
        elif self.role == roles.ADMIN:
            return roles_data_dict[roles.ADMIN]
        elif self.role == roles.EMPLOYER:
            return roles_data_dict[roles.SUPER_ADMIN]
        elif self.role == roles.ENTREPRENEUR:
            return roles_data_dict[roles.ENTREPRENEUR]
        else:
            return None
        
    def __str__(self):
        return self.username + " "+ str(self.getRoleName())
    
    def full_name(self):
        try:
            return self.first_name + " " + self.last_name
        except:
            return self.username


