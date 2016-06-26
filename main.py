
from Idamous import Idamous
import subprocess
import os
import sys

def start_shell():
    print ""
    print "IDAMOUS:  Integrated Framework for Reverse Engineering Software"
    print "---------------------------------------------------------------"
    print "Begin by loading your binay with the 'load [yourfile]' command."
    print "Type 'help' to see all available commands!"
    print ""
    
    idamous = Idamous()
    
    should_continue = True
    quit = [
        'quit',
        'exit'
    ]
    
    while should_continue:
        cmd = raw_input("Idamous> ")
    
        if cmd.lower() in quit:
            should_continue = False
        else:
            func = cmd.split()[0]
            params = cmd.split()[1:]
            
            if func == "help": func = "get_help"
            if func == "load": func = "set_file"
            
            obj = False
            
            if func[0] == '&':
                obj = True
                temp = func[1:].split('.', 1)
                if len(temp) > 1:
                    func = temp[0]
                    method = temp[1]
                else:
                    print '[-] Error: Please provide a method.'
                    continue

            if func in dir(idamous):
                fun = getattr(idamous, func)
                
                try:
                    if obj:
                        fun = getattr(fun, method)
                        
                        print fun()
                    else:
                        print fun(params)
                except Exception as e:
                    print '[-] function failed to run.'
                    print e
            else:
                print "[-] That command does not exist!"

# If you call idamous.py, run this.
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if len(sys.argv) >= 4 and sys.argv[1].lower() == "-c":
            idamous = Idamous()
            idamous.set_file(sys.argv[2])
            
            cmd = sys.argv[3]
            func = cmd.split()[0]
            params = cmd.split()[1:]
            
            if func == "help": func = "get_help"
            if func == "load": func = "set_file"
            
            obj = False
            
            if func[0] == '&':
                obj = True
                temp = func[1:].split('.', 1)
                if len(temp) > 1:
                    func = temp[0]
                    method = temp[1]
                else:
                    print '[-] Error: Please provide a method.'
                    exit(0)

            if func in dir(idamous):
                fun = getattr(idamous, func)
                
                var = None
                
                try:
                    if obj:
                        fun = getattr(fun, method)
                        
                        var = fun()
                    else:
                        var = fun(params)
                except Exception as e:
                    print '[-] function failed to run.'
                    print e
                    
                if var:
                    if type(var) == str:
                        print var
                    else:
                        for x in var:
                            print x
            else:
                print "[-] That command does not exist!"
        else:
            temp_file = 'test_binaries/custom_binaries/generate_fib.out'
            
            if len(sys.argv) >= 3:
                pass
            else:
                temp_file = sys.argv[1]
            
            idamous = Idamous()
            idamous.set_file(temp_file)
            print idamous.get_raw_data()
            print idamous.get_extracted_data()
            print idamous.get_interpreted_data()
    else:
        start_shell()
