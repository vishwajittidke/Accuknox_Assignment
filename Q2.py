# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")

# In some view or shell
import threading
print(f"Main thread: {threading.current_thread().name}")
my_instance = MyModel.objects.create(name="test")
