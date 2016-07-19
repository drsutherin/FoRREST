#!/usr/bin/python

import subprocess
import os
from plugins import *
import sys

from Model import Forrest_Model

class FoRREST:

    def __init__(self, filename=None):
        """
            Inits the class
        """
        # Change to not being hardcoded later
        self.operating_system = 'linux'
        self.current_file = filename
        self.raw = raw.Raw.Raw(self)
        self.extract = extract.Extract.Extract(self)
        self.interpret = interpret.Interpret.Interpret(self)
        self.transform = transform.Transform.Transform(self)
        self.infer = infer.Infer.Infer(self)
   
    def set_file(self, params):
        if type(params) == str:
            filename = params
        else:
            filename = params[0]
        
        if (os.path.isfile(filename)):
            self.current_file = filename
            return "[+] File %s successfully loaded" % self.current_file
        else:
            print "[-] That file does not exist!"
        
    
    def get_file(self, params = None):
        return self.current_file
        
    def get_raw(self, params = None):
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
        
    def get_extracted(self, params = None):
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
        
    def get_interpreted(self, params = None):
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

    def get_transformed(self, params = None):
	output = {}
	
	if self.current_file:
	    output['disassembly'] = self.transform.get_disassembly()
	    output['mnemonics'] = self.transform.get_mnemonics()
	    output['functions'] = self.transform.get_functions()
	    output['basic_blocks'] = self.transform.get_basic_blocks()
	    output['data_references'] = self.transform.get_data_references()
	    output['jump_targets'] = self.transform.get_jump_targets()
	else:
	    print "No file selected! Please select with",\
                "load [filename]"
	return output

    # Add test to make sure the file is loaded    
    def get_strings(self, params = None):
        output = self.interpret.get_strings()
        return output

    def help(self, params = None):
        with open('help.txt', 'r') as f:
            print f.read()

    def add_entry(self, params = None):
        return Forrest_Model.add_entry(self)

    def select(self, params = None):
        if type(params) == str:
            sha256sum = params
        else:
            if params is not None:
                sha256sum = params[0]
            else:
                if self.get_file():
                    sha256sum = self.raw.get_sha256()
                else:
                    print "No file selected yet!"

        entries = None

        if sha256sum:
            entries = Forrest_Model.select().where(
                Forrest_Model.sha256sum == sha256sum
            )

        return entries

    
    def _shell(self, commandName, args, stdin=None):
        """
            Make a call to the terminal and return the output.
        """
        cmd = [commandName]
        if type(args) == str:
            cmd.append(args)
        else:
            cmd.extend(args)
            
        #print 'running', cmd
        
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
            
        #print 'running', cmd
        
        if stdin:
            out = subprocess.Popen(cmd, stdin=stdin, stdout=subprocess.PIPE)
        else:
            out = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            
        return out.stdout

