from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.utils import timezone
import datetime

User = get_user_model()

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    published_date = models.DateField(default=datetime.date.today)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    total_copies = models.IntegerField(default=5)
    available_copies = models.IntegerField(default=4)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5)])
    rating_text = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} on '{self.book.title}': {self.rating}/5"

class Reserve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserve_date = models.DateTimeField(default=timezone.now)
    TAKEN = 'T'
    AVAILABLE = 'A'
    STATUS_CHOICE = {
        TAKEN: 'Taken',
        AVAILABLE: 'Available'
    }
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=AVAILABLE)

    def __str__(self):
        return f'{self.user} reserved "{self.book}"'

# class Fine(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     reserve = models.ForeignKey(Reserve, on_delete=models.PROTECT)
#     amount = models.IntegerField(default=100)
#     PAID = 'P'
#     UNPAID = 'U'
#     STATUS_CHOICE = {
#         PAID: 'Paid',
#         UNPAID: 'Unpaid'
#     }
#     status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=UNPAID)

#     def __str__(self):
#         return f'{self.user} - {self.amount}'

def get_default_return_date():
    return datetime.date.today() + timezone.timedelta(days=14)

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(default=datetime.date.today)
    return_date = models.DateField(default=get_default_return_date)

    def __str__(self):
        return f'{self.user.username} borrowed "{self.book.title}" till {self.return_date}'
