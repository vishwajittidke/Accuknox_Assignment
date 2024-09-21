# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal started processing")
    time.sleep(5)  # Simulating a long-running task
    print("Signal finished processing")

# In some view or shell
my_instance = MyModel.objects.create(name="test")
print("Model instance created")
