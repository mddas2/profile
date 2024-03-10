from django.db import models
from accounts.models import CustomUser
from experience.models import ProfessionCategory,Skills,Experience

# Create your models here.

class Employer(models.Model):
    cv = models.FileField(upload_to='users/employer',null=True)
    user = models.OneToOneField(CustomUser,related_name = 'employer',on_delete = models.CASCADE)
    expected_salary = models.PositiveIntegerField()
    profession_category = models.ForeignKey(ProfessionCategory,related_name = 'employer',on_delete = models.PROTECT)
    skills = models.ManyToManyField(Skills,through="EmployerHaveSkills",related_name='employers')

    def __str__(self) -> str:
        return self.user.username

class EmployerHaveSkills(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField()  # in years


# {
#     "cv": "path/to/cv.pdf",
#     "user": 1,  // Assuming the user ID to whom this employer belongs
#     "expected_salary": 50000,
#     "job_category": 1,  // Assuming the job category ID
#     "skills": [  // Assuming skills are specified as a list of skill IDs
#         {"skill": 1, "experience": 2},  // Skill ID and experience in years
#         {"skill": 2, "experience": 3}
#     ]
# }
