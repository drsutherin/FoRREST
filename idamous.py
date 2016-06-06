#!/usr/bin/python

import subprocess

class Idamous:
    
    def __init__(self):
        """
            Inits the class
        """
        # Change to not being hardcoded later
        self.operating_system = 'linux'
        self.current_file = None
    
    def set_file(self, filename):
        self.current_file = filename
    
    def _call_shell_function(self, commandName, args):
        """
            Make a call to the terminal and return the output.
        """
        output = subprocess.check_output([commandName].extend(args))
        return output
        
    # def get_elf(self, amount = 0):
    #     return_value = None
        
    #     if amount == 0:
    #         return_value = self._call_shell_function('readelf', ['-a', self.current_file])
    #     else:
    #         return_value = self._call_shell_function('readelf', ['-h', self.current_file])
            
    #     return return_value


# If you call idamous.py, run this.
if __name__ == '__main__':
    print 'Creating idamous instance'
    idamous = Idamous()
    idamous.set_file('test_binaries/custom_binaries/generate_fib.out')
    # print idamous.get_elf()
