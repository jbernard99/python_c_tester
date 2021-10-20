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

def compile():
	global GCC
	subprocess.call(GCC)

def run_exec():
	global EXEC_FILENAME
	subprocess.call(["./" + EXEC_FILENAME]) 

if __name__ == "__main__":
	compile()
	run_exec()
	print("Done!")
	print("Hello c'est teddy!")
