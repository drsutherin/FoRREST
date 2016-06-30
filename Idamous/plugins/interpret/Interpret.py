class Interpret:

    def __init__(self, idamous):
        self.idamous = idamous
        
    def _get_file(self):
        return self.idamous.get_file()

    def get_opcodes(self):
        """
            Returns a list of the assembly code in binary.

            ( For Cole/David
                Command: objdump -d filename
                Output:
                    00000000004005ed <main>:
                    4005ed:       55                      push   %rbp
                    4005ee:       48 89 e5                mov    %rsp,%rbp
                    4005f1:       48 83 ec 20             sub    $0x20,%rsp
                Commments:
                    This function should return the text in the middle.
            )

            Example:
                file = random.out
                returns [
                    '4008534', 55,
                    '4889e5',
                    '4883ec20',
                    etc
                ]
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
                        
                    if len(temp) > 0:
                        if len(namespace) > 0 and namespace[-1] in instructions:
                                instructions[namespace[-1]].append(temp)

        return namespace, instructions

    def get_strings(self):
        """
            Returns a list of strings found in the binary. The string must
            be four consecutive printable ASCII characters.
            
            ( For Cole/David
                Command: strings filename
                Output:
                    /lib64/ld-linux-x86-64.so.2
                    libc.so.6
                    __isoc99_scanf
                    puts
                    printf
                Comments:
                    Just return terminal_output.split()
            )
            
            Example:
                file = random.out
                returns [
                    '/lib64/ld-linux-x86-64.so.2',
                    'libc.so.6'
                    '__isoc99_scanf',
                    etc
                ]
        """
        out, err = self.idamous._shell('strings', self._get_file())

        return out

    def get_imports(self):
        """
            Returns a list of all the functions the binary references 
            from a linked file object.
            
            ( For Cole/David
                Command: nm -C --dynamic filename
                Output:
                    w __gmon_start__
                    U __isoc99_scanf
                    U __libc_start_main
                    U printf
                    U puts
                Comments:
                    We want the ones with a U.
            )
            
            Example:
                file = random.out
                returns [
                    '__isoc99_scanf',
                    '__libc_start_main',
                    'printf',
                    etc
                ]
        """
        stdout = self.idamous._shell_std('nm', ['-C', '--dynamic', self._get_file()])
        out, err = self.idamous._shell('grep', 'U', stdout)

        return [x.split()[1] for x in out]

    def get_exports(self):
        """
            Returns a list of functions and variables that the binary
            makes available to outside programs.

            ( For Cole/David
                Comments:
                    I'm not too sure on this one. I don't have any
                    .so files laying around. Maybe email Doctor Bryant?

                    At any rate, what you're looking for on Google is:
                    "nm get exported functions".

                    I think it might be that things starting with T
                    are functions that are exported.
            )

            Returns [
                'printf'
            ]
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

            ( For Cole/David
                Comments:
                    I'm not too sure what they want from this. The description
                    just says "structural information about how the program is
                    organized." I would email Doctor Bryant.
            )

            Returns maybe a list? Maybe Dictionary?
            
            PEView - Windows only
            
        """
	#All the folowing header Information, also the symbol table
	out, err = self.idamous_shell('objdump', ['-x', self._get_file()])

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
