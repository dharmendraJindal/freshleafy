from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class UserOrder(models.Model):
    user = models.ForeignKey(User)
    order_timestamp = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.user.username
