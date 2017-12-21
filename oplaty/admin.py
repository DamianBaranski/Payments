from django.contrib import admin
from .models import Account, Obligation, Supplier, Material, Bill, Income

admin.site.register(Account)
admin.site.register(Obligation)
admin.site.register(Supplier)
admin.site.register(Material)
admin.site.register(Bill)
admin.site.register(Income)
# Register your models here.
