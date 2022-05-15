from django.contrib.auth.models import User, Group, Permission
try:
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.first_name = 'John'
    user.last_name = 'Lennon'
    user.save()
except:
    pass

new_group, created = Group.objects.get_or_create(name='Viewable')
if created:
    todo_list_perm = Permission.objects.get(codename='todo_app.view_todolist')
    new_group.permissions.add(todo_list_perm)
    new_group.save()