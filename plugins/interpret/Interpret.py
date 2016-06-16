import subprocess
import os

class Interpret:
    
    def __init__(self, filename):
	self.filename = filename
        self.file = None

    #returns the strings from the binary
    def get_strings(self, binary):       
	output = subprocess.Popen(['strings', binary], stdout=subprocess.PIPE)
	output, error = output.communicate()
        return output

    #returns the programs header information from the binary,-h just gets the sections can change to -x to get all header section information    
    def get_header(self, binary):
	output = subprocess.Popen(['objdump', '-h' , binary], stdout = subprocess.PIPE)
	output, error = output.communicate()
	return output

    #returns the imported librarys from the binary
    def get_imports(self, binary):
	output = subprocess.Popen(['ldd', binary], stdout = subprocess.PIPE)
	output, error = output.communicate()
	return output
    	
    #def get_exports(self, binary):
    

    #returns the opcodes from teh binary
    def get_opcodes(self, binary):
	output = subprocess.Popen(['objdump', '-D', binary], stdout = subprocess.PIPE)
	output, error = output.communicate()
	return output
