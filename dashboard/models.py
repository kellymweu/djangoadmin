from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#this is a tupple
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY , null=True)
    quantity = models.PositiveIntegerField(null=True)

    #make the name appear in singular instead of the default plural
    class Meta:
        verbose_name_plural = 'Product'

    #String representation of the db in admin space
    def __str__(self) -> str:
        return f'{self.name}-{self.category}-{self.quantity}'
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    #make the name appear in singular instead of the default plural
    class Meta:
        verbose_name_plural = 'Order'

    #String representation of the db in admin space
    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'