# Transform
The Transform plugin provides access to the Level 3 representations of a file's data.  All of the features offered by this plugin are derived by implementing [Radare2](http://radare.org/)--a tool for disassembling and debugging binary files.

**```get_mnemonics```** returns a list of mnemonics that are present in a binary's instructions.

**```get_functions```** returns a list of the functions that are in the binary by parsing the disassembly from Radare2 to return only the assembly instructions.

**```get_data_references```** looks for ```lea``` and ```mov``` in the assembly instructions and creates a list of the memory addresses accessed by those instructions.

**```get_jump_targets```** looks through the disassembly of a binary and filters out any line that doesn't contain a jump command, leaving a list of only the jump instructions.
