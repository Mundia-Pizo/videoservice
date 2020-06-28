from django.urls import path
from .views import MembershipSelectView, paymentView
urlpatterns=[
    path('membership/',MembershipSelectView.as_view(), name='membership' ),
    path('payment/', paymentView, name='payment' )
]