import django
import os

os.environ['DJANGO_SETTINGS_MODULE']='product_listing_project.settings'
django.setup()
from django.contrib.auth.models import Group, User, Permission


add_user_perms = Permission.objects.get(name='Can add user')
print(add_user_perms)
delete_user_perms = Permission.objects.get(name='Can delete user')
view_user_perms = Permission.objects.get(name='Can view user')
add_post_perms = Permission.objects.get(name='Can add post')
change_post_perms= Permission.objects.get(name='Can change post')
delete_post_perms = Permission.objects.get(name='Can delete post')
view_post_perms = Permission.objects.get(name='Can view post')
add_group_perms = Permission.objects.get(name='Can add group')
change_group_perms = Permission.objects.get(name='Can change group')
delete_group_perms = Permission.objects.get(name='Can delete group')
view_group_perms = Permission.objects.get(name='Can view group')

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
    permissions = [add_user_perms, delete_user_perms, view_user_perms]
    admin_users.permissions.set(permissions) 
if Group.objects.filter(name="admin_item_gp").count() == 0:
    admin_items = Group(name="admin_item_gp", id=2)
    admin_items.save()
    permissions = [add_user_perms, delete_user_perms, view_user_perms, 
                    add_post_perms, change_post_perms, delete_post_perms, view_post_perms]
    admin_items.permissions.set(permissions)
if Group.objects.filter(name="admins").count() == 0:
    admins = Group(name="admins", id=3)
    admins.save()
    permissions = [add_user_perms, delete_user_perms, view_user_perms, 
                    add_post_perms, change_post_perms, delete_post_perms, view_post_perms,
                    add_group_perms, change_group_perms, delete_group_perms, view_group_perms]
    admins.permissions.set(permissions)
    if User.objects.filter(username="Instructor").count() == 0:
        user = User.objects.create_user('Instructor', 'instructor@gmail.com', 'Python420')
        user.save()
        g = Group.objects.get(name='admins')
        g.user_set.add(user)

# print(Permission.objects.all().values('name'))
users = User.objects.all().values('username', 'groups__name')

# sets users without groups to members
no_members =users = User.objects.filter(groups__name=None)
g = Group.objects.get(name='members')
for member in no_members:
    g.user_set.add(member)
