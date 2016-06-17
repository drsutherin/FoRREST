
import os
import hashlib

class File:
    
    def __init__(self, idamous):
        self.filename = idamous.get_file()
        self.file = None
        
    def get_name(self):
        """
            Returns the filename of the current file.
            
            Example: 
                file = /cake/awesome/sweet.py
                returns: "sweet.py" 
        """
        return os.path.basename(self.filename)
        
    def get_extension(self):
        """
            Returns the extension of the current file.
            
            Example:
                file = /cake/awesome/sweet.py
                returns: "py"
        """
        temp = self.filename.split('.')
        ext = ""
        
        # Check to see if there is a dot.
        if len(temp) > 1:
            ext = temp[-1]
        
        return ext

    def get_size(self):
        """
            Returns the size of the current file in bytes.
            
            Example:
                3343 idamous.py
                returns: 3343
        """
        return os.stat(self.filename).st_size
        
    def get_inode(self):
        """
            Returns the inode of the current file.
            
            Example:
                303 idamous.py
                returns: 303
        """
        return os.stat(self.filename).st_ino
    
    def get_path(self):
        """
            Returns the path to the file.
            
            Example:
                file = /cake/awesome/sweet.py
                returns: "/cake/awesome"
                
                file = plugins/raw/Raw.py
                returns: "plugins/raw"
        """
        return os.path.dirname(self.filename)
        
    def get_md5(self):
        """
            Returns the MD5 sum for the file.
            
            Example:
                file = /cake/awesome/sweet.py
                returns: "943172131622f261d9af95e1634159d9"
        """
        hash_algo = hashlib.md5()
        return File.hash_file(self.filename, hash_algo)
        
    def get_sha1(self):
        hash_algo = hashlib.sha1()
        return File.hash_file(self.filename, hash_algo)
        
    def get_sha256(self):
        hash_algo = hashlib.sha256()
        return File.hash_file(self.filename, hash_algo)
    
    def get_sha512(self):
        hash_algo = hashlib.sha512()
        return File.hash_file(self.filename, hash_algo)

    def read_chunck(self, chunksize=4096):
        """
            Returns a chunck of the file. By default, the size is 4096.
            The function will start at the beginning and hold its position
            each read.
            Once the file has been completely read in, calling this function
            will return empty string ('') and reset to the beginning of the
            file.
        """
        if self.file == None:
            self.file = open(self.filename, 'rb')

        chunk = self.file.read(chunksize)
        if not chunk:
            self.reset_read()
            
        return chunk
        
    def reset_read(self):
        """
            Force reset the read_chunck method to start at the beginning.
        """
        if self.file != None:
            self.file.close()
            self.file = None

    @staticmethod
    def hash_file(filename, hash_algo):
        """
            Returns a hash for @filename based on the the @hash_algo.
        """
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()

