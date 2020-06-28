from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Membership,  UserMemberShip, Subscription
from django.urls import reverse
from django.http import HttpResponseRedirect

# this is the convinience method for getting the user membership
def get_user_membership(request):
    user_membership = UserMemberShip.objects.filter(user=request.user)
    if user_membership.exists():
        return user_membership.first()
    return None

# this is the convinience method for the selected membership
def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription=user_subscription_qs.first()
        return user_subscription
    return None

def get_seleted_membership(request):
    membership_type=request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(
        membership_type=membership_type
    )
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None

class MembershipSelectView(ListView):
    model=Membership
    template_name="memberships/membership_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context['current_membership']= str(current_membership.membership)
        return context

    def post(self, request, *args, **kwargs):
        selected_membership_type = request.POST.get('membership_type')
        user_membership=get_user_membership(request)
        user_subscription = get_user_subscription(request)
        selected_membership_qs = Membership.objects.filter(
            membership_type=selected_membership_type
        )
        if selected_membership_qs.exists():
            selected_membership=selected_membership_qs.first()
        request.session['selected_membership_type']=selected_membership.membership_type
        return HttpResponseRedirect(reverse('payment'))

def paymentView(request):
    user_membership = get_user_membership(request)
    selected_membership = get_seleted_membership(request)
    context={
        'selected_membership':selected_membership
    }
    return render(request, 'memberships/payment.html', context)



    


        






