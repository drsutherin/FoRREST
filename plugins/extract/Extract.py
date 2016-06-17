
"""
    Requirements:
        * python-magic
"""

class Extract:
    
    def __init__(self, idamous):
        self.idamous = idamous
        self.filename = self.idamous.get_file()

    def get_filetype(self, meme = True):
        """
            Returns the type of file for the current file based on a sequence
            of bits at the start of the file. This is considered the mime type.
            
            Example:
                #!/bin/bash
                Returns: text/x-bash;
        """
        data = ""
        good = True
        
        try:
            import magic
        except ImportError:
            print "[-] Failed to load python-magic."
            print "[-] Do you have it installed?"
            print "[-] pip install python-magic"
            good = False
            
        if good:
            data = magic.from_file(self.filename, meme)
        
        return data
    
    def get_version(self):
        """
            Returns the version number of the binary if present.
            
            Example:
                file = random.out
                returns "5.4.0"
        """
        return ''
        
    def get_architecture(self):
        """
            Returns the architecture the file was compiled for.
            
            Example:
                file = random.out
                returns "x86-64"
        """
        return ''
        
    def get_compiler(self):
        """
            Returns the name of the compiler used to compile the file if present.
            
            ( For Cole/David
                Command: objdump -s --section .comment filename
                Output:
                    Contents of section .comment:
                    0000 4743433a 20285562 756e7475 20342e38  GCC: (Ubuntu 4.8
                    0010 2e342d32 7562756e 7475317e 31342e30  .4-2ubuntu1~14.0
                    0020 342e3329 20342e38 2e3400             4.3) 4.8.4. 
                Comment:
                    You may want to look into seeing if objdump will just display
                    ASCII output instead of looking into parsing out the extra
                    hex.
            )
            
            Example:
                file = random.out
                returns "GCC: (Ubuntu 4.8.4-2ubuntu1~14.0.4.3) 4.8.4."
        """
        return ''
        
    def get_sections(self):
        """
            Returns a list of section headers for a file.
            
            ( For Cole/David
                Command: objdump -h filename
                Output:
                    0 .interp       0000001c  0000000000400238  0000000000400238  00000238  2**0
                                    CONTENTS, ALLOC, LOAD, READONLY, DATA
                    1 .note.ABI-tag 00000020  0000000000400254  0000000000400254  00000254  2**2
                                    CONTENTS, ALLOC, LOAD, READONLY, DATA
                    2 .note.gnu.build-id 00000024  0000000000400274  0000000000400274  00000274  2**2
                                    CONTENTS, ALLOC, LOAD, READONLY, DATA
            )
            
            Example:
                file = random.out
                returns [
                    '.interp',
                    '.note.ABI-tag',
                    '.note.gnu.build-id',
                    '.gnu.hash',
                    etc
                ]
        """
        return []
