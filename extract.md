# Extract
The Extract plugin accesses the next, higher representation of the file's data.  These are also accessed using standard Python and GNU library functions, as well as the ```python-magic``` tool.  At this level, the utility of FoRREST arises primarily from parsing the information retrieved by calling the Python and GNU functions.

**```get_filetype```** returns the mime type (or magic number) of a file.

**```get_architecture```** function uses ```readelf``` to determine the architecture for which the current file was compiled.

**```get_version```** also uses ```readelf```, but with a different flag in order to return the version number of the file.

**```get_compiler```** uses ```objdump``` to get the sections of the file, and locates the compiler information.

**```get_sections```** function also uses ```objdump``` and returns the names of all of the sections within the current file.