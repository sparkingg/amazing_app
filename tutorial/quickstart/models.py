from django.db import models


class Dag(models.Model):
    name = models.CharField(max_length=12)
    owner = models.ForeignKey(to="auth.user", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tweet(models.Model):
    text = models.TextField(max_length=140)
    photo = models.URLField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(to="auth.user", on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.author,self.id)


class Follow(models.Model):
    follower = models.ForeignKey(to="auth.user", on_delete=models.CASCADE, related_name='follows')
    follows = models.ForeignKey(to="auth.user", related_name='followers', on_delete=models.CASCADE)
    followed = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{} to {}'.format(self.follower,self.follows)
