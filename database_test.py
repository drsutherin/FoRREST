
from Idamous import Idamous

# If you call idamous.py, run this.
if __name__ == '__main__':
    idamous = Idamous('test_binaries/custom_binaries/gen_fib.o')
    idamous.raw.add_entry()
