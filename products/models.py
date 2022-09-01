from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255, null=False, blank=False ,unique=True)
    category_image = models.ImageField(null=True,  default='images/default.png', upload_to='images/')
    class Meta:
        db_table='Category'
        verbose_name="Category"
        verbose_name_plural='Categories'
