"""
    :Platform: Unix
    :Class Authors: Authors: Logan Rickert, Cole Loewer, David Sutherin
    :Standard: Flake8

    The main purpose of this class is to transform the interpred data.

    Requirements:
        * radare2
        * r2pipe
"""


class Transform:

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

    def check_imports(self):
        """
            Description:
                Checks to make sure all of the required imports
                have been loaded.

            Returns:
                bool - if import was sucessful.
        """
        good = True
        try:
            import r2pipe
        except ImportError:
            print "[-] Failed to load r2pipe"
            print "[-] Do you have it installed?"
            good = False
        return good

    def get_disassembly(self):
        """
            Description:
                Gets the disassembly for a given file.

            Returns:
                None
        """
        if self.check_imports():
            r2 = r2pipe.open(self._get_file)
            out = r2.cmd('pd $s ~!invalid')
            # need to figure out how to parse this
            # there is a function to turn the information to json format built
            # into radare2
            r2.quit()
        return out

    def get_mnemonics(self):
        """
            Description:
                Gets the portion of the assembly instruction that is related to
                the action being preformed.

            Returns:
                None
        """
        if self.check_imports():
            r2 = r2pipe.open(self._get_file)
            out = r2.cmd('pi $s ~!invalid')
            r2.quit()
        return out

    def get_functions(self):
        """
            Description:
                Gets the functions used in the program.

            Returns:
                None
        """
        #needs parsing
        if self.check_imports():
            r2 = r2pipe.open(self._get_file)
            r2.cmd('af')
            out = r2.cmd('afl')
            r2.quit()
        return out

    def get_basic_blocks(self):
        """
            Description:
                Gets the directed graph of basic blocks that can be
                constructed by analyzing the boundaries and control
                flow of instructions.

            Returns:
                None
        """

        '''
            if self.check_imports() == True:
            r2 = r2pipe.open(self._get_file)
            r2.cmd('af')
            r2.cmd('ag > b.dot')
            #displays with xdot not really what i want
            out = r2.cmd('!xdot b.dot')
            #not done
        return out
        '''
        pass

    def get_data_references(self):
        """
            Description:
                The location of data values derived from interpreting memory
                store and load operations.

            Returns:
                None
        """
        '''
        if self.check_imports() == True:
            r2 = r2pipe.open(self._get_file)
            r2.cmd('/R ')
        return out
        '''
        pass

    def get_jump_targets(self):
        """
            Description:
                The memory address offsets obtained by analyzing the targets
                of conditional and unconditional control flow change
                instructions.

            Returns:
                None
        """
        #needs parsing
        if self.check_imports() is True:
            r2 = r2pipe.open(self._get_file)
            r2.cmd('/R j ~j')
            r2.close()
            pass
