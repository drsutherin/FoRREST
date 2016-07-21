class Infer:
    def __init__(self, forrest):
        self.forrest = forrest

    def _get_file(self):
        return self.forrest.get_file()

    def get_cfg(self):
        try:
	    import angr
            #from angrutils import *
            from .visualize import plot_cfg # this is the only thing necessary from angrutils
            proj = angr.Project(self._get_file(), load_options={'auto_load_libs':False})
            main = proj.loader.main_bin.get_symbol("main")
            start_state = proj.factory.blank_state(addr=main.addr)
            cfg = proj.analyses.CFGAccurate(fail_fast=True, starts=[main.addr], initial_state=start_state)
            plot_cfg(cfg, "%s_cfg" % self._get_file(), asminst=True, remove_imports=True, remove_path_terminator=True)
            return "[+] CFG saved as %s_cfg.png" % self._get_file()
        except ImportError:
            print "[-] Could not load angr"
            print "[-] Do you have it installed?"
        return

    def get_sys_calls(self, params = None):
        '''
        Will return system calls
        Can use Linux strace function, allow for params to add -e so users can search for calls to specific system functions
        '''
        pass

    def get_func_trace(self, params = None):
        '''
        Will return function calls
        ? Call transform.get_functions and then find calls to them?
        Can use params to allow users to specify which function to trace
        '''
        pass

    def slice(self, params = None):
        '''
        params will need to be a variable to track changes in (I think) and the function will return the sequences of opcodes leading up to a change in that variable/memory address
        No idea how to implement.  angr has back slicing, but I don't know if that's the same thing
        '''
        pass

    def get_ir(self):
        '''
        Will get the intermediate representation of the binary code
        Use angr->PyVex
        '''
	# Currently returns the IR for only 'main'
	try:
	    import angr, pyvex, r2pipe
            # Use r2 to get the size of main
            r2 = r2pipe.open(self._get_file())
            r2.cmd('aa')
            r2.cmd('bf sym.main')
            size = int(str(r2.cmd('b')),16)
            # Create angr project from file
            proj = angr.Project(self._get_file())
            begin = proj.entry
            # Note end of main
            end = begin + size
            # Load first block
            irsb = proj.factory.block(begin).vex
            loc = begin
            results = {}
            i = 1
            # Get and print blocks until end of main is reached or block size is 0
            while (loc < end) and irsb.size is not 0:
                results[i] = []
                irsb = proj.factory.block(loc).vex
                for stmt in irsb.statements:
                    results[i].append(stmt)
                loc += irsb.size
                i += 1
            #print results
            return results

        except ImportError:
            print "[-] Error loading dependencies: angr, pyvex, r2pipe required"
            print "[-] Do you have them installed?"
            
        return

    def decompile(self):
        '''
        Will decompile the binary file into source code
        Use radeco/retdec-python/boomerang/snowman ?  I haven't been able to install any of them successfully thus far
        '''
	import subprocess
	from subprocess import call
	import os

	file = self._get_file()

	path = os.path.expanduser('~')
	os.chdir(path)

	p = subprocess.Popen(['ls'], stdout = subprocess.PIPE)
	p2 = subprocess.Popen(['grep', 'boomerang'], stdin = p.stdout, stdout = subprocess.PIPE)
	
	folder = p2.stdout.readline()

	if folder != "":
	    folder = folder.rstrip('\n')

	    path = os.path.join(os.path.expanduser('~'), folder)
	    os.chdir(path)

	    path = os.path.join(os.path.expanduser('~'), 'FoRREST', 'outputs')
	    call(["./boomerang" , "-o", path , file])

	else:
	    print "Boomerang not found. Process Terminated"

        return

    def get_stack_frames(self):
        '''
        Will return the stack frames built by the program during execution
        Maybe add params to allow users to only check stack frames built by a given function?
        See angr->Program State.  Maybe have it write the program state every time a function is called?
        '''
        pass

    def get_packet_captures(self):
        '''
        Record all attempts to send data over a network, including the data
        Use Linux tcpdump?
        '''
        pass

    def symbolic_exec(self):
        '''
        Perform a symbolic execution to determine potential results
        Use angr's symbolic execution engine
        wtf should this return? Should it be interactive?
        '''
        pass

    def deobfuscate(self):
        '''
        Deobfuscate the binary
        No idea how to implement this
        Return a deobfuscated disassembly/decompilation?
        '''
        pass

    def taint_analysis(self):
        '''
        Peform a dynamic taint analysis to determine what data can be corrupted by user input and how that input is used
        Will probably involve data references/slicing
        Return list of memory addresses that are tainted, the instruction where they are tainted, and the instructions that use the tainted data ?
        '''
        pass
