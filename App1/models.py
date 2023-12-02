from django.db import models

# Create your models here.
class customer(models.Model):
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=10)
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=20)
    Place=models.CharField(max_length=30)
    Phone=models.IntegerField()
    Email=models.EmailField()
    class Meta:
        db_table="customer"

class food(models.Model):
    Food_name=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    Category_id=models.IntegerField()
    Price=models.CharField(max_length=20)
    class Meta:
        db_table="food"

class tables(models.Model):
    Table_name=models.CharField(max_length=50)
    chair_count=models.IntegerField()
    Size=models.CharField(max_length=30)
    Time=models.TimeField()
    Price=models.CharField(max_length=30)
    Image=models.ImageField()
    class Meta:
        db_table="tables"

class foodBooking(models.Model):
    Food_id=models.IntegerField()
    Quantity=models.IntegerField()
    Total=models.IntegerField()
    class Meta:
        db_table="foodBooking"

class tableBooking(models.Model):
    Table_id=models.IntegerField()
    Table_name=models.CharField(max_length=50)
    Time=models.TimeField()
    Amount=models.CharField(max_length=30)
    class Meta:
        db_table="tableBooking"

class payment(models.Model):
    Booking_id=models.IntegerField()
    Amount=models.CharField(max_length=30)
    User_id=models.CharField(max_length=20)        