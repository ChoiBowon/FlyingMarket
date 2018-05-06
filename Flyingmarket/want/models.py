from django.db import models


class Want(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    country_id = models.IntegerField()
    created = models.DateField(auto_now=True)
    #thumbnail = models.ImageField()
    goods_id = models.IntegerField()
    price = models.IntegerField()
    user_id = models.IntegerField()
    is_matched = models.BooleanField(default=False)

    def __str__(self):
        return self.title

