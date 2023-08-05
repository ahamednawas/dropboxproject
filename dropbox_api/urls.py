from django.urls import path,include
from .views import dropbox_oauth,Get_Refresh_Token,shared_link

urlpatterns = [
path('api-auth/', include('rest_framework.urls')),
    path('dropboxauth/',dropbox_oauth,name='oauth'),
    path('authorized/',Get_Refresh_Token, name='refreshtoken'),
    path('sharing/',shared_link,name='sharing'),


]
