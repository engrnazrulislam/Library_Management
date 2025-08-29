from django.db import models
from books.models import Book
from members.models import Member
from users.models import User
from uuid import uuid4
from django.utils.timezone import now

class BorrowReturnRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    BORROWED = 'Borrowed'
    RETURN = 'Return'
    STATUS_CHOICES = [
        (BORROWED, 'Borrowed'),
        (RETURN, 'Return')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrow_records")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrow_records")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrow_records")
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=BORROWED)

    def save(self, *args, **kwargs):
        if self.status == self.BORROWED:
            if self.book.quantity and self.book.quantity > 0:
                self.book.quantity -= 1
                self.book.save()
        elif self.status == self.RETURN:
            self.book.quantity += 1
            self.book.save()
            if not self.return_date:
                self.return_date = now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} - {self.status} by {self.member.user.first_name} {self.member.user.last_name}"
