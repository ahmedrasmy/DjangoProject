from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    if request.session.has_key('user_name'):
        return render(request, 'home.html')
    else:
        return redirect('login')


def add_project(request):
    if request.session.has_key('user_name'):
        if request.method == 'POST':
            user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]
            newproject = Projects.objects.create(
                title=request.POST['title'], category=request.POST['category'],
                total_target=request.POST['total_target'],
                start_date=request.POST['start_date'], end_date=request.POST['end_date'],
                details=request.POST['details'],user=user

            )

            tags = request.POST['tags']
            list_tags = list(tags.split(" "))
            images = request.FILES.getlist('images')
            if newproject:
                for image in images:
                    photo = ProjectsImages.objects.create(
                        images=image,
                        project=newproject
                    )
                for tag in list_tags:
                    newtag = ProjectsTages.objects.create(
                        tags=tag,
                        project=newproject
                    )

            return HttpResponse("added........")
        else:
            return render(request, 'startCampain.html')
    else:
        return redirect('login')

def admin_home(request):
    if request.session.has_key('user_name'):
        user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]
        if user.is_admin == True:
            if request.method == 'POST':
                newcategory = Category.objects.create(
                    title=request.POST['title'], image_cat = request.FILES['image_cat'],
                    user=user
                )
                return redirect('admin')
            else:
                return render(request,'admin.html')
        else:
            return render(request, 'notfounderror.html')
    return redirect('login')

def add5projects(request):
    return render(request,'add5Projects.html')

def project_reports(request):
    return render(request,'ProjectsReport.html')

def comments_reports(request):
    return render(request,'commentsReport.html')