import subprocess

class Interpret:

    def __init__(self, idamous):
        self.idamous = idamous
        self.filename = self.idamous.get_file()


    def get_opcodes(self):
        cmd = ['objdump']
        cmd.append('-d')
        cmd.append(self.filename)

        terminal_output = []

        output = subprocess.Popen(cmd, stdout = subprocess.PIPE)

        return terminal_output

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
					'55',
					'4889e5',
					'4883ec20',
					etc
				]
	"""
	pass

	def get_strings(self):
		cmd = ['strings']
		cmd.append(self.filename)

		terminal_output = []

		output = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	
		while True:
			line = output.stdout.readline()
			if line != "":
				line = line.rstrip()
				terminal_output.append(line)
			else:
				break

		return terminal_output

	pass

	def get_imports(self):
		cmd = ['nm']
		cmd.append('-C')
		cmd.append('--dynamic')
		cmd.append(self.filename)

		cmd2 = ['grep']
		cmd2.append(' U ')

		terminal_output = []

		process1 = subprocess.Popen(cmd, stdout = subprocess.PIPE)
		process2 = subprocess.Popen(cmd2, stdin = process1.stdout, stdout = subprocess.PIPE)

		while True:
			line = process2.stdout.readline()
			if line != "":
				line = line.lstrip(' ')
				line = line.rstrip()
				data = line.split(' ')
				terminal_output.append(data[1])
			else:
				break

		return terminal_output

	pass


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
	pass

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
		"""
	pass

