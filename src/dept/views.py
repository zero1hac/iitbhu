from django.shortcuts import render, render_to_response, RequestContext
from .models import department

# Create your views here.

def home(request):
    return render_to_response("index.html", locals(), context_instance = RequestContext(request))

def department(request, dept_code_):
    dept_ = department.objects.get(dept_code=dept_code_)
    return  render(request, "department.html", {'department':dept_})