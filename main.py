import printf_test

if __name__ == "__main__":
	return_ = printf_test.PrintfTest("printf", "Allo %c %d", 'q', 42)
	split = str(return_).split("::")
	split[1] = int(split[1])
	print(split)
