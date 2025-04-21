from django.contrib import admin
from django.urls import path , include
# from core.views import index, contact
from item.views import detail , newitem , delete , edititem , browseitems
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('dashboard/' , include('dashboard.urls')),
    
    path('' , include('conversation.urls')),

    path('items/<int:pk>' , detail , name='detail'),
    path('items/<int:pk>/delete/' , delete , name='delete'),
    path('items/<int:pk>/edit/' , edititem , name='edititem'),
    path('new/' , newitem , name='newitem'),
    path('items/' , browseitems , name='browseitems'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
