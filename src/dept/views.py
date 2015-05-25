from django.shortcuts import render, render_to_response, RequestContext,HttpResponse
from .models import Department

# Create your views here.

def home(request):
    return render_to_response("index.html", locals(), context_instance = RequestContext(request))

def department(request, dept_code1):
    try:
        dept = Department.objects.get(dept_code=dept_code1)
    except:
        return HttpResponse("sd")
    return  render(request, "department.html", {'department':dept})
