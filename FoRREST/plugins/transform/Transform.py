#requires radare2 to be installed
 
class Transform:
    
    def __init__(self, forrest):
        self.forrest = forrest
    
    def _get_file(self):
        return self.forrest.get_file()

    def get_disassembly(self):
	try:
	    import r2pipe
            r2 = r2pipe.open(self._get_file())
            out = r2.cmd('pi $s ~!invalid')
	    out = out.split('\n')
	except ImportError:
            print "[-] Failed to load r2pipe"
            print "[-] Do you have it installed?"
 	return out

    def get_mnemonics(self):
	try:
	    import r2pipe
            r2 = r2pipe.open(self._get_file())
            out = r2.cmd('pi $s ~!invalid')
	    out = out.split('\n')
	except ImportError:
            print "[-] Failed to load r2pipe"
            print "[-] Do you have it installed?"
        return [x.split()[0] for x in out]

    def get_functions(self):
	try:
	    import r2pipe
	    term_out = []
            r2 = r2pipe.open(self._get_file())
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
	except ImportError:
            print "[-] Failed to load r2pipe"
            print "[-] Do you have it installed?"
        return term_out

    def get_basic_blocks(self):
        '''
        Get entry and exit points for each block
        '''
        pass


    def get_data_references(self):
	try:
	    import r2pipe
            r2 = r2pipe.open(self._get_file())
            out = r2.cmd('/R mov ~mov')
            out += r2.cmd('/R lea ~lea | grep -v leave')
	    out = out.split('\n')
	    for x in out:
    		del out[0]
    		del out[0]
	except ImportError:
	    print "[-] Failed to load r2pipe"
            print "[-] Do you have it installed?"	
        return out
    
    def get_jump_targets(self):
	try:
	    import r2pipe
            term_out = []

	    r2 = r2pipe.open(self._get_file())
	    out = r2.cmd('/R j ~j ')
	    out = out.split('\n')

	    for x in out:
		x_split = x.split()
		jump = x_split[0] + ' ' + x_split[2] + ' ' + x_split[3]
		    
	    	if len(x_split) == 5:
	    	    jump += ' ' + x_split[4]

	    	term_out.append(jump)
	except ImportError:
            print "[-] Failed to load r2pipe"
            print "[-] Do you have it installed?"

	return term_out

    
