# Plugins
The following sections describe the plugins (i.e. sub-classes) and provide a brief description of how they function.  Each of the plugins corresponds to one of the levels of data representations described [here](https://drsutherin.gitbooks.io/forrest/content/structure.html). For more information about using FoRREST, see our [API documentation](https://drsutherin.github.io/FoRREST/html/)

## [Raw](https://drsutherin.gitbooks.io/forrest/content/raw.html)
The Raw plugin accesses the most fundamental information about the binary file, and are currently executed almost exclusively using Python standard library functions, e.g. ```os.stat()```.

## [Extract](https://drsutherin.gitbooks.io/forrest/content/extract.html)
The Extract plugin accesses the next, higher representation of the file's data.  These are also accessed using standard Python and GNU library functions, as well as the ```python-magic``` tool.  At this level, the utility of FoRREST arises primarily from parsing the information retrieved by calling the Python and GNU functions.

## [Interpret](https://drsutherin.gitbooks.io/forrest/content/interpret.html)
The Interpret plugin accesses the Level 2 representations of the executable's data.  All of the interpreted data functions are performed using standard GNU library functions.  Similar to the Extract plugin, its primary utility comes from parsing the information received from other functions.

## [Transform](https://drsutherin.gitbooks.io/forrest/content/transform.html)
The Transform plugin provides access to the Level 3 representations of a file's data.  All of the features offered by this plugin are derived by implementing [Radare2](http://radare.org/)--a tool for disassembling and debugging binary files.

## [Infer](https://drsutherin.gitbooks.io/forrest/content/infer.html)
The Infer plugin accesses the highest level representation of the information extracted from a binary file, and can be used to perform in-depth analyses.  The inferred data features are gathered by using [boomerang](http://boomerang.sourceforge.net/)--a tool for acquiring the decompilation of a file, Radare2, and [angr](http://angr.io/)--an extensive tool for performing binary analysis.