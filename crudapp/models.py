from django.db import models

class BusinessRule(models.Model):
    tags = models.JSONField("Tags")
    information = models.CharField("Information", max_length = 255, blank = True, null = True)
    createdAt = models.DateTimeField("Created At", auto_now_add = True)
    deletedAt = models.DateTimeField("Deleted at", blank = True, null = True)

    def __str__(self):
        return self.information
