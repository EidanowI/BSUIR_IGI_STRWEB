from django.urls import path
from django.conf.urls.static import static
from django.urls import re_path
from autoservice import settings
from . import views

urlpatterns = [ 
    path('login/', views.login, name ='login'),
    path('', views.index, name='index'),
    path('about/', views.about , name ='about'),
    path('news/', views.news , name ='news'),
    path('faq/', views.faq , name ='faq'),
    path('contacts/', views.contacts , name ='contacts'),
    path('policy/', views.policy , name ='policy'),
    path('vacancy/', views.vacancy , name ='vacancy'),
    path('review_list/', views.review_list , name ='review_list'),
    path('coupons/', views.coupons , name ='coupons'),
    path('register/', views.register , name ='register'),
    path('cataloge/', views.cataloge , name ='cataloge'),
    path('settings/', views.settings , name ='settings'),
    path('review_list/create_review/', views.create_review , name ='create_review'),
    path('cart/', views.view_cart,name='view_cart'),
    path('popular_products/', views.popular_products,name='popular_products'),
    path('view_orders/', views.view_orders,name='view_orders'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('complete_order/', views.complete_order, name='complete_order'),

    path('crud/',views.ind_crud,name="crud"),
    path('add/',views.add ,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    re_path(r'^crud/delete/(?P<id>\d+)/$',views.delete,name="delete"),
    re_path(r'^crud/update/(?P<id>\d+)/$',views.update,name="update"),
    re_path(r'^crud/update/uprec/(?P<id>\d+)/$',views.uprec,name="uprec")
    #path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    #path('toggle_coupon/<int:coupon_id>/', views.toggle_coupon_status, name='toggle_coupon_status'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
