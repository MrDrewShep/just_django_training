"""crashcourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Below is a direct way of bringing in a view
# but not scalable. Rather, we create `urls.py` 
# in the app directory and include that whole file
# from todo.views import todo_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls', namespace='todos')),
    # path('', todo_list), see notes above
]
