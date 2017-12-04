import cloudpickle
import sys

class Foo1(object):
    def __init__(self):
        pass

print("")
print("*****************************************")
cpversion = cloudpickle.__version__
print ("cloudpickle version: %s" % cpversion)
try:
	serialized1 = cloudpickle.dumps(Foo1)
#	print("Serialized1: ", serialized1)
	Foo2 = cloudpickle.loads(serialized1)
	serialized2 = cloudpickle.dumps(Foo2)
#	print("Serialized2: ", serialized2)
	print("")
	assert serialized1 == serialized2, "serialisations don't match"
	print ("assertion passed")
except Exception as err:
	print ("ASSERTION FAILED", err)

