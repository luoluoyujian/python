from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo,HeroInfo,Areas
from datetime import date
# Create your views here.

def my_render(request, template_path, context_dict={}):
    '''使用模板文件'''
    # 使用模板文件
    # 1.加载模板文件, 模板对象
    temp = loader.get_template(template_path)
    # 2.定义模板上下文:给模板文件传递数据，模板渲染:产生标准的html内容
    res_html = temp.render(context_dict)
    # 3.返回给浏览器
    return HttpResponse(res_html)

def index(request):
    # return HttpResponse('hello python')
    # return my_render(request,'booktest/index.html')
    return render(request,'index.html',{'content':'python 最牛'})

def index2(request):
    a='b'+1
    return HttpResponse('hello python2')


# day75代码开始
def show_books(request):
    '''显示图书的信息'''
    # 1.通过Models查找图书表中的数据
    books=BookInfo.objects.all()
    # 2.使用模板
    return render(request,'booktest/show_books.html',{'books':books})

def detail(request,bid):
    # 1.根据bid查询图书信息
    book=BookInfo.objects.get(id=bid)
    # 2.根据book查询关联的英雄信息
    heros=book.heroinfo_set.all()
    # 3.使用模板
    return render(request,'booktest/detail.html',{'book':book,'heros':heros})


def create(request):
    '''新增一本图书'''
    # 1.创建BookInfo对象
    b = BookInfo()
    b.btitle = 'C语言开发宝典'
    b.bpub_date = date(2019,10,1)
    # 2.保存进数据库
    b.save()
    # 3.返回应答,让浏览器再访问,重定向
    return HttpResponseRedirect('/show_books')

def delete(request, bid):
    '''删除点击的图书'''
    # 1.通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 2.删除
    book.delete()
    # 3.重定向，让浏览器访问/index
    return HttpResponseRedirect('/show_books')


def areas(request):
    '''获取广州市的上级地区和下级地区'''
    # 1.获取广州市的信息
    area=Areas.objects.get(atitle='广州市')
    # 2.查询广州市的上级地区
    parent=area.aParent
    # 3.查询广州市的下级地址
    children=area.areas_set.all()
    # 使用模板
    return render(request, 'areas.html', {'area': area, 'parent': parent, 'children': children})


def login(request):
    """
    展示登录页面
    """
    # 判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已登录, 跳转到首页
        return redirect('/index')
    if 'username' in request.COOKIES:
        username=request.COOKIES.get('username')
    else:
        username=''
    return render(request,'login.html',{'username':username})

def login_check(request):
    '''登录校验视图'''
    # request.POST 保存的是post方式提交的参数 QueryDict
    # request.GET 保存是get方式提交的参数  类型也是 QueryDict
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember =request.POST.get('remember')

    # 实际开发:根据用户名和密码查找数据库
    # 模拟: admin 123
    if username == 'admin' and password == '123':
        # 记住用户登录状态
        # 只有session中有islogin,就认为用户已登录
        request.session['islogin'] = True
        response = HttpResponseRedirect('/index')
        if remember=='on':
            # 设置cookie username，过期时间1周
            response.set_cookie('username', username, max_age=7 * 24 * 3600)
        return response


    else:
        return redirect('/login')

def test_ajax(request):
    '''显示ajax页面'''
    return render(request, 'test_ajax.html')


def ajax_handle(request):
    '''ajax请求处理'''
    # 返回的json数据 {'res':1}
    # num='a'+1
    return JsonResponse({'res':1})


#接下来实战ajax登录
def login_ajax(request):
    '''显示ajax登录页面'''
    return render(request, 'login_ajax.html')


def login_ajax_check(request):
    '''ajax登录校验'''
    # 1.获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2.进行校验,返回json数据
    if username == 'admin' and password == '123':
        # 用户名密码正确
        return JsonResponse({'res':1})
        # return redirect('/index') ajax请求在后台，不要返回页面或者重定向，这样是不行的，一定要返回Json！
    else:
        # 用户名或密码错误
        return JsonResponse({'res':0})


def set_cookie(request):
    '''设置cookie信息'''
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息,名字为num, 值为2
    # response.set_cookie('num', 2)
    #下面是设置cookie在两周之后过期
    response.set_cookie('num', 2, max_age=14*24*3600)
    # response.set_cookie('num', 2, expires=datetime.now()+timedelta(days=14))
    # 返回response
    return response

def get_cookie(request):
    '''获取cookie的信息'''
    # 取出cookie num的值
    num = request.COOKIES['num']
    return HttpResponse(num)


# /set_session
def set_session(request):
    '''设置session'''
    request.session['username'] = 'admin'
    request.session['age'] = 18
    # request.session.set_expiry(5)
    return HttpResponse('设置session')


# /get_session
def get_session(request):
    '''获取session'''
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+':'+str(age))

#　/clear_session
def clear_session(request):
    '''清除session信息'''
    # request.session.clear()
    request.session.flush()
    return HttpResponse('清除成功')


# /test_var
def test_var(request):
    '''模板变量'''
    my_dict = {'title':'字典键值'}
    my_list = [1,2,3]
    book = BookInfo.objects.get(id=1)
    # 定义模板上下文
    context = {'my_dict':my_dict, 'my_list':my_list, 'book':book}
    return render(request, 'test_var.html', context)

def test_tags(request):
    '''模板标签'''
    # 1. 查找所有图书的信息
    books=BookInfo.objects.all()
    return render(request,'test_tags.html',{'books':books})

def test_filters(request):
    books = BookInfo.objects.all()
    return render(request,'test_filters.html',{'books':books})