from django.db import models
from django.contrib.auth.models import User


STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam' , 'Assam'),
    ('Bihar' , 'Bihar'),
    ('Chhattisgarh' , 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat' , 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh' , 'Himachal Pradesh' ),
    ('Jharkhand' , 'Jharkhand'),
    ('Karnataka' , 'Karnataka'),
    ('Kerala' , 'Kerala'),
    ('Maharashtra' , 'Maharashtra'),
    ('Madhya Pradesh' , 'Madhya Pradesh'),
    ('Manipur' , 'Manipur'),
    ('Meghalaya' , 'Meghalaya'),
    ('Mizoram' , 'Mizoram'),
    ('Nagaland' , 'Nagaland'),
    ('Odisha' , 'Odisha'),
    ('Punjab' , 'Punjab'),
    ('Rajasthan' , 'Rajasthan'),
    ('Sikkim' , 'Sikkim'),
    ('Tamil Nadu' , 'Tamil Nadu'),
    ('Tripura' , 'Tripura'),
    ('Telangana' , 'Telangana'),
    ('Uttar Pradesh' , 'Uttar Pradesh'),
    ('Uttarakhand' , 'Uttarakhand'),
    ('West Bengal' , 'West Bengal'),
    ('Andaman & Nicobar Islands' , 'Andaman & Nicobar Islands'),
    ('Chandigarh' , 'Chandigarh'), 
    ('Dadra & Nagar Haveli and Daman & Diu' , 'Dadra & Nagar Haveli and Daman & Diu'),
    ('Delhi' , 'Delhi'),
    ('Jammu & Kashmir' , 'Jammu & Kashmir'),
    ('Ladakh' , 'Ladakh'),
    ('Lakshadweep' , 'Lakshadweep'),
    ('Puducherry' , 'Puducherry'),

)


CATEGORY_CHOICES=(
    ('AIC', 'Amul Ice Cream'),
    ('DRIC', 'DoubleRainbow Ice Cream'),
    ('VLIC', 'Valdilal Ice Cream'),
    ('BRIC','BaskinRobbins Ice Cream'),
    ('BBIC', 'BlueBunny Ice Cream'),
    ('CMIC', 'CargillsMagic Ice Cream'),
    ('CBIC', 'CreamBell Ice Cream'),
    ('CSIC', 'CreamStone Ice Cream'),
    ('HIC', 'Havmor Ice Cream'),
    ('MDIC', 'Mother Diary Ice Cream'),
    
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    product_image = models.ImageField(upload_to='product')
    
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode= models.IntegerField()
    state= models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
    
STATUS_CHOICES = (
    ('Accepted' , 'Accepted'),
    ('Packed' , 'Packed'),
    ('On the Way' , 'On the Way'),
    ('Delivered' , 'Delivered'),
    ('Cancel' , 'Cancel'),
    ('Pending' , 'Pending'),
)
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)  
    def __str__(self):
        return self.name  
