
def is_admin(user):
    return user.groups.filter(name='admin_gp') 

def is_member(user):
    return user.groups.filter(name='members') 

def is_admin_users(user):
    return user.groups.filter(name='admin_user_gp') 

def is_admin_items(user):
    return user.groups.filter(name='admin_item_gp') 


