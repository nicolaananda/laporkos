# models.py
from django.db import models


class Ticket(models.Model):
    ROOM_CHOICES = [
        (1, "Kamar 1"),
        (2, "Kamar 2"),
        (3, "Kamar 3"),
        (4, "Kamar 4"),
        (5, "Kamar 5"),
        (6, "Kamar 6"),
        (7, "Kamar 7"),
        (8, "Kamar 8"),
        (9, "Kamar 9"),
        (10, "Kamar 10"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    room_number = models.IntegerField(choices=ROOM_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
