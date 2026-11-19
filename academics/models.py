from django.conf import settings
from django.db import models

class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    units = models.PositiveSmallIntegerField(default=3)

    # instructor FK (1:N)
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="subjects_taught"
    )

    # students FK (N:M)
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="Enrollment",
        related_name="subjects_enrolled"
    )

    # junction table / associative entity
class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE
    )
    date_enrolled = models.DateField(auto_now_add=True)

class Announcement(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        related_name="announcements"
    )

    title = models.CharField(max_length=120)
    body = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-posted_at"]


# table level rules, constraints, ordering
class Meta:
    constraints=(
        models.UniqueConstraint(
            fields=["student", "subject"],
            name="unique_enrollment"
        )
    )


def __str__(self):
    return f"{self.code} - {self.title}"