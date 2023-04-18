
from django.urls import  path
from LearnwingApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   
   path('',views.Home1),
   path('adminpage',views.AdminPage,name='adminpage'),
   path('course_category',views.AddCategory,name='course_category'),
   path('addcourse',views.AddCourse,name='addcourse'),
   path('addsubcourse',views.AddSubCourse,name='addsubcourse'),
   # path('addsyllabus',views.AddSyllabus,name='addsyllabus'),
   path('edit/<int:id>',views.Edit,name='edit')
   
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 