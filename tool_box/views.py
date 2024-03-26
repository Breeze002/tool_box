# tool_box/views.py
from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import render
import os
'''
主要就是用来刷新对应的html界面的
'''


def index(request):
    return render(request, 'index.html')


def get_AItool(request):
    if request.method == 'GET':
        HTML_FILE_PATH = os.path.abspath(os.path.join('.\\templates', 'AItool.html'))

        # 检查文件是否存在
        if os.path.exists(HTML_FILE_PATH):
            # 读取文件内容
            with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
                html_content = file.read()
            # 返回文件内容作为HTTP响应
            return HttpResponse(html_content)
        else:
            # 如果文件不存在，返回404错误页面
            return HttpResponseNotFound('The requested page does not exist.')
    else:
        # 如果请求不是GET类型，返回405 Method Not Allowed
        return HttpResponseNotAllowed(['GET'])


def research_tool(request):
    if request.method == 'GET':
        HTML_FILE_PATH = os.path.abspath(os.path.join('.\\templates', 'research.html'))
        # 检查文件是否存在
        if os.path.exists(HTML_FILE_PATH):
            # 读取文件内容
            with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
                html_content = file.read()
            # 返回文件内容作为HTTP响应
            return HttpResponse(html_content)
        else:
            # 如果文件不存在，返回404错误页面
            return HttpResponseNotFound('The requested page does not exist.')
    else:
        # 如果请求不是GET类型，返回405 Method Not Allowed
        return HttpResponseNotAllowed(['GET'])