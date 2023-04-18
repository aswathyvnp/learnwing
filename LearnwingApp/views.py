from django.shortcuts import redirect, render
from LearnwingApp.forms import CategoryForm,AddCourseForm,AddSubCourseForm
from LearnwingApp.models import Course,SubCourse

# Create your views here.
def Home1(request):
    return render(request,'home.html')
def AdminPage(request):
    return render(request,'adminpage.html')

def AddCategory(request):
    form=CategoryForm()
    if request.method=='POST':
        form1=CategoryForm(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request,'addcategory.html',{'form':form})

def AddCourse(request):
    form=AddCourseForm()
    if request.method=='POST':
        form1=AddCourseForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
    return render(request,'addcourse.html',{'courseform':form})

def Edit(request,id):
    object=SubCourse.objects.get(id=id)
    form=AddSubCourseForm(instance=object)
    data=SubCourse.objects.all()
    if request.method=='POST':
        form1=AddSubCourseForm(request.POST,request.FILES,instance=object)
        if form1.is_valid():
            form1.save()
            return redirect('addsubcourse')
    return render(request,'adminpage.html',{'subcourseform':form,'data':data})

def AddSubCourse(request):
    form=AddSubCourseForm()
    data=SubCourse.objects.all()
    if request.method=='POST':
        form1=AddSubCourseForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
    return render(request,'addsubcourse.html',{'subcourseform':form,'data':data})

# def AddSyllabus(request):
#     form=SyllabusForm()
#     data=Syllabus.objects.all()
#     if request.method=='POST':
#         form1=SyllabusForm(request.POST)
#         if form1.is_valid():
#             form1.save()
#     return render(request,'adminpage.html',{'syllabusform':form,'data':data})

    
    
    
    
    
    
    # data=Course.objects.all()
    # if request.method=='POST':
    #     form1=AddCourseForm(request.POST,request.FILES, instance=object)
    #     if form1.is_valid():
    #         form1.save()
    #         # return redirect('/')
    # return render(request,"home.html",{'data':data,'form':form})
    
    



