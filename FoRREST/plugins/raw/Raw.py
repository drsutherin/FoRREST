
import os
import hashlib
from Model import Raw_Model

class Raw:

    def __init__(self, forrest):
        self.forrest = forrest
        self.file = None
        
    def _get_file(self):
        return self.forrest.get_file()

    def add_entry(self):
        if self._get_file() != None:
            Raw_Model.create(
                name=self.get_name(),
                extension=self.get_extension(),
                size=self.get_size(),
                inode=self.get_inode(),
                path=self.get_path(),
                md5sum=self.get_md5(),
                sha1sum=self.get_sha1(),
                sha256sum=self.get_sha256()
            )

    def get_name(self):
        """
            Returns the filename of the current file.
            
            Example: 
                file = /cake/awesome/sweet.py
                returns: "sweet.py" 
        """
        return os.path.basename(self._get_file())
        
    def get_extension(self):
        """
            Returns the extension of the current file.
            
            Example:
                file = /cake/awesome/sweet.py
                returns: "py"
        """
        temp = self._get_file().split('.')
        ext = ""
        
        # Check to see if there is a dot.
        if len(temp) > 1:
            ext = temp[-1]
        
        return ext

    def get_size(self):
        """
            Returns the size of the current file in bytes.
            
            Example:
                3343 forrest.py
                returns: 3343
        """
        return os.stat(self._get_file()).st_size
        
    def get_inode(self):
        """
            Returns the inode of the current file.
            
            Example:
                303 forrest.py
                returns: 303
        """
        return os.stat(self._get_file()).st_ino
    
    def get_path(self):
        """
            Returns the path to the file.
            
            Example:
                file = /cake/awesome/sweet.py
                returns: "/cake/awesome"
                
                file = plugins/raw/Raw.py
                returns: "plugins/raw"
        """
        return os.path.dirname(self._get_file())
        
    def get_md5(self):
        """
            Returns the MD5 sum for the file.
            
            Example:
                file = /cake/awesome/sweet.py
                returns: "943172131622f261d9af95e1634159d9"
        """
        hash_algo = hashlib.md5()

        return Raw.hash_file(self._get_file(), hash_algo)

    def get_sha1(self):
        hash_algo = hashlib.sha1()
        return Raw.hash_file(self._get_file(), hash_algo)

    def get_sha256(self):
        hash_algo = hashlib.sha256()

        return Raw.hash_file(self._get_file(), hash_algo)

    def get_sha512(self):
        hash_algo = hashlib.sha512()
        return Raw.hash_file(self._get_file(), hash_algo)

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
            self.file = open(self._get_file(), 'rb')

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

