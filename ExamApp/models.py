from django.db import models
from LogRegApp.models import User

# Create your models here.
class QuoteManager(models.Manager):
    def QuoteValidator(self, postData):
        errors={}
        if len(postData['author'])<3:
            errors['authorShort'] = "Author must exceed 3 characters"
        if len(postData['quote_desc'])<10:
            errors['quoteShort'] = "Quote must exceed 10 characters"
        return errors

class Quote(models.Model):
    quote_user = models.ForeignKey(User, related_name='quotes', on_delete=models.CASCADE)
    quote_desc = models.TextField()
    author = models.CharField(max_length=24)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()