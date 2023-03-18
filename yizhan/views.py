from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User,Yizhan
import hashlib
from django.views.decorators.cache import cache_page
# from .models import Book

from django.db import models

def info(request):
    all_book = Yizhan.objects.filter(is_active=True)
    return render(request,'yizhan/Item/corpus.html',locals())
# Create your views here.
#
# def all_book(request):
#     all_book = Book.objects.filter(is_active=True)
#
#     return render(request, 'yizhan/all_book.html', locals())
#
#
# def update_book(request, book_id):
#     try:
#         book = Book.objects.get(id=book_id)
#     except Exception as e:
#         print('--update book error is %s' % (e))
#         return HttpResponse("--The book is not existed")
#     if request.method == 'GET':
#         return render(request, 'yizhan/update_book.html', locals())
#     elif request.method == 'POST':
#         price = request.POST['price']
#         market_price = request.POST['market_price']
#         book.price = price
#         book.market_price = market_price
#         book.save()
#         return HttpResponseRedirect('/yizhan/all_book')
#

def delete_book(request):

    book_id=request.GET.get('book_id')
    if not book_id:
        return HttpResponse('--请求异常--')
    try:
        book=Yizhan.objects.get(id=book_id,is_active=True)
    except Exception as e:
        print('--delete book get error &s--'%(e))
        return HttpResponse('--The Book_id is Error')
    book.is_active=False
    book.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/yizhan/info')
def reg_view(request):
    if request.method == 'GET':
        return render(request, 'yizhan/firstpage/register.html')
    elif request.method == 'POST':
        if 'agree' in request.POST:
            username = request.POST['username']
            password_1 = request.POST['password_1']
            password_2 = request.POST['password_2']

            if password_1 != password_2:
                return HttpResponse('两次密码输入不一致')

            old_users = User.objects.filter(username=username)
            if old_users:
                return HttpResponse('用户名已注册')

            m = hashlib.md5()
            m.update(password_1.encode())
            password_m = m.hexdigest()
            try:
                user = User.objects.create(username=username, password=password_m)
            except Exception as e:
                print('--create user error %s--' % (e))
                return HttpResponse('用户名已注册')

            request.session['username'] = username
            request.session['uid'] = user.id

            # return HttpResponse('注册成功!')
            return HttpResponseRedirect('http://127.0.0.1:8000/yizhan/')
        else:
            return HttpResponseRedirect('http://127.0.0.1:8000/yizhan/error')

def login_view(request):
    if request.method == 'GET':
        if request.session.get('username')and request.session.get('uid'):
            # return HttpResponse('首页')
            return HttpResponseRedirect('http://127.0.0.1:8000/yizhan/')
        c_username=request.COOKIES.get('username')
        c_uid=request.COOKIES.get('uid')
        if c_username and c_uid:
            request.session['username']=c_username
            request.session['uid']=c_uid
            # return HttpResponse('首页')
            return HttpResponseRedirect('http://127.0.0.1:8000/yizhan/')
        return render(request, 'yizhan/firstpage/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s' % (e))
            return HttpResponse('您的用户名或密码有误，请重新输入')

        m = hashlib.md5()
        m.update(password.encode())

        if m.hexdigest() != user.password:
            return HttpResponse('您的用户名或密码有误，请重新输入')

        request.session['username'] = username
        request.session['uid'] = user.id
        # resp=HttpResponse('--登录成功--')
        resp= HttpResponseRedirect('http://127.0.0.1:8000/yizhan/')
        if 'remember' in request.POST:
            resp.set_cookie('username',username,3600*24)
            resp.set_cookie('uid',user.id,3600*24)

        return resp
def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    resp=HttpResponseRedirect('http://127.0.0.1:8000/yizhan/login')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp



def index_test(request):
    return render(request,'yizhan/firstpage/index.html')
def info_manege(request):
    all_book = Yizhan.objects.filter(is_active=True)
    return render(request,'yizhan/Item/item_info.html',locals())

def type_manage(request):
    all_book = Yizhan.objects.filter(is_active=True)
    return render(request,'yizhan/Item/item_type.html',locals())

def order_info(request):
    # all_order = OrderStatus.objects.all()
    return render(request,'yizhan/Order/order_info.html')

def order_shipping(request):
    return render(request,'yizhan/Order/order_shipping.html')

def user_info(request):
    all_user=User.objects.all()
    return render(request,'yizhan/Account/account_info.html',locals())

def bookinfo_add(request):
    if request.method == 'GET':
        return render(request, 'yizhan/Item/item_mdf.html')
    elif request.method == 'POST':
        Yizhan.objects.create(title=request.POST["title"],writer=request.POST['writer'],market_price=request.POST['market_price'],
                                 current_price=request.POST['current_price'],on_sale=request.POST['on_sale'],pub=request.POST['pub'])
        return HttpResponseRedirect('http://127.0.0.1:8000/yizhan/info')
def bookinfo_change(request):
    book_id=request.GET.get('book_id')
    if not book_id:
        return HttpResponse('--请求异常--')
    try:
        book = Yizhan.objects.get(id=book_id)
    except Exception as e:
            print('--update book error is %s' % (e))
            return HttpResponse("--The book is not existed")
    if request.method == 'GET':
            return render(request, 'yizhan/Item/item_edit.html', locals())
    elif request.method == 'POST':
            market_price = request.POST['market_price']
            current_price = request.POST['current_price']
            on_sale=request.POST['on_sale']
            book.market_price = market_price
            book.current_price = current_price
            book.on_sale=on_sale
            book.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/yizhan/info')

def category_add(request):
    return render(request,'yizhan/Item/item_addcategory.html')

def category_change(request):
    cat = request.GET.get('cat')
    if not cat:
        return HttpResponse('--请求异常--')
    try:
        kin = Yizhan.objects.get(category=cat)
    except Exception as e:
        print('--update book error is %s' % (e))
        return HttpResponse("--The type is not existed")
    if request.method == 'GET':
        return render(request, 'yizhan/Item/item_editcategory.html', locals())
    elif request.method == 'POST':
        des=request.POST['description']
        kin.description=des
        kin.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/yizhan/type')

    return render(request,'yizhan/Item/item_editcategory.html')

def product_add(request):

    return render(request,'yizhan/Item/item_addproduct.html')

def product_change(request):
    return render(request,'yizhan/Item/item_editproduct.html')
@cache_page(1)
def order_desc(request):
    return render(request,'yizhan/Order/order_mdf.html')

def user_desc(request):
    return render(request,'yizhan/Account/account_mdf.html')

def error(request):
    return render(request,'yizhan/Common/Error.html')