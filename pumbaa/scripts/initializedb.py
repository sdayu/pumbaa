import os
import sys

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from pumbaa import models
from pumbaa import crypto

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    models.initial(settings)
    
    role_names = ['admin', 'lecturer', 'staff', 'moderator', 'member', 'anonymous']
    
    for rname in role_names:
        role = models.Role.objects(name=rname).first()
        if not role:
            role = models.Role(name=rname)
            role.save()
            print('add role:', rname)
            
    adminuser = 'admin'
    adminpass = 'adminadmin'
    
    admin = models.User.objects(username=adminuser).first()
    sm = crypto.SecretManager(settings.get('pumbaa.secret'))
    if admin is None:
        admin = models.User(username=adminuser)
        admin.first_name = 'Administrator'
        admin.last_name = 'CoE'
        admin.display_name = 'Administrator'
        admin.status = 'activate'
        admin.email = 'admin@pumbaa.coe.psu.ac.th'
        admin.password = sm.get_hash_password(adminpass)
        admin.roles.append(models.Role.objects(name='admin').first())
        admin.save()
        
        print('add admin user:', adminuser)

