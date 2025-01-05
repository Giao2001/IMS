from django.db import models
from django.utils import timezone


class Warehouse(models.Model):
    wh_code = models.CharField(max_length=20, primary_key=True)
    wh_name = models.CharField(max_length=100)
    wh_comment = models.CharField(max_length=500, blank=True)
    wh_bg = models.ImageField(upload_to='warehouse_images/')
    create_at = models.DateTimeField(default=timezone.now)
    create_by = models.DateTimeField(null=True)
    update_at = models.DateTimeField(default=timezone.now)
    update_by = models.DateTimeField(null=True)


class Area(models.Model):
    area_code = models.CharField(max_length=20, primary_key=True)
    area_name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    create_by = models.DateTimeField(null=True)
    update_at = models.DateTimeField(default=timezone.now)
    update_by = models.DateTimeField(null=True)


class Bin(models.Model):
    bin_code = models.CharField(max_length=20, primary_key=True)
    bin_name = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    pos_x = models.IntegerField(blank=True)
    pos_y = models.IntegerField(blank=True)
    create_at = models.DateTimeField(default=timezone.now)
    create_by = models.DateTimeField(null=True)
    update_at = models.DateTimeField(default=timezone.now)
    update_by = models.DateTimeField(null=True)


class Attribute(models.Model):
    attr_code = models.CharField(max_length=20, primary_key=True)
    attr_name = models.CharField(max_length=50)
    update_at = models.DateTimeField(default=timezone.now)
    update_by = models.DateTimeField(null=True)


class Bin_Attr_Value(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
    create_at = models.DateTimeField(default=timezone.now)
    create_by = models.DateTimeField(null=True)

