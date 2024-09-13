
# Question 1: Are Django signals executed synchronously or asynchronously by default?

# Django Signals are executed synchronously

# Example : # Pre Save : Modifies the User model before it is saved to the database.

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(pre_save, sender=User)
def user_save_bf(sender, instance, **kwargs):
    print("Before saving the user")
    print(instance.username)


# Example : # Post Save : After the model instance is saved to the database.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_save_af(sender, instance, **kwargs):
    print("After saving the user")
    print(instance.username)


# How to Create a new user

user=User.objects.create(username='Teacher1')

