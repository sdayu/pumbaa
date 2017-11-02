from flask import redirect, url_for, session
from flask_login import LoginManager, UserMixin
from flask_principal import Principal, Permission, RoleNeed

class User(UserMixin):
    def __init__(self, **kwargs):
        self.data = kwargs

    def __setattr__(self, name, value):
        if name in ['data']:
            self.__dict__[name] = value
        else:
            if '_' in name:
                name = name.replace('_', '-')
            self.data[name] = value

    def __getattr__(self, name):
        nname = name.replace('_', '-')

        if nname in self.data:
            return self.data[nname]

        if name in self.__dict__:
            return self.__dict__[name]

        raise AttributeError(name)


def init_acl(app):
    # initial login manager
    login_manager = LoginManager(app)

    # initial principal
    principals = Principal(app)
    admin_permission = Permission(RoleNeed('admin'))
    user_permission = Permission(RoleNeed('user'))

    @login_manager.user_loader
    def load_user(user_id):
        if 'user' not in session:
            return
        user = User(**session['user'])
        user.token = session.get('token', None)
        return user

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('accounts.login'))
