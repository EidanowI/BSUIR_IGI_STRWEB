from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

# Create your models here.
User = get_user_model()

class Profile(models.Model):
    USER_ROLES=[
        {'customer', 'Customer'},
        {'admin','Admin'},
        {'worker', 'Worker'},
        
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
   
    phone_number = models.CharField("User contact phone number", max_length=13,default=0)
    id_user = models.IntegerField()
    address = models.CharField("User full address", max_length=200, default=0)
    role = models.CharField(max_length=20, choices=USER_ROLES)
    orders = models.FloatField(default=0)
    age = models.PositiveIntegerField(default=1)
    def str(self):
        return f'{self.user.username} - {self.role}'
    


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)    
    description = models.TextField(max_length=700, null=False, blank=False)
    price = models.FloatField(validators=[MinValueValidator(0.1)], blank=False, null=False)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Vacancy(models.Model):
    title = models.CharField(max_length=100, null= False)
    description = models.TextField(max_length=400, null = False)

class Coupons(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=100, null=False)
    number = models.CharField(max_length=20, null=False)
    active = models.BooleanField(default=True, verbose_name='Активный')

class Contacts(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=100, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    email = models.EmailField(null= False)
    image = models.ImageField(null = False, default="news1.jpg")

class News(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=100, null=False)
    image = models.ImageField(default="news1.jpg",null = False)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Review by {self.user.username}"
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    answer_date = models.DateField(auto_now_add=True)

    def str(self):
        return self.question
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    address = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
class Member(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
