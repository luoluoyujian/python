# 作者: 王道 龙哥
# 2022年08月23日16时43分48秒
from booktest import views
from django.urls import path
urlpatterns = [
    path('index/',views.index),
    path('index2/',views.index2),
    path('show_books/',views.show_books),
    path('books/<int:bid>',views.detail),
    path('create/',views.create),
    path('delete<int:bid>',views.delete),
    path('areas',views.areas),
    path('login/',views.login),
    path('login_check/',views.login_check),
    path('test_ajax/',views.test_ajax),
    path('ajax_handle/',views.ajax_handle),
    path('login_ajax/',views.login_ajax),
    path('login_ajax_check/',views.login_ajax_check),
    path('set_cookie/',views.set_cookie),
    path('get_cookie/',views.get_cookie),
    path('set_session/',views.set_session),
    path('get_session/',views.get_session),
    path('clear_session/',views.clear_session),
    path('test_var/',views.test_var),
    path('test_tags/',views.test_tags),
    path('test_filters/',views.test_filters)
]