from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView

from .models import Post
# Create your views here.

# url연결해줄때 과연 어떤것들은 render로 넘겨줄건지 정한다. 

def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')
    
def post_create_view(request):
    return render(request, 'posts/post_form.html')

def post_update_view(request, id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')


def url_view(request):
    print('url_view()')
    data = {'code' : '001', 'msg' : 'OK'}
    return HttpResponse('url_view')
    # return JsonResponse(data)

def url_parameter_view(request,username):
    print('url_parameter_view()')
    print(username)
    print(request.GET)
    return HttpResponse(username)

def function_view(request):
    print(f'request.meothd: {request.method}')
    print(f'request.GET : {request.GET}')
    print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'

def function_list_view(request):
    object_list = post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html', {'object_list' : object_list})