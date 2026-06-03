from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.utils import timezone

from django.db.models import Q

from datetime import timedelta

from django.core.mail import send_mail

from django.conf import settings

from .models import (

    StudentProfile,
    Book,
    BookIssue,
    BookRequest

)


# ================= HOME PAGE =================

def home(request):

    total_books = Book.objects.count()

    total_students = StudentProfile.objects.count()

    issued_books = BookIssue.objects.count()

    return render(request, 'home.html', {

        'total_books': total_books,
        'total_students': total_students,
        'issued_books': issued_books

    })


# ================= REGISTER PAGE =================

def register_page(request):

    if request.method == "POST":

        username = request.POST.get('username')

        email = request.POST.get('email')

        year = request.POST.get('year')

        department = request.POST.get('department')

        reg_no = request.POST.get('reg_no')

        phone = request.POST.get('phone')

        pin = request.POST.get('pin')

        student_image = request.FILES.get('student_image')

        password = reg_no + pin

        # ================= VALIDATION =================

        if User.objects.filter(username=username).exists():

            return render(request, 'register.html', {

                'error': 'Username already exists'

            })

        if User.objects.filter(email=email).exists():

            return render(request, 'register.html', {

                'error': 'Email already exists'

            })

        # ================= CREATE USER =================

        user = User.objects.create_user(

            username=username,
            email=email,
            password=password

        )

        # ================= CREATE PROFILE =================

        StudentProfile.objects.create(

            user=user,
            year=year,
            department=department,
            reg_no=reg_no,
            phone=phone,
            pin=pin,
            student_image=student_image

        )

        return render(request, 'register.html', {

            'success': 'Registration Successful'

        })

    return render(request, 'register.html')


# ================= STUDENT LOGIN =================

