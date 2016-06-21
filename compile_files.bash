#!/bin/bash

# This script will compile all C files in the custom binaries/c_codes directory
#		and save them as .out files in custom_binaries/
for i in test_binaries/custom_binaries/c_codes/*.c
do
	j=${i/*\//}  
	k=${j/\.*/}
	k="test_binaries/custom_binaries/${k}.out"
	gcc $i -o $k
done
