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

    #returns the programs header information from the binary    
    def get_elf(self):
	output = subprocess.Popen(['objdump', '-h' , binary], stdout = subprocess.PIPE)
	output, error = output.communicate()
	return output
    
    #def get_imports(self):
    
    
    #def get_exports(self):
    
    
    #def get_opcodes(self):
