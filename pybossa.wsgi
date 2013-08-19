# Check the official documentation http://flask.pocoo.org/docs/deploying/mod_wsgi/
# Activate the virtual env (we assume that virtualenv is in the env folder)
activate_this = '/srv/pybossa/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
# Import sys to add the path of PyBossa
import sys
sys.path.insert(0,'/srv/pybossa/pybossa')
sys.path.insert(0,'/srv/pybossa')
# Run the web-app
import skybossa.chimpbossa
from pybossa.web import app as application
