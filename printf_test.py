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

def compile():
	global GCC
	subprocess.run(GCC)

def run_exec():
	global EXEC_FILENAME
	string = subprocess.run(["./" + EXEC_FILENAME], capture_output=True)
	print(f">> {str(string.stdout)[2:-1]}")

def format(*args):
	format = f'("{str(args[0])}"'
	for arg in args[1:]:
		if (isinstance(arg, int)):
			format += f", {str(arg)}"
		elif (isinstance(arg, str) and len(arg) == 1):
			format += f", '{str(arg)}'"
		elif (isinstance(arg, str)):
			format += f', "{str(arg)}"'
	format += ");"
	return (format)

def write_main(format, func):
	global START
	global END
	with open("main.c", "w") as f:
		f.write(f"{START} {func}{format} {END}")

if __name__ == "__main__":
	string = format("Allo %c %d", 'q', 42)
	write_main(string, "printf")
	compile()
	run_exec()
