from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='blog'),
    path("about", views.about, name='about'),
    path("base", views.base, name='base'),
    path("premium", views.premium, name='premium'),
    path("contact", views.contact, name='contact'),
    path("submit_contact", views.contact_form, name='submit_contact'),

    path("search/", views.search, name='search'),
    # path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    # path('payment/', views.payment_view, name='payment'),
    # path('payment/success/', views.payment_success_view, name='payment_success'),
    path("add_blog", views.add_blog, name='add_blog'),
    path("create_blog", views.create_blog, name='create_blog'),
    # path("create_blog/int:id>", views.create_blog, name='create_blog'),
    path("update_blog/<int:id>", views.update_blog, name='update_blog'),
    path("delete_blog/<int:id>", views.delete_blog, name='delete_blog'),
    path("read_blog/<int:id>", views.read_blog, name='read_blog'),
    
    
]