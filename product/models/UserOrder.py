from django.contrib.auth.models import User
from django.db import models


class UserOrder(models.Model):
    user = models.ForeignKey(User)
    order_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username
