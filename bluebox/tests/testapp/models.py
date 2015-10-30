from django.db import models


class MockObject(models.Model):
    content = models.TextField()

    def get_absolute_url(self):
        return '/object/%s/' % self.id
