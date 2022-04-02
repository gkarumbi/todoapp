from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include


urlpatterns =[
    
    path('',views.index,name="TodoList"),
    path('api/v1/', views.CategoryListAPIView.as_view()),
    path('api/v2/', views.TodoListAPIView.as_view()),



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)