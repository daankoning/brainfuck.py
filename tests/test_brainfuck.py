from unittest import TestCase
from src.brainfuckpy import brainfuck


class TestBrainfuck(TestCase):
	def setUp(self):
		self.output_cache = []
		self.input_cache = iter([])
		self.output_callback = lambda x: self.output_cache.append(chr(x))
		self.input_callback = lambda: ord(next(self.input_cache))

	def test_get_matching_brackets(self):
		self.assertEqual(
			({0: 1, 7: 10, 4: 15}, {1: 0, 10: 7, 15: 4}),
			brainfuck.get_matching_brackets("[]>>[.+[..]<<--]")
		)

	def test_strip_bad_characters(self):
		self.assertEqual(
			"[]>>[.+[..]<<--]--",
			brainfuck.strip_bad_characters("[a]>>[.;\n \t  'a' +[.hi.]<<--] Robert'); DROP TABLE Students;--")
		)

	def test_evaluate_processed(self):
		brainfuck.evaluate_processed(
			"++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.",
			output_callback=self.output_callback
		)
		self.assertEqual(list("Hello World!\n"), self.output_cache)

		self.output_cache = []
		self.input_cache = iter("Hello, world!")
		brainfuck.evaluate_processed(
			"+++++++++++++[>,.<-]",
			input_callback=self.input_callback,
			output_callback=self.output_callback
		)
		self.assertEqual(list("Hello, world!"), self.output_cache)