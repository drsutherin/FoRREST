
import os
import hashlib

class File:
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        
    def get_name(self):
        return os.path.basename(self.filename)
        
    def get_extension(self):
        temp = self.filename.split('.')
        ext = ""
        
        if len(temp) > 1:
            ext = temp[-1]
        
        return ext

    def get_size(self):
        return os.stat(self.filename).st_size
        
    def get_inode(self):
        return os.stat(self.filename).st_ino
    
    def get_path(self):
        return os.path.dirname(self.filename)
        
    def get_md5(self):
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
        if self.file == None:
            self.file = open(self.filename, 'rb')

        chunk = self.file.read(chunksize)
        if not chunk:
            self.file.close()
            self.file = None
            
        return chunk

    @staticmethod
    def hash_file(filename, hash_algo):
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()

