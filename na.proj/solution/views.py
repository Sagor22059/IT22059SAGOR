from django.http import HttpResponseForbidden
from django.shortcuts import render
from .models import Solution

def pending_approvals(request):
    if request.user.role not in ['admin', 'co-admin']:
        return HttpResponseForbidden("Access Denied")
    solutions = Solution.objects.filter(is_approved=False)
    return render(request, 'solutions/pending_approvals.html', {'solutions': solutions})
from django.shortcuts import render, redirect
from .forms import SolutionSubmissionForm

def submit_solution(request):
    if request.method == 'POST':
        form = SolutionSubmissionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.student = request.user
            solution.save()
            return redirect('student_profile')
    else:
        form = SolutionSubmissionForm()
    return render(request, 'solutions/submit_solution.html', {'form': form})

