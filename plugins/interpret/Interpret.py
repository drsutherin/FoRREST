
import subprocess
import os

class Interpret:
    
    def __init__(self, idamous):
        self.idamous = idamous
        
    def get_opcodes(self):
        """
            Returns a list of the assembly code in binary.
            
            ( For Cole/David
                Command: objdump -d filename
                Output:
                    00000000004005ed <main>:
                    4005ed:       55                      push   %rbp
                    4005ee:       48 89 e5                mov    %rsp,%rbp
                    4005f1:       48 83 ec 20             sub    $0x20,%rsp
                Commments:
                    This function should return the text in the middle.
            )
            
            Example:
                file = random.out
                returns [
                    '55',
                    '4889e5',
                    '4883ec20',
                    etc
                ]
        """
        pass
    
    def get_strings(self):
        """
            Returns a list of strings found in the binary. The string must
            be four consecutive printable ASCII characters.
            
            ( For Cole/David
                Command: strings filename
                Output:
                    /lib64/ld-linux-x86-64.so.2
                    libc.so.6
                    __isoc99_scanf
                    puts
                    printf
                Comments:
                    Just return terminal_output.split()
            )
            
            Example:
                file = random.out
                returns [
                    '/lib64/ld-linux-x86-64.so.2',
                    'libc.so.6'
                    '__isoc99_scanf',
                    etc
                ]
        """
        pass
    
    def get_imports(self):
        """
            Returns a list of all the functions the binary references 
            from a linked file object.
            
            ( For Cole/David
                Command: nm -C --dynamic filename
                Output:
                    w __gmon_start__
                    U __isoc99_scanf
                    U __libc_start_main
                    U printf
                    U puts
                Comments:
                    We want the ones with a U.
            )
            
            Example:
                file = random.out
                returns [
                    '__isoc99_scanf',
                    '__libc_start_main',
                    'printf',
                    etc
                ]
        """
        pass
    
    def get_exports(self):
        """
            Returns a list of functions and variables that the binary
            makes available to outside programs.
            
            ( For Cole/David
                Comments:
                    I'm not too sure on this one. I don't have any
                    .so files laying around. Maybe email Doctor Bryant?
                    
                    At any rate, what you're looking for on Google is:
                    "nm get exported functions".
                    
                    I think it might be that things starting with T
                    are functions that are exported.
            )
            
            Returns [
                'printf'
            ]
        """
        pass

    def get_header_information(self):
        """
            Returns the header information for a file.
            
            ( For Cole/David
                Comments:
                    I'm not too sure what they want from this. The description
                    just says "structural information about how the program is
                    organized." I would email Doctor Bryant.
            )
            
            Returns maybe a list? Maybe Dictionary?
        """
        pass
    

