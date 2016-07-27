# Infer
The Infer plugin accesses the highest level representation of the information extracted from a binary file, and can be used to perform in-depth analyses.  The inferred data features are gathered by using [boomerang](http://boomerang.sourceforge.net/)--a tool for acquiring the decompilation of a file, Radare2, and [angr](http://angr.io/)--an extensive tool for performing binary analysis.

**```get_cfg```** uses angr and an extension of it called angr-utils.  The CFG is saved as a PNG image file located in the same directory as the file upon which it was called, and it is displayed immediately.

**```get_ir```** uses angr and its dependency PyVex to return the intermediate representation of the original bytes.

**```decompile```** gets the decompilation by using boomerang to translate the binary into C code.  The file is saved in the outputs directory within FoRREST's root directory. 

**```deobfuscate```** is currently being developed. We are planning to use a tool called metasm.

#### Not Yet Implemented
**```get_sys_calls```** is intended to return the program's call to the host system.  Not currently implemented, considering using ```strace```

**```get_func_trace```** is intended to return all calls to a specific function.  Not currently implemented, considering calling FoRREST's ```get_functions``` along with the disassembly to determine where functions are called, and by what other functions.

**```slice```** Not currently implemented, planning to use angr to perform back-slicing.

**```get_stack_frames```** is intended to return all of the stack frames built by the program during execution. Not currently implemented.

**```symbolic_exec```** Not currently implemented, planning to use angr's execution engine for symbolic execution.

**```taint_analysis```** Not currently implemented, considering using a combination of FoRREST's \verb/get_data_references/ and \verb/slice/ functions.