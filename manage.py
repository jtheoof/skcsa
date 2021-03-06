#!/usr/bin/env python
import sys

from django.core.management import execute_manager
try:
    import os
    path = os.path.abspath(os.path.split(__file__)[0])
    sys.path.append(path)
except ImportError:
    sys.stderr.write("Error: not able to append the directory containing %s to the system path\n" % __file__)
    sys.exit(1)
try:
    from settings import development# Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(development)
