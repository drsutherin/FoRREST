
"""
    Requirements:
        * python-magic
"""

class Extract:
    
    def __init__(self, filename):
        self.filename = filename

    def get_filetype(self, meme = True):
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
            
        
