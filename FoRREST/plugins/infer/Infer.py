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
