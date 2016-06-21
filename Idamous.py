#!/usr/bin/python

import subprocess
import os
from plugins import *
import sys

class Idamous:
    
    def __init__(self):
        """
            Inits the class
        """
        # Change to not being hardcoded later
        self.operating_system = 'linux'
        self.current_file = None
        self.raw = raw.File.File(self)
        self.extract = extract.Extract.Extract(self)
        self.interpret = interpret.Interpret.Interpret(self)
    
    def set_file(self, params):
        if type(params) == str:
            filename = params
        else:
            filename = params[0]
        
        if (os.path.isfile(filename)):
            self.current_file = filename
        else:
            print "[-] That file does not exist!"
        
    
    def get_file(self, params = None):
        return self.current_file
        
    def get_raw_data(self, params = None):
        output = {}

        if self.current_file:
            output['name'] = self.raw.get_name()
            output['extension'] = self.raw.get_extension()
            output['size'] = self.raw.get_size()
            output['md5'] = self.raw.get_md5()
            output['sha1'] = self.raw.get_sha1()
            output['sha256'] = self.raw.get_sha256()
        else:
            print "No file selected! Please select with",\
                "load [filename]"

        return output
        
    def get_extracted_data(self, params = None):
        output = {}
        
        if self.current_file:
            output['type'] = self.extract.get_filetype()
            output['version'] = self.extract.get_version()
            output['architecture'] = self.extract.get_architecture()
            output['compiler'] = self.extract.get_compiler()
            output['sections'] = self.extract.get_sections()
        else:
            print "No file selected! Please select with",\
                "load [filename]"
        
        return output
        
    def get_interpreted_data(self, params = None):
        output = {}
        
        if self.current_file:
            output['opcodes'] = self.interpret.get_opcodes()
            output['strings'] = self.interpret.get_strings()
            output['imports'] = self.interpret.get_imports()
            output['exports'] = self.interpret.get_exports()
            output['header_information'] = self.interpret.get_header_information()
        else:
            print "No file selected! Please select with",\
                "load [filename]"
        
        return output
        
    def get_help(self, params = None):
        with open('help.txt', 'r') as f:
            print f.read()
    
    def _shell(self, commandName, args, stdin=None):
        """
            Make a call to the terminal and return the output.
        """
        cmd = [commandName]
        if type(args) == str:
            cmd.append(args)
        else:
            cmd.extend(args)
            
        print 'running', cmd
        
        if stdin:
            out, err = subprocess.Popen(cmd, stdin=stdin, stdout=subprocess.PIPE).communicate()
        else:
            out, err = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()
        
        if out: out = out.splitlines()
        if err: err = err.splitlines()
        
        return out, err
        
    def _shell_std(self, commandName, args, stdin=None):
        """
            Make a call to the terminal and return the output.
        """
        cmd = [commandName]
        if type(args) == str:
            cmd.append(args)
        else:
            cmd.extend(args)
            
        print 'running', cmd
        
        if stdin:
            out = subprocess.Popen(cmd, stdin=stdin, stdout=subprocess.PIPE)
        else:
            out = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            
        return out.stdout
        

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
            if len(sys.argv) >= 3:
                idamous = Idamous()
                idamous.set_file('test_binaries/custom_binaries/generate_fib.out')
                print idamous.get_raw_data()
                print idamous.get_extracted_data()
                print idamous.get_interpreted_data()
            else:
                idamous = Idamous()
                idamous.set_file(sys.argv[1])
                print idamous.get_raw_data()
                print idamous.get_extracted_data()
                print idamous.get_interpreted_data()
    else:
        start_shell()
    # idamous = Idamous()
    # idamous.set_file('test_binaries/custom_binaries/generate_fibb.out')
    # print idamous.get_raw_data()
    # print idamous.get_extracted_data()
    # print idamous.get_interpreted_data()
