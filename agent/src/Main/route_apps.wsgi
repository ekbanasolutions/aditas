#!/usr/bin/python3.5

import sys
sys.path.insert(0, '/var/www/bigdata_services/Main')

from route_apps import app as application
from route_apps import main

main()