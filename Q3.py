# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    raise Exception("Signal caused an exception")

# In some view or shell
try:
    with transaction.atomic():
        MyModel.objects.create(name="test")
except Exception as e:
    print(f"Transaction failed: {e}")

# Verify if the record was created
print(MyModel.objects.count())
