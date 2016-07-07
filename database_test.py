
from FoRREST import FoRREST

# If you call forrest.py, run this.
if __name__ == '__main__':
    forrest = FoRREST('test_binaries/custom_binaries/gen_fib.o')
    forrest.raw.add_entry()
