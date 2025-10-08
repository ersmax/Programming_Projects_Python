from Pig_latin import pig_latin


tests = [
		("hello", "ellohay"),
		("apple", "appleyay"),
		("Hello", "Ellohay"),
		("HELLO", "ELLOHAY"),
		("smile", "ilesmay"),
		("string!", "ingstray!"),
		("...", "..."),
		("123abc", "123abcyay"),
		("eat pie", "eatyay iepay"),
		("My name is AL SWEIGART and I am 4,000 years old.",
		 "Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay."),
	]

def test_pig_latin_conversion():
	for input_text, expected in tests:
		got = pig_latin(input_text)
		wanted = expected
		assert got == wanted
