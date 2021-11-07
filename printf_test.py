import sys 
import subprocess 
import os 

EXEC_FILENAME = "a.out"
C_FILENAME = ["main.c"]
GCC = [
	"gcc",
	"-Wall",
	"-Werror",
	"-Wextra",
] + C_FILENAME

START = "#include<stdio.h>\nint main(){int len = 0;"
END = "return (0);}"
SEP = 'printf("|||");'
P_LEN = 'printf("::%d", len);'

class PrintfTest:
	def __init__(self, *args):
		self.format = f'({str(args[0])}'
		self.args = [arg for arg in args[1:]]
		self._format()
		self.func = "len=printf"
		self.funccomp = "len=printf"
		self._write_main()
		self.compile()
		self.return_ = self.run_exec()
		self.split = str(self.return_).split("|||")
		self.compare()

	def _format(self, *args):
		for arg in self.args:
			if (isinstance(arg, int)):
				self.format += f", {str(arg)}"
			elif (isinstance(arg, str) and len(arg) == 1):
				self.format += f", '{str(arg)}'"
			elif (isinstance(arg, str)):
				self.format += f', "{str(arg)}"'
		self.format += ");"

	def _write_main(self):
		global START
		global END
		global SEP
		with open("main.c", "w") as f:
			f.write(f"{START}{self.func}{self.format}{P_LEN}{SEP}{self.funccomp}{self.format}{P_LEN}{END}")

	def compile(self):
		global GCC
		subprocess.run(GCC)

	def run_exec(self):
		global EXEC_FILENAME
		string = subprocess.run(["./" + EXEC_FILENAME], capture_output=True)
		return(f"{str(string.stdout)[2:-1]}")
	
	def __repr__(self):
		return(self.return_)
	
	def compare(self):
		if (self.split[0] == self.split[1]):
			print("PASSED")
		else:
			print(f"expected: {self.splt[0]} - returned: {self.split[1]}")

if __name__ == "__main__":
	string = format("Allo %c %d", 'q', 42)
	write_main(string, "printf")
	compile()
	run_exec()
