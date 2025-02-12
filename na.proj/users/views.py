from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden,HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from solution.models import Solution

def is_admin(user):
    return user.role == 'admin'

@user_passes_test(is_admin)
def admin_only_view(request):
    return HttpResponse("Welcome, Admin!")


def is_admin(user):
    return user.role == 'admin'


def admin_only_view(request):
    return HttpResponse("Welcome, Admin!")


def approve_solution(request, solution_id):
    if request.user.role not in ['admin', 'co-admin']:
        return HttpResponseForbidden("Access Denied")
    solution = get_object_or_404(Solution, id=solution_id)
    solution.is_approved = True
    solution.save()
    return redirect('pending_approvals')


def student_profile(request):
    solutions = Solution.objects.filter(student=request.user).order_by('-submitted_at')
    return render(request, 'users/student_profile.html', {'solution': solutions})
