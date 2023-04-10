from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser



PROFESSION = (
    ('Cleaner', 'Cleaner'),
    ('Secetary', 'Secetary'),
    ('Engineer', 'Engineer'),
    ('Principal', 'Principal'),
    ('Vice-Principal', 'Vice-Principal'),
    ('Board of Regents', 'Board of Regents'),
    ('ICT Specialist', 'ICT Specialist'),
)
SUBJECTS = (
    ('Mathematics', 'Mathematics'),
    ('English', 'English'),
    ('Chemistry', 'Chemistry'),
    ('Social Science', 'Social Science'),
    ('Agriculture', 'Agriculture'),
    ('Physics', 'Physics'),
    ('Biology', 'Biology'),
    ('Futher Mathematics', 'Futher Mathematics'),
    ('Phonetics', 'Phonetics'),
    ('Commerce', 'Commerce'),
    ('Geography', 'Geography'),
    ('Economics', 'Economics'),
    ('Computer Programming', 'Computer Programming'),
    ('ICT Services', 'ICT Services'),
    ('Electronics', 'Electronics'),
    ('Data Processing', 'Data Processing'),
    ('Yoruba', 'Yoruba'),
    ('Hausa', 'Hausa'),
    ('Igbo', 'Igbo'),
    ('Technical Drawing', 'Technical Drawing')
)
LEVEL_OF_EXPERTISE = (
    ('1', 'Novice'),
    ('2', 'Amateur'),
    ('3', 'Regular'),
    ('4', 'Professional'),
    ('5', 'Skilled'),
    ('6', 'Expertrate'),
    ('7', 'Masters')
)
LEVEL = (
    ('1', 'Year 6'),
    ('2', 'Year 7'),
    ('3', 'Year 8'),
    ('4', 'Year 9'),
    ('5', 'Year 10'),
    ('6', 'Year 11'),
    ('7', 'Year 12')
)
ACADEMIC_LEVEL = (
    ('1', 'Rank 1'),
    ('2', 'Rank 2'),
    ('3', 'Rank 3'),
    ('4', 'Rank 4'),
    ('5', 'Rank 5')
)
# Create your models here.
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    is_admin=models.BooleanField('Is Admin',default=False)
    is_customer=models.BooleanField('Is Customer',default=True)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
        
class Management(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25, unique=True)
    profession = models.CharField(choices=PROFESSION, max_length=100)
    organization = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    date_of_employment = models.DateField(max_length=20, null=True)
    # lecturers = models.ForeignKey("Lecturers", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
class Lecturers(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    subjects_taught = models.CharField(choices=SUBJECTS, max_length=200)
    salary = models.IntegerField(max_length=200)
    level_of_expertise = models.CharField(choices=LEVEL_OF_EXPERTISE, max_length=1)
    years_of_experience = models.IntegerField()
    # Management = models.ManyToManyField(Management, related_name='lecturers', through='Students')
    
    def mail(self):
        return self.email
    
    def subjects(self):
        return self.subjects_taught
    
    def salary(self):
        return self.salary
    
    def loe(self):
        return self.level_of_expertise
    
    def __str__(self):
        return self.name
    
    
class Students(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    # management = models.ForeignKey(Management, on_delete=models.CASCADE)
    Lecturers = models.ForeignKey(Lecturers, on_delete=models.CASCADE, null=True)
    # subjects_offered = models.ManyToManyFields()
    year_level = models.CharField(choices=LEVEL, max_length=1)
    # organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    academic_level = models.CharField(choices=ACADEMIC_LEVEL, max_length=1)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class UserAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email

def post_user_created(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created, sender=User)   
    
