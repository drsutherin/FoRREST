
from FoRREST import FoRREST
import subprocess
import os
import sys

# Adds a history function to the cli interface
import readline

def display_help(params = []):
    forrest = FoRREST()
    if len(params) is 0:
        print ""
        print "FoRREST: A Framework of Robust Reverse Engineering Software Tools"
        print "---------------------------------------------------------------"
        print "Run, FoRREST, run!"
        print "---------------------------------------------------------------"
        print "Begin by loading your binay with the 'load [yourfile]' command."
        print "Type 'ls' to see all available commands!"
        print ""
    elif len(params) is 1 and params[0] == "ls":
        # Get all functions that don't start with _ and print them out.
        for func in [func for func in dir(FoRREST) if not func.startswith("_")]:
            print func
	for func in [func for func in dir(forrest.raw) if not func.startswith("_")]:
	    if func != "forrest" and func != "select":
	    	print func
	for func in [func for func in dir(forrest.extract) if not func.startswith("_")]:
	    if func != "forrest" and func != "select":
	    	print func
	for func in [func for func in dir(forrest.interpret) if not func.startswith("_")]:
	    if func != "forrest" and func != "select":
	    	print func
	for func in [func for func in dir(forrest.transform) if not func.startswith("_")]:
	    if func != "forrest" and func != "select":
	    	print func
	for func in [func for func in dir(forrest.infer) if not func.startswith("_")]:
	    if func != "forrest" and func != "select":
	    	print func
	
def get_cmd(cmd = None):
    if not cmd:
        cmd = raw_input("FoRREST> ").split()
    else:
        cmd = cmd.split()

    func = cmd[0]
    params = cmd[1:]

    if func == "load": func = "set_file"
    if func == "ls":
        func = "help"
        params = ["ls"]

    return func, params

def run_func(forrest, func, params):
    return_value = ""

    is_obj = False

    if func in dir(forrest):
                fun = getattr(forrest, func)

                try:
                    if is_obj:
                        fun = getattr(fun, method)                        
                        print fun()
                    else:
                        print fun(params)
                except Exception as e:
                    print '[-] function failed to run.'
                    print e

    # Elifs allow users to call plugin functions directly from the command line
    # There's probably a short/cleaner way to do this, but this works -DS 7/8

    # Gives access to Raw functions
    elif func in dir(forrest.raw):
        fun = getattr(forrest.raw, func)
        try:
            return_value = fun()
        except Exception as e:
            print "[-] Raw function failed to run."
            print e

    # Gives access to Extract functions
    elif func in dir(forrest.extract):
        fun = getattr(forrest.extract, func)
        try:
            return_value = fun()
        except Exception as e:
            print "[-] Extracted function failed to run."
            print e

    # Gives access to Interpret functions
    elif func in dir(forrest.interpret):
        fun = getattr(forrest.interpret, func)
        try:
            return_value = fun()
        except Exception as e:
            print "[-] Interpreted function failed to run."
            print e

    # Gives access to Transform functions
    elif func in dir(forrest.transform):
        fun = getattr(forrest.transform, func)
        try:
            return_value = fun()
        except Exception as e:
            print "[-] Transformed function failed to run."
            print e

    # Gives access to Infer functions
    elif func in dir(forrest.infer):
        fun = getattr(forrest.infer, func)
        try:
            print fun()
        except Exception as e:
            print "[-] Inferred function failed to run."
            print e

    else:
        print "[-] That command does not exist!"

    return return_value

def shell(forrest = FoRREST(), should_display_help = True):
    if should_display_help: display_help()

    should_continue = True

    quit = [
        'quit',
        'exit'
    ]

    while should_continue:
        func, params = get_cmd()

        if func in quit:
            should_continue = False
        elif func == "help":
            display_help(params)
        else:
            print run_func(forrest, func, params)

def test_forrest(test_file):
    forrest = FoRREST()
    forrest.set_file(test_file)

    print "\nRaw Data:"
    print forrest.get_raw()

    print "\nExtracted Data:"
    print forrest.get_extracted()

    print "\nInterpreted Data:"
    print forrest.get_interpreted()

if __name__ == '__main__':
    # Example: ['main.py', '-c', 'load filename', 'get_extracted']
    # Removes main.py
    args = sys.argv[1:]
    filename = 0

    if len(args) is 0:
        shell()
    elif len(args) is 1 and args[filename].lower()[0] != "-":
        print 'Running FoRREST test on {}.'.format(args[filename])
        test_forrest(args[filename])
    elif args[filename].lower() == "-c":
        forrest = FoRREST()

        # Go through each string and treat the string as an entry
        # and run it.
        for shell_command in args[1:]:
            func, params = get_cmd(shell_command)
            print run_func(forrest, func, params)
    elif args[filename].lower() == "-d" or args[filename].lower() == "-e":
        forrest = FoRREST()

        # Treat arguments like names of files.
        # Pretend like each file is a pre-defined
        # list of shell commands.
        for filename in args[1:]:
            if os.path.isfile(filename):
                with open(filename, 'r') as f:
                    temp = f.read().splitlines()
                    for line in temp:
                        line = line.strip()
                        if line:
                            func, params = get_cmd(line)
                            print run_func(forrest, func, params)
            else:
                print "[-] ERROR:", filename, "is not a file!"

        if args[0].lower() == "-d": shell(forrest, False)
