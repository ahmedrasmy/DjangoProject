
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', home, name = 'home'),
    path('add_project/', add_project, name = 'add_project'),
    path('admin/', admin_home, name = 'admin'),
    path('admin/add5projects/', add5projects, name = 'add5projects'),
    path('admin/project_reports/', project_reports, name = 'project_reports'),
    path('admin/comments_reports/', comments_reports, name = 'comments_reports'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)