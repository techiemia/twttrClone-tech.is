from django.db import models
from cloudinary.models import CloudinaryField

#Creating my model

class Post(models.Model):
    class Meta(object):
        db_table = "posts"
    name = models.CharField(
        "name",
        blank=False,
        null=False,
        max_length=14,
        db_index=True,
        default="Anonymous"
    )

    body = models.CharField(
        "body", blank=True, null=True, max_length=140, db_index=True
    )

    created_at = models.DateTimeField("created Date TIme", blank=True, null=True, auto_now_add=True)

    image = CloudinaryField('image', blank =True, db_index = True)

    likes= models.PositiveIntegerField(
        'Likes', default=0, null=True, blank = True
    )
