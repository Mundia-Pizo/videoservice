from django.urls import path
from .views import MembershipSelectView, paymentView, PaymentRedirectView
urlpatterns=[
    path('membership/',MembershipSelectView.as_view(), name='membership' ),
    path('payment/', paymentView, name='payment' ),
    path('payment_redirect/', PaymentRedirectView.as_view(), name='payment-redirect')
]