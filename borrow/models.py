from django.db import models
from books.models import Book
from members.models import Member
from uuid import uuid4

# Create your models here.
class BorrowRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrow_records")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrow_records")
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.user.first_name} {self.member.user.last_name}"