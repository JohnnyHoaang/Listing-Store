from django.contrib import admin
from product_listing_app.models import Post, Comment,Rating, AzureImage
from django.contrib import admin
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(AzureImage)
