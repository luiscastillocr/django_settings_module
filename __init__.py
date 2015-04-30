import os
ENV = os.getenv('ENV')

print "LOADING %s SETTINGS" % ENV
exec('from %s import *' % ENV)
