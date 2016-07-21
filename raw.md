# Raw
The Raw plugin accesses the most fundamental information about the binary file, and are currently executed almost exclusively using Python standard library functions, e.g. ```os.stat()```.


**```get_name```** simply parses the string which was passed as the path to the file to load, and returns only the file name, excluding the path.

**```get_path```** is analogous to ```get_name```, but returns only the path to the file, excluding the file name.

**```get_extension```** function simply parses the file path string and returns the file's extension (or nothing, if the file does not have one).

**```get_size```** returns the size of the currently loaded file in bytes.

**```get_inode```** returns the inode of the currently loaded file.

***```get_{md5,sha1,sha256,sha512}```** are multiple functions to get the checksums of the current file using various hashing algorithms

**```read_chunk```** reads a section of the original byte stream from the file.  The default chunk size is 4096 bytes, but that can be changed by passing the function an integer.
