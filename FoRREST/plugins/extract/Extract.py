
"""
    Requirements:
        * python-magic
"""

from Model import Extract_Model

class Extract:
    
    def __init__(self, forrest):
        self.forrest = forrest
        
    def _get_file(self):
        return self.forrest.get_file()

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
            data = magic.from_file(self._get_file(), meme)
        
        return data
    
    def get_version(self):
        """
            Returns the version number of the binary if present.
            
            Example:
                file = random.out
                returns "5.4.0"
        """
        return self.get_elf_header('Version')
        
    def get_architecture(self):
        """
            Returns the architecture the file was compiled for.
            
            Example:
                file = random.out
                returns "x86-64"
        """
        return self.get_elf_header('Machine')
        
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
        return self.get_section_ascii('.comment').strip('\x00')
        
    def get_section_ascii(self, section):
        temp = self.get_section_hex(section)
        
        word = ""
        temp = [z for x in temp for y in x for z in y]
        for x in zip(temp[::2], temp[1::2]):
            word += chr(int(x[0] + x[1], 16))
        
        return word
        
    def get_section_hex(self, section):
        out, err = self.forrest._shell('objdump', ['-s', '--section', section, self._get_file()])
        out = map(lambda x: x.lstrip(), out)
        out = [x.split(' ', 5)[1:5] for x in out[4:]]
        
        return out
        
    def get_elf_header(self, item = None):
        out, err = self.forrest._shell('readelf', ["-h", self._get_file()])

        temp = [x.split(':', 1) for x in out]
        temp = [y.strip() for x in temp for y in x]
        
        return_value = dict(zip(temp[::2], temp[1::2]))
        
        if item:
            if item in return_value:
                return_value = return_value[item]
            else:
                return_value = ''
                
        return return_value
        
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
        out, err = self.forrest._shell('objdump', ['-h', self._get_file()])

        return [x.strip().split()[1] for x in out[5:][::2]]

    def add_entry(self):
        if self._get_file() != None:
            return Extract_Model.add_entry(
                filetype=self.get_filetype(),
                version=self.get_version(),
                architecture=self.get_architecture(),
                compiler=self.get_compiler(),
                sections=self.get_sections()
            )
        else: return None

    @staticmethod
    def select(model):
        extract_model = model.extract[0]

        class Model:
            filetype=extract_model.filetype,
            version=extract_model.version,
            architecture=extract_model.architecture,
            compiler=extract_model.compiler,
            sections=[item.section for item in extract_model.sections]

        return Model
