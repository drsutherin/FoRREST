# Idamous
Reverse Engineering Framework

Version 0.8

## Overview
The purpose of this project is to create a vulnerability anaylsis framework that
combines existing tools into one package. It also makes it easier to create or
install tools into the framework for use.

## Background
This framework is currently designed for Linux

## Requirements
* Python 2.7

## Running
To run the program:

```
python Idamous.py
```

## Extending
To extend the program, just import idamous.

```
import Idamous
```

# Levels of Representation

The information found in a binary can be represented in many ways and on
many different levels. You start on a low-level with very simplistic information
and as you extract data, you start to get higher-level information.

### Level 0 (Raw Data)

* **Filename** - The name of the file that you are working with.
* **Extension** - The name of the extension for the file you are working with
if it's present.
* **Size** - The size of the file you are working with.
* **inode** - The physical location the file on the file system.
* **Path** - The path that leads to the file.
* **Checksums** - The digest value obtained by running a hashing algorithm on
the raw data.

### Level 1 (Extracted Data)

* **Filetype** - The type of file which is denoted by a sequence of bits at the 
start of a file. This is considered the mime type.
* **Version** - The version numbers of the program (if used).
* **Architecture** - The architecture that the program was compiled for.
* **Compiler** - The compiler that was used to generate the file (if known).
* **Sections** - The name and offset addresses that divide the file into
meaningful paritions.

### Level 2 (Interpreted Data)

* **Opcodes** - The bytes from the .text section that can be decoded into a 
stream of opcodes. The .text is the binary's actual code.
* **Strings** - A list of strings from the .data section and other sections.
* **Imports** - A list of functions the program references from a linked
object file.
* **Exports** - A list of variables and function addresses made available to
outside programs.
* **Header Information** - Information about how the program is organized.

### Level 3 (Transformed Data)

* **Disassembly** - The output from the transformation from a binary file
to an assembly file.
* **Mnemonics** - The portion of the assembly instruction that is related
to the action being preformed.
* **Functions** - The list of addresses that are discovered from analyzing the
targets of call instructions.
* **Basic Blocks** - The directed graph of basic blocks that can be constructed
by analyzing the boundaries and control flow of instructions.
* **Data References** - The location of data values derived from interpreting
memory store and load operations.
* **Jump Targets** - The memory address offsets obtained by analyzing the
targets of conditional and unconditional control flow change instructions.
