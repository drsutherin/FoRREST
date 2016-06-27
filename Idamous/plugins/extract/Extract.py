
"""
    :Platform: Unix
    :Class Authors: Authors: Logan Rickert, Cole Loewer, David Sutherin
    :Standard: Flake8

    The main purpose of this class is to extract some basic information from
    the raw data stored within the file.

    Requirements:
        * python-magic
"""


class Extract:

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

    def get_filetype(self, mime=True):
        """
            Description:
                Returns the type of file for the current file based on a
                sequence of bits at the start of the file. This is considered
                the mime type.

            Args:
                `mime` (bool): Return the mime type or the full mime.

            Example:
                #!/bin/bash
                Returns: text/x-bash;

            Returns:
                str - The mime type
        """
        data = ""
        good = True

        try:
            import magic
        except ImportError:
            print "[-] Failed to load python-magic."
            print "[-] Do you have it installed?"
            print "[-] pip install python-magic"
            good = False

        if good:
            data = magic.from_file(self._get_file(), mime)

        return data

    def get_version(self):
        """
            Description:
                Returns the version number of the binary if present.

            Example:
                file = random.out
                returns "5.4.0"

            Returns:
                str - version number
        """
        return self.get_elf_header('Version')

    def get_architecture(self):
        """
            Description:
                Returns the architecture the file was compiled for.

            Example:
                file = random.out
                returns "x86-64"

            Returns:
                str - architecture
        """
        return self.get_elf_header('Machine')

    def get_compiler(self):
        """
            Description:
                Returns the name of the compiler used to compile the file if
                present.

            Example:
                file = random.out
                returns "GCC: (Ubuntu 4.8.4-2ubuntu1~14.0.4.3) 4.8.4."

            Returns:
                str - Compiler used
        """
        return self.get_section_ascii('.comment').strip('\x00')

    def get_section_ascii(self, section):
        """
            Description:
                Returns the given `section` in ascii.

            Args:
                `section` (str) - The section of the file.

            Example:
                section = ".comment"
                returns "GCC: (Ubuntu 4.8.4-2ubuntu1~14.0.4.3) 4.8.4."

            Returns:
                [str, str, ...] - The `section` in ascii.
        """
        temp = self.get_section_hex(section)

        word = ""
        temp = [z for x in temp for y in x for z in y]
        for x in zip(temp[::2], temp[1::2]):
            word += chr(int(x[0] + x[1], 16))

        return word

    def get_section_hex(self, section):
        """
            Description:
                Returns the given `section` in hex.

            Args:
                `section` (str) - The section of the file.

            Example:
                section = ".comment"
                returns [[23, 89, 43], [34, 59, 83], [45]]

            Returns:
                [[str], [str], ...] - The `section` in hex.
        """
        out, err = self.idamous._shell('objdump', [
            '-s', '--section', section, self._get_file()
        ])
        out = map(lambda x: x.lstrip(), out)
        out = [x.split(' ', 5)[1:5] for x in out[4:]]

        return out

    def get_elf_header(self, item=None):
        """
            Description:
                Gets the data from the elf header and returns it.

            Args:
                `item` - Only get entry in the elf header.

            Example:
                {
                    'Machine': "Index 80368",
                    'Class': "ELF32"
                }

            Returns:
                dict([[str, str], ...]) - A dictionary of the elf header.
        """
        out, err = self.idamous._shell('readelf', ["-h", self._get_file()])

        temp = [x.split(':', 1) for x in out]
        temp = [y.strip() for x in temp for y in x]

        return_value = dict(zip(temp[::2], temp[1::2]))

        if item:
            if item in return_value:
                return_value = return_value[item]
            else:
                return_value = ''

        return return_value

    def get_sections(self):
        """
            Description:
                Returns a list of section headers for a file.

            Example:
                file = random.out
                returns [
                    '.interp',
                    '.note.ABI-tag',
                    '.note.gnu.build-id',
                    '.gnu.hash',
                    etc
                ]

            Returns:
                [str, str, ...] - A list of the sections.
        """
        out, err = self.idamous._shell('objdump', ['-h', self._get_file()])

        return [x.strip().split()[1] for x in out[5:][::2]]
