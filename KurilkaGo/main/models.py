from django.db import models

# Create your models here.
class Cigarette(models.Model):
    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    type_description = models.CharField(max_length=200)
    number = models.IntegerField()
    strength = models.CharField(max_length=50)
    flavor = models.CharField(max_length=50)
    nicotine_content = models.CharField(max_length=50)
    thickness = models.CharField(max_length=50)
    resin_content = models.CharField(max_length=50)
    filter_presence = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='cigarette_images/', null=True, blank=True)

class DisposableVape(models.Model):
    producer = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    number_pulls = models.IntegerField()
    number = models.IntegerField()
    strength = models.CharField(max_length=50)
    nicotine_content = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='disposable_vape_images/', null=True, blank=True)

class Heating(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    holder_charge = models.CharField(max_length=50)
    battery_charge = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    session_time = models.CharField(max_length=50)
    package = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='heating_images/', null=True, blank=True)

class Hookah(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField()
    height = models.CharField(max_length=50)
    width = models.CharField(max_length=50)
    hose_length = models.CharField(max_length=50)
    bulb_volume = models.CharField(max_length=50)
    material_flask = models.CharField(max_length=50)
    material_bowl = models.CharField(max_length=50)
    material_shaft = models.CharField(max_length=50)
    material_tube = models.CharField(max_length=50)
    connection_type = models.CharField(max_length=50)
    shaft_diameter = models.CharField(max_length=50)
    color_shaft = models.CharField(max_length=50)
    color_bowl = models.CharField(max_length=50)
    tubes_amount = models.IntegerField()
    # image = models.ImageField(upload_to='hookah_images/', null=True, blank=True)

class Liquid(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    capacity_liquid = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    atomizer = models.CharField(max_length=50)
    vape_refuel = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    capacity_battery = models.CharField(max_length=50)
    type_battery = models.CharField(max_length=50)
    type_charge = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='liquid_images/', null=True, blank=True)

class Vape(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    capacity_liquid = models.IntegerField()
    type = models.CharField(max_length=100)
    atomizer = models.CharField(max_length=100)
    vape_refuel = models.CharField(max_length=100)
    power = models.IntegerField()
    capacity_battery = models.IntegerField()
    type_battery = models.CharField(max_length=100)
    type_charge = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.BinaryField()
