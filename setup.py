try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'realize "cat" command',
    'author': 'Murphian',
    'url': 'XXXXXXXXXX',
    'download_url': 'XXXXXXXXXXXXX',
    'author_email': 'murphianx@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex5'],
    'scripts': [],
    'name': 'ex5'
}

setup(**config)