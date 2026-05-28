from django.urls import path

from . import views


urlpatterns = [

    # ================= HOME =================

    path(
        '',
        views.home,
        name='home'
    ),

    # ================= REGISTER =================

    path(
        'register/',
        views.register_page,
        name='register'
    ),

    # ================= STUDENT LOGIN =================

    path(
        'login/',
        views.login_page,
        name='login'
    ),

    # ================= STAFF LOGIN =================

    path(
        'staff-login/',
        views.staff_login_page,
        name='staff_login'
    ),

    # ================= LOGOUT =================

    path(
        'logout/',
        views.logout_user,
        name='logout'
    ),

    # ================= STUDENT PROFILE =================

    path(
        'student-profile/',
        views.student_profile,
        name='student_profile'
    ),

    # ================= EDIT PROFILE =================

    path(
        'edit-profile/',
        views.edit_profile,
        name='edit_profile'
    ),

    # ================= ADMIN DASHBOARD =================

    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    # ================= ADD BOOK =================

    path(
        'add-book/',
        views.add_book,
        name='add_book'
    ),

    # ================= STUDENT VIEW BOOKS =================

    path(
        'view-books/',
        views.view_books,
        name='view_books'
    ),

    # ================= ADMIN VIEW BOOKS =================

    path(
        'admin-view-books/',
        views.admin_view_books,
        name='admin_view_books'
    ),

    # ================= EDIT BOOK =================

    path(
        'edit-book/<int:book_id>/',
        views.edit_book,
        name='edit_book'
    ),

    # ================= REQUEST BOOK =================

    path(
        'request-book/<int:book_id>/',
        views.request_book,
        name='request_book'
    ),

    # ================= STUDENT BOOK REQUESTS =================

    path(
        'student-book-requests/',
        views.student_book_requests,
        name='student_book_requests'
    ),

    # ================= APPROVE REQUEST =================

    path(
        'approve-request/<int:request_id>/',
        views.approve_request,
        name='approve_request'
    ),

    # ================= REJECT REQUEST =================

    path(
        'reject-request/<int:request_id>/',
        views.reject_request,
        name='reject_request'
    ),

    # ================= ISSUED BOOKS =================

    path(
        'issued-books/',
        views.issued_books,
        name='issued_books'
    ),

    # ================= RETURN BOOK =================

    path(
        'return-book/<int:issue_id>/',
        views.return_book,
        name='return_book'
    ),

    # ================= BORROWED BOOK HISTORY =================

    path(
        'borrowed-history/',
        views.borrowed_history,
        name='borrowed_history'
    ),

    # ================= DUE GENERATION =================

    path(
        'due-generation/',
        views.due_generation,
        name='due_generation'
    ),

    # ================= GENERATE DUE =================

    path(
        'generate-due/<int:issue_id>/',
        views.generate_due,
        name='generate_due'
    ),

    # ================= CLEAR DUE =================

    path(
        'clear-due/<int:issue_id>/',
        views.clear_due,
        name='clear_due'
    ),

    # ================= MANAGE STUDENTS =================

    path(
        'manage-students/',
        views.manage_students,
        name='manage_students'
    ),

    # ================= DELETE STUDENT =================

    path(
        'delete-student/<int:student_id>/',
        views.delete_student,
        name='delete_student'
    ),

]