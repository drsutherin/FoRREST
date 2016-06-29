

class Interpret:

    def __init__(self, idamous):
        """
            Description:
                This sets up the class.

            Args:
                `idamous` (Idamous): The idamous instance to work with.

            Returns:
                None
        """
        self.idamous = idamous

    def _get_file(self):
        """
            Description:
                This function gets the filepath and name of the file.

            Returns:
                str - Filepath and name
        """
        return self.idamous.get_file()

    def get_opcodes(self):
        """
            Description:
                Returns a list of the assembly code in binary. Each instruction
                is a list of bytes.

            Example:
                file = random.out
                returns [
                    '4008534', 55,
                    '4889e5',
                    '4883ec20',
                    etc
                ]

            Returns:
                [[str], ...] - A list of binary instructions.
        """
        out, err = self.idamous._shell('objdump', ['-d', self._get_file()])

        instructions = {}
        namespace = []

        for x in out:
            x = x.split()

            if len(x) == 2:
                if x[1][0] == '<' and x[1][-2] == '>' and x[1][-1] == ':':
                    namespace.append(x[1][1:-2])
                    if namespace[-1] not in instructions:
                        instructions[namespace[-1]] = []

            elif len(x) >= 2:
                temp = []
                if x[0][-1] == ':':
                    temp = []

                    for i in range(1, len(x)):
                        if len(x[i]) == 2:
                            temp.append(x[i])
                        else:
                            break

                    if len(temp) > 0 and len(namespace) > 0:
                        if namespace[-1] in instructions:
                            instructions[namespace[-1]].append(temp)

        return namespace, instructions

    def get_strings(self):
        """
            Description:
                Returns a list of strings found in the binary. The string must
                be four consecutive printable ASCII characters.

            Example:
                file = random.out
                returns [
                    '/lib64/ld-linux-x86-64.so.2',
                    'libc.so.6'
                    '__isoc99_scanf',
                    etc
                ]

            Returns:
                [str, ...] - A list of strings found in the binary file.
        """
        out, err = self.idamous._shell('strings', self._get_file())

        return out

    def get_imports(self):
        """
            Description:
                Returns a list of all the functions the binary references
                from a linked file object.

            Example:
                file = random.out
                returns [
                    '__isoc99_scanf',
                    '__libc_start_main',
                    'printf',
                    etc
                ]

            Returns:
                [str, ...] - A list of strings that are the names of imported
                functions.
        """
        stdout = self.idamous._shell_std('nm', [
            '-C', '--dynamic', self._get_file()
        ])
        out, err = self.idamous._shell('grep', 'U', stdout)

        return [x.split()[1] for x in out]

    def get_exports(self):
        """
            Description:
                Returns a list of functions and variables that the binary
                makes available to outside programs.

            Example:
                [
                    'printf'
                ]

            Returns:
                [str, ...] - A list of strings that are the names of exported
                functions.
        """
	out, err = self.idamous._shell('nm', ['-g',  self._get_file()])
	
	term_out = []

	for x in out:
	   if len(x.split()) == 3:
	      term_out.append(x.split()[2])
	   else:
	      term_out.append(x.split()[1])

	return term_out	

    def get_header_information(self):
        """
            Returns the header information for a file.

            Returns maybe a list? Maybe Dictionary?

            PEView - Windows only

        """
	#All the header Information
	out, err = self.idamous_shell('objbump', ['-x', self._get_file()])


	#archive-header
	out, err = self.idamous_shell('objdump', ['-a', self._get_file()])
	#file headers
	out, err = self.idamous_shell('objdump', ['-f', self._get_file()])
	#section headers
	out, err = self.idamous_shell('objdump', ['-h', self._get_file()])
	#private headers
	out, err = self.idamous_shell('objdump', ['-p', self._get_file()])
	#relocation entries of the files
	out, err = self.idamous_shell('objdump', ['-r', self._get_file()])
	

        return ''
