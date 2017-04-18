from flask_login import current_user
from flask_principal import identity_loaded, RoleNeed, UserNeed, Permission

from . import app, login_manager
from . import models

admin_permission = Permission(RoleNeed('admin'))
member_permission = Permission(RoleNeed('member'))
staff_permission = Permission(RoleNeed('staff'))
lecturer_permission = Permission(RoleNeed('lecturer'))
moderator_permission = Permission(RoleNeed('moderator'))
anonymous_permission = Permission(RoleNeed('anonymous'))

dashboard_permission = Permission(RoleNeed('admin'), RoleNeed('member'))


@login_manager.user_loader
def load_user(userid):
    # Return an instance of the User model
    user = models.User.objects.with_id(userid)
    return user

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Set the identity user object
    identity.user = current_user

    # Add the UserNeed to the identity
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    # Assuming the User model has a list of roles, update the
    # identity with the roles that the user provides
    if hasattr(current_user, 'roles'):
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.name))
