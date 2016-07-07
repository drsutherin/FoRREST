#requires radare2 to be installed
class Transform:
    
    def __init__(self, idamous):
        self.idamous = idamous
    
    def _get_file(self):
        return self.idamous.get_file()

    def check_imports(self):
        good = True
        try:
            import r2pipe
        except ImportError:
            print "[-] Failed to load r2pipe"
            print "[-] Do you have it installed?"
            good = False
        return good

    def get_disassembly(self):
        if self.check_import() == True:
            r2 = r2pipe.open(self._get_file)
            out = r2.cmd('pi $s ~!invalid')
	    out = out.split('\n')
 	return out

    def get_mnemonics(self):
        if self.check_imports() == True:
            r2 = r2pipe.open(self._get_file)
            out = r2.cmd('pi $s ~!invalid')
        return [x.split()[0] for x in out]

    def get_functions(self):
        if self.check_imports() == True:
            r2 = r2pipe.open(self._get_file)
            #analyze the functions
            r2.cmd('af')
	    #list the functions
            out = r2.cmd('afl')
	    #properly split the list
	    out = out.split('\n')
	#parse for the functions
        for x in out:
    	    if len(x.split()) == 6:
    	     	term_out.append(x.split()[5])
            else:
		term_out.append(x.split()[3])

        return term_out

    def get_basic_blocks(self):
        if self.check_imports() == True:
            r2 = r2pipe.open(self._get_file)
            r2.cmd('aa')
	    out =r2.cmd('afg')
        return out


    def get_data_references(self):
        '''
        if self.check_imports() == True:
            r2 = r2pipe.open(self._get_file)
            r2.cmd('/R ')
        return out
        '''
        pass
    
    def get_jump_targets(self):
        #needs parsing
        if self.check_imports() == True:
            term_out = []

	    r2 = r2pipe.open(self._get_file)
	    out = r2.cmd('/R j ~j ')
	    out = out.split('\n')

	    for x in out:
		x_split = x.split()
		jump = x_split[0] + ' ' + x_split[2] + ' ' + x_split[3]
		    
	    	if len(x_split) == 5:
	    	    jump += ' ' + x_split[4]

	    	term_out.append(jump)
		   	
	return term_out

    
