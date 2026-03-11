# # import imp
# # import os
# # import sys


# # sys.path.insert(0, os.path.dirname(__file__))

# # wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
# # application = wsgi.application

# from config.wsgi import application


# ///////////////////////////////////////

# import importlib.machinery
# import importlib.util
# import os
# import sys


# sys.path.insert(0, os.path.dirname(__file__))

# def load_source(modname, filename):
#     loader = importlib.machinery.SourceFileLoader(modname, filename)
#     spec = importlib.util.spec_from_file_location(modname, filename, loader=loader)
#     module = importlib.util.module_from_spec(spec)
#     loader.exec_module(module)
#     return module

# wsgi = load_source('wsgi', 'passenger_wsgi.py')
# application = wsgi.application

# ///////////////////
import os
import sys

# Add project path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

