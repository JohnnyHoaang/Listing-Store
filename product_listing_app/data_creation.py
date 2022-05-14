from product_listing_app.models import Post
from datetime import date

print("Adding data to db")
# Need protections against adding the same person twice

if Post.objects.filter(title='Dora').count() == 0:
    our_vac = Post(title='Our vacation')
    our_vac.save()
    
