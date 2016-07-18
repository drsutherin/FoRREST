# Structure
FoRREST is structured as a set of Python classes.  The primary class, FoRREST, contains basic features for manipulating the object (load a file, call the shell, etc.).  The remaining classes are referred to as Plugins, and are divided according to the levels of information representation described below.

## Levels of Information Representation

The information found in a binary can be represented in many ways and on
many different levels. You start on a low-level with very simplistic information
and as you extract data, you start to get higher-level information.

### Level 0: Raw Data

* **Filename** - The name of the file that you are working with.
* **Extension** - The name of the extension for the file you are working with if it's present.
* **Size** - The size of the file you are working with.
* **inode** - The physical location the file on the file system.
* **Path** - The path that leads to the file.
* **Checksums** - The digest value obtained by running a hashing algorithm on the raw data.

### Level 1: Extracted Data

* **Filetype** - The type of file which is denoted by a sequence of bits at the start of a file. This is considered the mime type.
* **Version** - The version numbers of the program (if used).
* **Architecture** - The architecture that the program was compiled for.
* **Compiler** - The compiler that was used to generate the file (if known).
* **Sections** - The name and offset addresses that divide the file into meaningful paritions.

### Level 2: Interpreted Data

* **Opcodes** - The bytes from the .text section that can be decoded into a  stream of opcodes. The .text is the binary's actual code.
* **Strings** - A list of strings from the .data section and other sections.
* **Imports** - A list of functions the program references from a linked object file.
* **Exports** - A list of variables and function addresses made available to outside programs.
* **Header Information** - Information about how the program is organized.

### Level 3: Transformed Data

* **Disassembly** - The output from the transformation from a binary file to an assembly file.
* **Mnemonics** - The portion of the assembly instruction that is related to the action being preformed.
* **Functions** - The list of addresses that are discovered from analyzing the targets of call instructions.
* **Basic Blocks** - The directed graph of basic blocks that can be constructed by analyzing the boundaries and control flow of instructions.
* **Data References** - The location of data values derived from interpreting memory store and load operations.
* **Jump Targets** - The memory address offsets obtained by analyzing the targets of conditional and unconditional control flow change instructions.

### Level 4: Inferred Data

* **Control Flow Graph** - Control flow graphs (CFGs) are visual representations of basic blocks that include arrows signifying which blocks a given block calls or is called by
* **System Calls** -  System call traces determine what operating system functions the program attempts to access.
* **Function Traces** - Function traces note sequences of functions that are executed, and in what order.
* **Program Slices** -  Program slices are sub-sequences of code that affect the value of a variable through assignment or some other operation.
* **Intermediate Representation** - Intermediate representation (IR) is a form of expanded assembly code, that breaks each processor instruction into multiple steps to explicitly define every action necessary to perform the instruction. 
* **Decompilation** - Decompiled source code is the final step in the transition from the original string of bytes to a high-level, human-readable programming language.  It is, ideally, very similar to the original source code that created the executable.
* **Stack Frames** - Stack frames are records of the program stacks built in memory when calling functions within the program, i.e. parameter values, local variables, and return addresses.
* **Packet Captures** - Packet captures are sets of data that are collected whenever a program tries to communicate over a network
* **Symbolic Execution** - Symbolic execution of programs allows for analysis of potential paths without using concrete input.  This is done by automated analysis tools which substitute symbols for the values of variables.
* **Deobfuscation** - Obfuscation makes exeuctables very hard to reverse engineer.  Developers may obfuscate their code for many reasons, from wanting to protect their intellectual property to disguising a program's true intent because it's malicious. Obfuscation can also happen unintentionally when a compiler optimizes code.  Deobfuscation attempts to simplify the code in order to make it clear what the developer's intent was

