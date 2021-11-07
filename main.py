import printf_test

TESTS = [
	["42 Quebec"],
	["%d Quebec", 42],
	["%d %x %X %c %s", 42, 42, 42,'c', "42"],
	["%c Quebec", '4']
]

TESTS = [
	'''"42 Quebec"''',
	'''"%d Quebec", 42''',
	'''"%d %x %X %c %s", 42, 42, 42,'c', "42"''',
	""""%c Quebec", '4'"""
]

# tests_format = julienfunction(TESTS)

for i, test in enumerate(TESTS):
	print(f"test {i}: ", end="")
	printf_test.PrintfTest(test)
# printf_test.PrintfTest("Allo %c %d", 'q', 42);

if __name__ == "__main__":
	pass
