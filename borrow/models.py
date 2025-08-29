from django.db import models
from books.models import Book
from members.models import Member
from uuid import uuid4
from users.models import User
from django.utils.timezone import now
# Create your models here.
class BorrowReturnRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    BORROWED = 'Borrowed'
    RETURN = 'Return'
    AVAILABLE='Available'
    STATUS_CHOICES = [
        (BORROWED, 'Borrowed'),
        (RETURN, 'Return'),
        (AVAILABLE, 'Available')
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="borrow_records")
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrow_records")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrow_records")
    borrow_date = models.DateField(auto_now_add=True)

    return_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=AVAILABLE)

    def save(self, *args, **kwargs):
        if self.status == self.RETURNED and not self.return_date:
            self.return_date = now().date()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.book.title} - {self.get_status_display()} borrowed by {self.member.user.first_name} {self.member.user.last_name}"