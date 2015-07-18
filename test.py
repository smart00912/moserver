import os
import sys
AUTO_PLATFORM = 'test'
sysdir = os.path.abspath(os.path.dirname(__file__))
print '|'.join((sysdir,'modules/'+AUTO_PLATFORM))

