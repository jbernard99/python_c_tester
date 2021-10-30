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

START = "#include<stdio.h>\nint main(){"
END = "return (0);}"
LEN = "int len = "
P_LEN = 'printf("::%d", len);'

class PrintfTest:
	def __init__(self, func, *args):
		self.format = f'("{str(args[0])}"'
		self.args = [arg for arg in args[1:]]
		self.func = func
		self._format()
		self._write_main()
		self.compile()
		self.result = self.run_exec()
		print(self.result)

	def _format(self):
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
		with open("main.c", "w") as f:
			f.write(f"{START}{LEN}{self.func}{self.format}{P_LEN}{END}")

	def compile(self):
		global GCC
		subprocess.run(GCC)

	def run_exec(self):
		global EXEC_FILENAME
		string = subprocess.run(["./" + EXEC_FILENAME], capture_output=True)
		return(f">> {str(string.stdout)[2:-1]}")

if __name__ == "__main__":
	string = format("Allo %c %d", 'q', 42)
	write_main(string, "printf")
	compile()
	run_exec()
