from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from datetime import timedelta


# ================= STUDENT PROFILE =================

class StudentProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    year = models.CharField(
        max_length=20
    )

    department = models.CharField(
        max_length=100
    )

    reg_no = models.CharField(
        max_length=50
    )

    phone = models.CharField(
        max_length=15
    )

    pin = models.CharField(
        max_length=10
    )

    # ================= EMAIL =================

    email = models.EmailField(
        null=True,
        blank=True
    )

    # ================= STUDENT IMAGE =================

    student_image = models.ImageField(
        upload_to='student_images/',
        null=True,
        blank=True
    )

    def __str__(self):

        return self.user.username


# ================= BOOK MODEL =================

class Book(models.Model):

    title = models.CharField(
        max_length=200
    )

    author = models.CharField(
        max_length=200
    )

    section = models.CharField(
        max_length=100
    )

    row = models.CharField(
        max_length=50
    )

    column = models.CharField(
        max_length=50
    )

    quantity = models.IntegerField(
        default=1
    )

    # ================= BOOK COVER IMAGE =================

    cover_image = models.ImageField(
        upload_to='book_covers/',
        null=True,
        blank=True
    )

    def __str__(self):

        return self.title


# ================= BOOK REQUEST =================

class BookRequest(models.Model):

    STATUS_CHOICES = [

        ('Pending', 'Pending'),

        ('Approved', 'Approved'),

        ('Rejected', 'Rejected')

    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    requested_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.student.username} - {self.book.title}"


# ================= BOOK ISSUE =================

class BookIssue(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    # ================= ISSUE =================

    issued_at = models.DateTimeField(
        auto_now_add=True
    )

    # ================= RETURN =================

    returned = models.BooleanField(
        default=False
    )

    returned_at = models.DateTimeField(
        null=True,
        blank=True
    )

    # ================= DUE STATUS =================

    due_generated = models.BooleanField(
        default=False
    )

    due_generated_at = models.DateTimeField(
        null=True,
        blank=True
    )

    due_return_date = models.DateTimeField(
        null=True,
        blank=True
    )

    due_cleared = models.BooleanField(
        default=False
    )

    # ================= GENERATE DUE =================

    def generate_due(self):

        self.due_generated = True

        self.due_generated_at = timezone.now()

        self.due_return_date = timezone.now() + timedelta(days=2)

        self.save()

    # ================= CLEAR DUE =================

    def clear_due(self):

        self.due_generated = False

        self.due_cleared = True

        self.save()

    def __str__(self):

        return f"{self.student.username} - {self.book.title}"