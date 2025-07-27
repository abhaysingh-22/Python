# now i want to print that method written in hello_chai.py

from hello_chai import chai
import sys

name = "singh"
print("Ref count before: ", sys.getrefcount(name))

chai("singh")
print("Ref count after: ", sys.getrefcount(name))