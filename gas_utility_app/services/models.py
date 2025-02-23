from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default="")
    age = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    total_orders = models.PositiveIntegerField(default=0)
    pending_orders = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.full_name
    

class ServiceRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('order_gas', 'Order Gas'),
        ('buy_non_domestic_gas', 'Buy Non-Domestic Gas'),
        ('subsidy_voluntarily', 'Subsidy Voluntarily'),
        ('locate_distributor', 'Locate Distributor'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    request_type = models.CharField(max_length=50, choices=REQUEST_TYPE_CHOICES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Service Request - {self.get_request_type_display()}"
    
