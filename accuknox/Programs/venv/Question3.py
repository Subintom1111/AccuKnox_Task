

# Question 3: Do Django signals run in the same database transaction as the caller?

# Django signals do not automatically run in the same database transaction .We Can Control the Signal is exected in relation.

# User is save to database but signal is pass after the transaction is Completed.

# Example

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created(sender, instance, **kwargs):
    print("Signal : User saved.")

def user_create():
    user=User(username="Teacher1")
    user.save()

    transaction.on_commit(print("Transaction Completed"))

