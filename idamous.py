#!/usr/bin/python

import subprocess
import os
import sys

from importlib import import_module
from plugins import *

# from plugins.elf import elf

class Idamous:
	
	def __init__(self):
		"""
			Inits the class
		"""
		# Change to not being hardcoded later
		self.operating_system = 'linux'
		self.current_file = None
		self.result_directory = None
	
	def set_file(self, filename):
		self.current_file = filename
	
	def get_file(self):
		return self.current_file
	
	"""
	Provides interaction to select a file to load
	@param cmd: a list of strings in the form ['load', 'filename']
	"""
	def load_file(self, cmd):
                try:
			binary = cmd[1]
                        f = open(binary)
                        f.close()
                        # Creates a directory for the results of the Idamous tests
			idamous.set_file(binary)
		        if "." in binary:
         	        	splitFile = binary.split(".")[-2]
	                	splitFile = splitFile.split("/")[-1]
			else:
				splitFile = binary.split("/")[-1]

		        self.set_result_directory("./results/" + splitFile)
		        # This could be dangerous...
        		subprocess.Popen(["rm", "-rf", self.get_result_directory()])

		        subprocess.Popen(["mkdir", self.get_result_directory()])
			print "File %s successfully loaded" % binary

                except IOError:
                        print "File %s does not exist. Try again" % binary

	def set_result_directory(self, dir):
		self.result_directory = dir

	def get_result_directory(self):
		return self.result_directory

	def _call_shell_function(self, commandName, args):
		"""
			Make a call to the terminal and return the output.
		"""
		output = subprocess.check_output([commandName].extend(args))
		return output

	def basics(self):
		result = elf.elf.read_header(self)
		result += md5.md5.checksum(self)
		result += sha1.sha1.checksum(self)
		return result

	"""
	Get raw (level 0) data about the file.
	@param cmd: 	A list of strings in the form ["get_raw", "-etc"] where e, t, and c are placeholders for
			functionality we can add later, i.e. "-n" will only return the filename
	TODO:		Examine the rest of the list to determine (and then implement) options as described above
	"""
	def get_raw_data(self, cmd):
		 # Get raw data
	        raw_data = raw.File.File(self.get_file())

        	print 'Filename:', raw_data.get_name()
	        print 'File extension:', raw_data.get_extension()
		print 'File size:', raw_data.get_size()
	        print 'File inode:', raw_data.get_inode()
        	print 'File path:', raw_data.get_path()
	        print 'File MD5:', raw_data.get_md5()
	        print 'File SHA1:', raw_data.get_sha1()

	        raw_file = self.get_result_directory() + "/raw_data.txt"

	        # Open file to write raw data, create one if necessary
	        if not os.path.isfile(raw_file):
        	        subprocess.Popen(["touch", raw_file])
	        f = open(raw_file, "w")

	        f.write("Filename: %s\n" % raw_data.get_name())
	        f.write('File extension: %s\n' % raw_data.get_extension())
	        f.write('File size: %s\n' % raw_data.get_size())
	        f.write('File inode: %s\n' % raw_data.get_inode())
	        f.write('File path: %s\n' % raw_data.get_path())
	        f.write('File MD5: %s\n' % raw_data.get_md5())
	        f.write('File SHA1: %s\n' % raw_data.get_sha1())
        	f.close()

	        print "Raw data saved to %s" % raw_file

	"""
	Get extracted (level 1) data about the file.
        @param cmd:     A list of strings in the form ["get_extracted", "-etc"] where e, t, and c are placeholders for
                        functionality we can add later
        TODO:           Examine the rest of the list to determine (and then implement) options as described above
	"""
	def get_extracted_data(self, cmd):
		# Get extracted data and write to file
	        extracted_data = extract.Extract.Extract(idamous.get_file())

        	extracted_file = idamous.get_result_directory() + "/extracted_data.txt"
	        if not os.path.isfile(extracted_file):
        	        subprocess.Popen(["touch", extracted_file])
	        e = open(extracted_file, "w")

	        print 'Filetype:', extracted_data.get_filetype()
	        e.write('Filetype: %s\n' % extracted_data.get_filetype())

	     	print "Extracted data saved to %s" % extracted_file
	        e.close()

	def get_interpreted_data(self, cmd):
		interpreted_file = idamous.get_result_directory() + "/interpreted_data.txt"
		if not os.path.isfile(interpreted_file):
                        subprocess.Popen(["touch", interpreted_file])
                i = open(interpreted_file, "w")

		interpreted_data = interpret.Interpret.Interpret(self.get_file())
		
		print 'Strings: %s' % interpreted_data.get_strings(self.get_file())
		i.write('Strings: %s\n' % interpreted_data.get_strings(self.get_file()))

		print 'Header Information: %s' % interpreted_data.get_header(self.get_file())
		i.write('Header Information: %s' % interpreted_data.get_header(self.get_file()))
		
		print 'Imports: %s' % interpreted_data.get_imports(self.get_file())
		i.write('Imports: %s' % interpreted_data.get_imports(self.get_file()))
		
		print 'Opcodes: %s' % interpreted_data.get_opcodes(self.get_file())
		i.write('Opcodes: %s' % interpreted_data.get_opcodes(self.get_file()))
		

# If you call idamous.py, run this.
if __name__ == '__main__':

	print 'Creating idamous instance'
	idamous = Idamous()
	
	# Primary control loop
	print ""
	print "IDAMOUS:  Integrated Framework for Reverse Engineering Software"
	print "---------------------------------------------------------------"
	print "Begin by loading your binay with the 'load [yourfile]' command."
	print "Type 'help' to see all available commands!"
	print ""
	
	#shorten the commands at some point for easier use
	#a command history function would be very nice but not a necessity
	while True:
		sys.stdout.flush()
		sys.stdout.write("idamous->")
		sys.stdout.flush()
		cmd = raw_input()
		cmd = cmd.lower()
		cmd = cmd.split(" ")
		
		print "cmd[0] is: %s" % cmd[0]
		if idamous.get_file() == None and not (cmd[0] == "load" or cmd[0] == "exit" or cmd[0] == "help"):
			print "No file loaded. Use 'load' command"

		elif cmd[0] == "get_extracted":
			idamous.get_extracted_data(cmd)

		elif cmd[0] == "get_interpreted":
			idamous.get_interpreted_data(cmd)

		elif cmd[0] == "get_raw":
			idamous.get_raw_data(cmd)

		elif cmd[0] == "help":
			f = open("help.txt")
			for line in f:
				print line
			f.close()

		elif cmd[0] == "load":
			idamous.load_file(cmd)
		
		# 'quit' does not seem to work before a file is loaded while exit does
		elif cmd[0] == "quit" or cmd[0] == "exit":
			print "Thanks for using Idamous!"
			break;
		else:
			print "Command not recognized. Try again or type 'help'."

