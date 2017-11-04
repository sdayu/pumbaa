from flask import redirect, url_for, session
from flask_login import LoginManager, UserMixin, current_user
from flask_principal import Principal, Permission, RoleNeed, identity_loaded, UserNeed

from . import models

admin_permission = Permission(RoleNeed('admin'))
member_permission = Permission(RoleNeed('member'))
staff_permission = Permission(RoleNeed('staff'))
lecturer_permission = Permission(RoleNeed('lecturer'))
moderator_permission = Permission(RoleNeed('moderator'))
anonymous_permission = Permission(RoleNeed('anonymous'))

dashboard_permission = Permission(RoleNeed('admin'), RoleNeed('member'))

def init_acl(app):
    # initial login manager
    login_manager = LoginManager(app)

    # initial principal
    principals = Principal(app)
    admin_permission = Permission(RoleNeed('admin'))
    user_permission = Permission(RoleNeed('user'))

    @login_manager.user_loader
    def load_user(user_id):
        user = models.User.objects.with_id(user_id)
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

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('accounts.login'))
