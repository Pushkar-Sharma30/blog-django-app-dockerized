from django.contrib import admin
from .models import Blog, Category, Contact
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Contact)