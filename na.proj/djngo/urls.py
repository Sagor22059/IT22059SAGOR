from django.contrib import admin
from django.urls import path
from contest_app import views


urlpatterns = [
 path('admin/', admin.site.urls),
 path('', views.home, name='home'),
 path('register/', views.register_student, name='register'),
 path('submit-problem/', views.submit_problem, name='submit_problem'),
 path('submissions/', views.list_submissions, name='list_submissions'),

]