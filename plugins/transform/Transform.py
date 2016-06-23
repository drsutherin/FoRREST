
class Transformed:
	
	def __init__(self, idamous):
		self.idamous = idamous
	
	def _get_file(self):
		return self.idamous.get_file()
		
	def get_disassembly(self):
		pass
	
	def get_mnemonics(self):
		pass
	
	def get_functions(self):
		pass
	
	def get_basic_blocks(self):
		pass

	def get_data_references(self):
		pass
	
	def get_jump_targets(self):
		pass
	
