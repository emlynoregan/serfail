

import sys
import time
import imp
import os

from subprocess import call

print ("python version: %s" % (tuple(sys.version_info), ))

with open("/dev/null","w") as devnull:

	returncode = call(["python3", "-m", "pip", "install", "cloudpickle==0.5.2"], stdout=devnull)

	while not returncode:
		import cloudpickle
		imp.reload(cloudpickle)
		cpversion = cloudpickle.__version__
#		print ("outer: cloudpickle version: %s" % cpversion)

		call(["python3", "./serfailinner.py"])


		returncode = call(["python3", "-m", "pip", "install", "cloudpickle<" + cpversion], stdout=devnull)

