

# Question 2: Do Django signals run in the same thread as the caller?

# The signal and the original action (Saving a user) happen together in sequence. It is Possible.

# Example : Signal & Saving a user in same time.

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_pass(sender, instance, **kwargs):
    print(f"Signal is running : {threading.current_thread().name}")


print(f"Caller : {threading.current_thread().name}")
user=User.objects.create(username="Teacher1")


