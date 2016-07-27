# Interpret
The Interpret plugin accesses the Level 2 representations of the executable's data.  All of the interpreted data functions are performed using standard GNU library functions.  Similar to the Extract plugin, its primary utility comes from parsing the information received from other functions.

 Opcodes: \verb/get_opcodes/ returns the opcodes from the disassembly of the file separated into hexadecimal bytes, while omitting the memory addresses in which those opcodes are stored when the file is loaded.  It also returns any comments from the disassembly regarding that opcode, e.g. if the opcode represents a call to an external library.  It does so by using \verb/objdump/ and parsing the information.

\item Strings: The \verb/get_strings/ function utilizes the \verb/strings/ command to return a list of strings that are present in the loaded binary. 

\item Imports: The \verb/get_imports/ function returns a list off the functions that the binary references from a linked file object. This is done by using the GNU \verb/nm/ command with the arguments \verb/-C --dynamic/.

\item Exports: The \verb/get_exports/ function returns a list of functions and variables that the binary makes available outside of its self. This is also done by using the \verb/nm/ command, however using the argument \verb/-g/ to extract the external symbols. \newline