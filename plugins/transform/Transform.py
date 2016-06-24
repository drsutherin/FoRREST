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
	except: ImportError:
	    print "[-] Failed to load r2pipe"
	    print "[-] Do you have it installed?"
	    good = False
	return good

    def get_disassembly(self):
	if self.check_import() == True:
	    r2 = r2pipe.open(self._get_file)
	    out = r2.cmd('pd $s ~!invalid')
	    #need to figure out how to parse this
	    #there is a function to turn the information to json format built into radare2
	return out

    def get_mnemonics(self):
	if self.check_imports() == True:
	    r2 = r2pipe.open(self._get_file)
	    out = r2.cmd('pi $s ~!invalid')
	return out

    def get_functions(self):
	#needs parsing
	if self.check_imports() == True:
	    r2 = r2pipe.open(self._get_file)
	    r2.cmd('af')
	    out = r2.cmd('afl')
	return out

    def get_basic_blocks(self):
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
	    r2 = r2pipe.open(self._get_file)
	    r2.cmd('/R j ~j')
        pass
    
