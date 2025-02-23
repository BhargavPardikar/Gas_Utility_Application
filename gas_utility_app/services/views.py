from django.shortcuts import redirect, render

from services.forms import ServiceRequestForm
from .models import ServiceRequest
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, CustomerForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'services/submit_request.html', {'form': form})

def track_request(request):
  
    requests = ServiceRequest.objects.all()
    return render(request, 'services/track_request.html', {'requests': requests})

def account_info(request):
   
    customer = customer.objects.first()
    return render(request, 'services/account.html', {'customer': customer})


def account_info(request):
  
    customer = Customer.objects.first()

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('account_info')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'services/account.html', {
        'customer': customer,
        'form': form,
    }) 

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, CustomerForm  # Ensure both forms are imported
from .models import Customer

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the User object
            # Save additional information to the Customer model
            Customer.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                age=form.cleaned_data['age'],
                address=form.cleaned_data['address'],
                email=form.cleaned_data['email'],
                mobile_number=form.cleaned_data['mobile_number']
            )
            login(request, user)  # Log the user in
            return redirect('submit_request')  # Redirect to the submit dashboard
    else:
        form = RegistrationForm()
    return render(request, 'services/register.html', {'form': form})

@login_required
def account_info(request):
    customer = request.user.customer  # Fetch the logged-in user's customer profile
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('account_info')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'services/account.html', {'customer': customer, 'form': form})


