from django.db import models
import re, bcrypt
# Create your models here.
class UserManager(models.Manager):
    def RegValidator(self, postData):
        errors = {}
        if len(User.objects.filter(email= postData['email']))>0:
            errors['existing_user'] = "Email already in use"
        if len(postData['first_name'])<2:
            errors['first_name_short'] = "Name must be a tleast 2 characters"
        if len(postData['first_name'])>24:
            errors['first_name_long'] = "Name must not exceed 24 characters"
        if len(postData['last_name'])<2:
            errors['last_name_short'] = "Name must be at least 2 charaters"
        if len(postData['last_name'])>24:
            errors['last_name_long'] = "Name must not exceed 24 characters"
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['email']):
            errors['invalid_email'] = "Invalid email address"
        if len(postData['email'])>36:
            errors['email_long'] = "Invalid Email"
        if len(postData['password'])<8:
            errors['password_short'] = "Password must be at least 8 characters"
        return errors
    def LoginValidator(self, postData):
        errors = {}
        check_email = User.objects.filter(email=postData['log_email'])
        if len(check_email)<1:
            errors['no_email'] = "Invalid email or password combination"
        elif not bcrypt.checkpw(postData['log_password'].encode(), check_email[0].password.encode()):
            errors['wrong_pw'] = "Invalid email or password combination"
        return errors 

class User(models.Model):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    email = models.CharField(max_length=36)
    password = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()