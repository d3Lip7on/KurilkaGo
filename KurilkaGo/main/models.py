from django.db import models

# Create your models here.
class Cigarette(models.Model):
    title = models.TextField()
    producer = models.TextField()
    type = models.TextField()
    description = models.TextField()
    number = models.IntegerField()
    strength = models.TextField()
    flavor = models.TextField()
    nicotine_content = models.IntegerField()
    thickness = models.TextField()
    resin_content = models.IntegerField()
    filter_presence = models.IntegerField()
    price = models.FloatField()
    image = models.BinaryField()

    class Meta:
        db_table = 'cigarettes'  # Замените на фактическое имя вашей таблицы

    def __str__(self):
        return self.name

class DisposableVape(models.Model):
    producer = models.TextField()
    type = models.TextField()
    description = models.TextField()
    number_pulls = models.IntegerField()
    number = models.IntegerField()
    strength = models.TextField()
    nicotine_content = models.FloatField()
    image = models.BinaryField()
    price = models.FloatField()

    class Meta:
        db_table = 'disposable_vape'  # Замените на фактическое имя вашей таблицы

    def __str__(self):
        return self.name

class Heating(models.Model):
    title = models.TextField()
    description = models.TextField()
    holder_charge = models.FloatField()
    battery_charge = models.FloatField()
    weight = models.IntegerField()
    color = models.TextField()
    session_time = models.IntegerField()
    package = models.TextField()
    price = models.FloatField()
    image = models.BinaryField()

    class Meta:
        db_table = 'heating'  # Замените на фактическое имя вашей таблицы

    def __str__(self):
        return self.name

class Hookah(models.Model):
    title = models.TextField()
    brand = models.TextField()
    color = models.TextField()
    description = models.TextField()
    height = models.IntegerField()
    width = models.IntegerField()
    hose_length = models.IntegerField()
    bulb_volume = models.FloatField()
    material_flask = models.TextField()
    material_bowl = models.TextField()
    material_shaft = models.TextField()
    material_tube = models.TextField()
    connection_type = models.TextField()
    shaft_diameter = models.IntegerField()
    color_shaft = models.TextField()
    color_bowl = models.TextField()
    tubes_amount = models.IntegerField()
    image = models.BinaryField()
    price = models.FloatField()

    class Meta:
        db_table = 'hookahs'  # Замените на фактическое имя вашей таблицы

    def __str__(self):
        return self.name

class Liquid(models.Model):
    title = models.TextField()
    producer = models.TextField()
    type = models.TextField()
    strength = models.TextField()
    taste = models.TextField()
    nicotine_content = models.FloatField()
    volume = models.TextField()
    price = models.FloatField()
    image = models.BinaryField()

    class Meta:
        db_table = 'liquids'  # Замените на фактическое имя вашей таблицы

    def __str__(self):
        return self.name

class Vape(models.Model):
    title = models.TextField()
    description = models.TextField()
    capacity_liquid = models.IntegerField()
    type = models.TextField()
    atomizer = models.TextField()
    vape_refuel = models.TextField()
    power = models.IntegerField()
    capacity_battery = models.IntegerField()
    type_battery = models.TextField()
    type_charge = models.TextField()
    price = models.FloatField()
    image = models.BinaryField()

    class Meta:
        db_table = 'vapes'  # Замените на фактическое имя вашей таблицы

    def __str__(self):
        return self.name