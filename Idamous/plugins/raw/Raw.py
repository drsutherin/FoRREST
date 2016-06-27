
"""
    :Platform: Unix
    :Class Authors: Authors: Logan Rickert, Cole Loewer, David Sutherin
    :Standard: Flake8

    The main purpose of this class is to handle getting meta-data about files.
"""

import os
import hashlib
from Model import Raw_Model


class Raw:

    def __init__(self, idamous):
        """
            Description:
                This sets up the class.

            Args:
                idamous: The idamous instance to work with.

            Returns:
                None.
        """
        self.idamous = idamous
        self.file = None

    def _get_file(self):
        """
            Description:
                This function gets the filepath and name of the file.

            Returns:
                str. Filepath and name.
        """
        return self.idamous.get_file()

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
            Description:
                Returns the filename of the current file.

            Example:
                file = /cake/awesome/sweet.py
                returns: "sweet.py"

            Returns:
                str. The filename.
        """
        return os.path.basename(self._get_file())

    def get_extension(self):
        """
            Description:
                Returns the extension of the current file.

            Example:
                file = /cake/awesome/sweet.py
                returns: "py"

            Returns:
                str. The extenstion.
        """
        temp = self._get_file().split('.')
        ext = ""

        # Check to see if there is a dot.
        if len(temp) > 1:
            ext = temp[-1]

        return ext

    def get_size(self):
        """
            Description:
                Returns the size of the current file in bytes.

            Example:
                3343 idamous.py
                returns: 3343

            Returns:
                int. The size of the file.
        """
        return os.stat(self._get_file()).st_size

    def get_inode(self):
        """
            Description:
                Returns the inode of the current file.

            Example:
                303 idamous.py
                returns: 303

            Returns:
                int. The inode.
        """
        return os.stat(self._get_file()).st_ino

    def get_path(self):
        """
            Description:
                Returns the path to the file.

            Example:
                file = /cake/awesome/sweet.py
                returns: "/cake/awesome"

                file = plugins/raw/Raw.py
                returns: "plugins/raw"

            Returns:
                str. The path.
        """
        return os.path.dirname(self._get_file())

    def get_md5(self):
        """
            Description:
                Returns the MD5 sum for the file.

            Example:
                file = /cake/awesome/sweet.py
                returns: "943172131622f261d9af95e1634159d9"

            Returns:
                str. The hash.
        """
        hash_algo = hashlib.md5()
        return Raw.hash_file(self._get_file(), hash_algo)

    def get_sha1(self):
        """
            Description:
                Returns the SHA1 sum for the file.

            Example:
                file = /cake/awesome/sweet.py
                returns: "943172131622f261d9af95e1634159d9"

            Returns:
                str. The hash.
        """
        hash_algo = hashlib.sha1()
        return Raw.hash_file(self._get_file(), hash_algo)

    def get_sha256(self):
        """
            Description:
                Returns the SHA256 sum for the file.

            Example:
                file = /cake/awesome/sweet.py
                returns: "943172131622f261d9af95e1634159d9"

            Returns:
                str. The hash.
        """
        hash_algo = hashlib.sha256()
        return Raw.hash_file(self._get_file(), hash_algo)

    def get_sha512(self):
        """
            Description:
                Returns the SHA512 sum for the file.

            Example:
                file = /cake/awesome/sweet.py
                returns: "943172131622f261d9af95e1634159d9"

            Returns:
                str. The hash.
        """
        hash_algo = hashlib.sha512()
        return Raw.hash_file(self._get_file(), hash_algo)

    def read_chunck(self, chunksize=4096):
        """
            Description:
                Returns a chunck of the file. By default, the size is 4096.
                The function will start at the beginning and hold its position
                each read.
                Once the file has been completely read in, calling this
                function will return empty string ('') and reset to the
                beginning of the file.

            Args:
                chunksize (int): The lenght of string to read in.

            Returns:
                str. The chunck from the requested file in rb.
        """
        if self.file is None:
            self.file = open(self._get_file(), 'rb')

        chunk = self.file.read(chunksize)
        if not chunk:
            self.reset_read()

        return chunk

    def reset_read(self):
        """
            Description:
                Force reset the read_chunck method to start at the beginning.

            Returns:
                None.
        """
        if self.file is not None:
            self.file.close()
            self.file = None

    @staticmethod
    def hash_file(filename, hash_algo):
        """
            Description:
                Returns a hash for @filename based on the the @hash_algo.

            Args:
                filename (str): The name of the file to hash.
                hash_algo (hashlib): The hashing algorithm.
                (IE: hashlib.sha512())

            Returns:
                str. The hash.
        """
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()
