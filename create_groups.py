import django
import os

os.environ['DJANGO_SETTINGS_MODULE']='product_listing_project.settings'
django.setup()


from django.contrib.auth.models import Group, User, Permission
if Group.objects.filter(name="members").count() == 0:
    members = Group(name="members", id=0)
    members.save()
    g = Group.objects.get(name='members')
    users = User.objects.all()
    for u in users:
        g.user_set.add(u)
if Group.objects.filter(name="admin_user_gp").count() == 0:
    admin_users = Group(name="admin_user_gp", id=1)
    admin_users.save()
    perms = Permission.objects.filter(name='Can add user group')
    perms2 = Permission.objects.filter(name='Can delete user group')
    perms3 = Permission.objects.filter(name='Can view user group')
    admin_users.permissions.set(perms)
    admin_users.permissions.set(perms2)
    admin_users.permissions.set(perms3)
    # cant set many permissions 
if Group.objects.filter(name="admin_item_gp").count() == 0:
    admin_items = Group(name="admin_item_gp", id=2)
    admin_items.save()
if Group.objects.filter(name="admins").count() == 0:
    admins = Group(name="admins", id=3)
    admins.save()
print(Permission.objects.all().values('name'))
