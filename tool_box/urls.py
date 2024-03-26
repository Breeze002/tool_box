# tool_box/urls.py
from django.urls import path

import tool_box.views as views

'''
用来连接相应的urls的
'''

urlpatterns = [   # 这个就相当于路由
    path('', views.index),
    path('get_AItool', views.get_AItool),
    path('research_tool', views.research_tool),
]