from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact_us', views.contact_us),
    path('about_us', views.about_us),
    path('current_roasts', views.current_roasts),
    path('upcoming_roasts', views.upcoming_roasts),
    path('<int:roast_id>/view_roast', views.view_roast),
    path('<int:roast_id>/add_to_cart', views.add_to_cart),
    path('submit_mail', views.submit_mail),
    path('back_home', views.back_home),

    # paypal
    path('store/', views.store, name="store"),
    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    path('complete/', views.paymentComplete, name="complete"),
]