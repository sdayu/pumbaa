import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_mako',
    'pyramid_debugtoolbar',
    'pyramid_beaker',
    'waitress',
    'mongoengine',
    'velruse',
    'pycrypto',
    'wtforms',
    'feedformater'
    ]

from pumbaa import __version__

setup(name='pumbaa',
      version=__version__,
      description='pumbaa community site',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pumbaa",
      entry_points="""\
      [paste.app_factory]
      main = pumbaa:main
      [console_scripts]
      initialize_pumbaa_db = pumbaa.scripts.initializedb:main

      """,
      )
