from django.urls import path
# from .views import integer,string,slug123,path123
from .views import *

urlpatterns = [
      path('integer/<int:pk>',integer,name='integer'),
      path('string/<str:pk>',string,name='string'),
      path('slug123/<slug:pk>',slug123,name='slug123'),
      path('path123/<path:pk>',path123,name='path123'),
      
      # for taking all together
      path('combination/<path:pk>/<slug:pk1>/<str:pk2>/<int:pk3>',combination,name='combination')
]