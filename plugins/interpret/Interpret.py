import subprocess
import os

class Interpret:
    
    def __init__(self, filename):
	self.filename = filename
        self.file = None

    #returns the strings from the binary
    def get_strings(self, binary):       
	output = subprocess.Popen(['strings', binary], stdout=subprocess.PIPE).communicate()[0]
        return output
    
    #returns the elfheader from the binary    
    #def get_elf(self):

    
    #def get_imports(self):
    
    
    #def get_exports(self):
    
    
    #def get_opcodes(self):