def login_page(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(

            request,
            username=username,
            password=password

        )

        if user is not None:

            login(request, user)

            request.session['role'] = 'student'

            request.session['username'] = username

            return redirect('student_profile')

        return render(request, 'login.html', {

            'error': 'Invalid Username or Password'

        })

    return render(request, 'login.html')


# ================= STAFF LOGIN =================

def staff_login_page(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        if password == "admin.vk.aurcm.in":

            request.session['role'] = 'admin'

            request.session['username'] = username

            return redirect('admin_dashboard')

        return render(request, 'staff_login.html', {

            'error': 'Invalid Staff Password'

        })

    return render(request, 'staff_login.html')


# ================= LOGOUT =================

def logout_user(request):

    logout(request)

    request.session.flush()

    return redirect('home')


# ================= STUDENT PROFILE =================

def student_profile(request):

    if not request.user.is_authenticated:

        return redirect('login')

    profile = StudentProfile.objects.get(

        user=request.user

    )

    requests = BookRequest.objects.filter(

        student=request.user

    ).order_by('-id')

    issued_books = BookIssue.objects.filter(

        student=request.user

    ).order_by('-id')

    due_books = BookIssue.objects.filter(

        student=request.user,
        due_generated=True

    ).order_by('-id')

    active_borrowed = BookIssue.objects.filter(

        student=request.user,
        returned=False

    ).count()

    total_books = Book.objects.count()

    return render(request, 'student_profile.html', {

        'profile': profile,
        'requests': requests,
        'issued_books': issued_books,
        'due_books': due_books,
        'active_borrowed': active_borrowed,
        'total_books': total_books

    })


# ================= EDIT PROFILE =================

def edit_profile(request):

    if not request.user.is_authenticated:

        return redirect('login')

    profile = StudentProfile.objects.get(

        user=request.user

    )

    if request.method == "POST":

        phone = request.POST.get('phone')

        year = request.POST.get('year')

        email = request.POST.get('email')

        student_image = request.FILES.get('student_image')

        profile.phone = phone

        profile.year = year

        profile.user.email = email

        profile.user.save()

        if student_image:

            profile.student_image = student_image

        profile.save()

        return redirect('student_profile')

    return render(request, 'edit_profile.html', {

        'profile': profile

    })


# ================= ADMIN DASHBOARD =================

def admin_dashboard(request):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    return render(request, 'admin_dashboard.html')


# ================= ADD BOOK =================

def add_book(request):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    if request.method == "POST":

        title = request.POST.get('title')

        author = request.POST.get('author')

        section = request.POST.get('section')

        row = request.POST.get('row')

        column = request.POST.get('column')

        quantity = request.POST.get('quantity')

        cover_image = request.FILES.get('cover_image')

        Book.objects.create(

            title=title,
            author=author,
            section=section,
            row=row,
            column=column,
            quantity=quantity,
            cover_image=cover_image

        )

        return redirect('admin_dashboard')

    return render(request, 'add_book.html')


# ================= STUDENT VIEW BOOKS =================

def view_books(request):

    books = Book.objects.all()

    search = request.GET.get('search')

    if search:

        books = books.filter(

            Q(title__icontains=search) |
            Q(author__icontains=search) |
            Q(section__icontains=search)

        )

    return render(request, 'view_books.html', {

        'books': books

    })


# ================= ADMIN VIEW BOOKS =================

def admin_view_books(request):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    books = Book.objects.all().order_by('-id')

    search = request.GET.get('search')

    if search:

        books = books.filter(

            Q(title__icontains=search) |
            Q(author__icontains=search) |
            Q(section__icontains=search)

        )

    return render(request, 'admin_view_books.html', {

        'books': books

    })


# ================= EDIT BOOK =================

def edit_book(request, book_id):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    book = Book.objects.get(id=book_id)

    if request.method == "POST":

        book.title = request.POST.get('title')

        book.author = request.POST.get('author')

        book.section = request.POST.get('section')

        book.row = request.POST.get('row')

        book.column = request.POST.get('column')

        book.quantity = request.POST.get('quantity')

        if request.FILES.get('cover_image'):

            book.cover_image = request.FILES.get('cover_image')

        book.save()

        return redirect('admin_view_books')

    return render(request, 'edit_book.html', {

        'book': book

    })


# ================= REQUEST BOOK =================

def request_book(request, book_id):

    if not request.user.is_authenticated:

        return redirect('login')

    book = Book.objects.get(id=book_id)

    already_requested = BookRequest.objects.filter(

        student=request.user,
        book=book,
        status="Pending"

    ).exists()

    if not already_requested:

        BookRequest.objects.create(

            student=request.user,
            book=book

        )

    return redirect('view_books')


# ================= STUDENT BOOK REQUESTS =================

def student_book_requests(request):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    requests = BookRequest.objects.all().order_by('-id')

    return render(request, 'student_book_request.html', {

        'requests': requests

    })


# ================= APPROVE REQUEST =================

def approve_request(request, request_id):

    role = request.session.get('role')

    if role != 'admin':
        return redirect('staff_login')

    req = BookRequest.objects.get(id=request_id)
    book = req.book

    if book.quantity > 0:

        BookIssue.objects.create(
            student=req.student,
            book=book
        )

        book.quantity -= 1
        book.save()

        req.status = "Approved"
        req.save()

        # SEND MAIL
        send_mail(
            'Book Request Approved',
            f'''
Hello {req.student.username},

Your requested book "{book.title}" has been approved.

Please collect the book from the library.

Thank You,
Smart Library
            ''',
            settings.EMAIL_HOST_USER,
            [req.student.email],
            fail_silently=False
        )

    return redirect('student_book_requests')

       

# ================= REJECT REQUEST =================

def reject_request(request, request_id):

    role = request.session.get('role')

    if role != 'admin':
        return redirect('staff_login')

    req = BookRequest.objects.get(id=request_id)

    req.status = "Rejected"
    req.save()

    send_mail(
        'Book Request Rejected',
        f'''
Hello {req.student.username},

Your requested book "{req.book.title}" has been rejected by the library admin.

Please contact library staff for more details.

Thank You,
Smart Library
        ''',
        settings.EMAIL_HOST_USER,
        [req.student.email],
        fail_silently=False
    )

    return redirect('student_book_requests')
   


# ================= ISSUED BOOKS =================

def issued_books(request):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    issues = BookIssue.objects.filter(

        returned=False

    ).order_by('-id')

    search = request.GET.get('search')

    if search:

        issues = issues.filter(

            Q(student__username__icontains=search) |
            Q(book__title__icontains=search) |
            Q(book__author__icontains=search) |
            Q(student__studentprofile__department__icontains=search) |
            Q(student__studentprofile__year__icontains=search)

        )

    return render(request, 'issued_books.html', {

        'issues': issues

    })


# ================= RETURN BOOK =================

def return_book(request, issue_id):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    issue = BookIssue.objects.get(id=issue_id)

    issue.returned = True

    issue.returned_at = timezone.now()

    issue.save()

    book = issue.book

    book.quantity += 1

    book.save()

    return redirect('issued_books')


# ================= BORROWED HISTORY =================

def borrowed_history(request):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    issues = BookIssue.objects.all().order_by('-id')

    search = request.GET.get('search')

    if search:

        issues = issues.filter(

            Q(student__username__icontains=search) |
            Q(student__studentprofile__department__icontains=search) |
            Q(student__studentprofile__year__icontains=search) |
            Q(book__title__icontains=search) |
            Q(book__author__icontains=search)

        )

    return render(request, 'borrowed_book_history.html', {

        'issues': issues

    })


# ================= DUE GENERATION =================

def due_generation(request):

    role = request.session.get('role')

    if role != 'admin':
        return redirect('staff_login')

    issues = BookIssue.objects.filter(
        returned=False
    ).order_by('-id')

    return render(
        request,
        'due_generation.html',
        {
            'issues': issues
        }
    )


# ================= GENERATE DUE =================

def generate_due(request, issue_id):

    role = request.session.get('role')

    if role != 'admin':
        return redirect('staff_login')

    issue = BookIssue.objects.get(id=issue_id)

    issue.due_generated = True
    issue.due_generated_at = timezone.now()
    issue.due_return_date = timezone.now() + timedelta(days=2)

    issue.save()

    # SEND MAIL
    send_mail(
        'Library Due Notice',
        f'''
Hello {issue.student.username},

A due has been generated for the book:

Book Name: {issue.book.title}

Return Date:
{issue.due_return_date.strftime("%d-%m-%Y %I:%M %p")}

Please return the book before the due date.

Thank You,
Smart Library
        ''',
        settings.EMAIL_HOST_USER,
        [issue.student.email],
        fail_silently=False
    )

    return redirect('due_generation')


# ================= CLEAR DUE =================

def clear_due(request, issue_id):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    issue = BookIssue.objects.get(id=issue_id)

    issue.due_generated = False

    issue.due_generated_at = None

    issue.due_return_date = None

    issue.save()

    return redirect('due_generation')


# ================= MANAGE STUDENTS =================

def manage_students(request):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    students = StudentProfile.objects.all()

    department = request.GET.get('department')

    year = request.GET.get('year')

    if department:

        students = students.filter(

            department__icontains=department

        )

    if year:

        students = students.filter(

            year__icontains=year

        )

    return render(request, 'manage_students.html', {

        'students': students

    })


# ================= DELETE STUDENT =================

def delete_student(request, student_id):

    role = request.session.get('role')

    if role != 'admin':

        return redirect('staff_login')

    student = StudentProfile.objects.get(id=student_id)

    student.user.delete()

    return redirect('manage_students')