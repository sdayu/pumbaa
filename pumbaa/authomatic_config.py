from authomatic.providers import oauth2, oauth1

CONFIG = {

    'twiter': { # Your internal provider name

        # Provider class
        'class_': oauth1.Twitter,

        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': '',
        'consumer_secret': '',
    },
    'facebook': {
        'class_': oauth2.Facebook,
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '',
        'consumer_secret': '',
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email'],
    }

}

