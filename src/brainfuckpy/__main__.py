import brainfuckpy
import sys, os, select


def incorrect_usage():
	sys.stdout.write("Incorrect usage: use the -h flag to display a help message. \n")


def help_message():
	sys.stdout.write("""NAME	
	brainfuckpy -- A lightweight pure python brainfuck interpreter

SYNOPSIS
	brainfuckpy [-h] [file|program]

DESCRIPTION
	Either pipe in, provide as an argument or provide a file containing a valid program.
	
	-h, --help
			display this message.\n""")


def main():
	if len(sys.argv) == 1 and select.select([sys.stdin, ], [], [], 0.0)[0]:
		pgrm = sys.stdin.read()
		brainfuckpy.brainfuck(pgrm)
	elif len(sys.argv) == 1:
		incorrect_usage()
	elif os.path.isfile(sys.argv[1]):
		with open(sys.argv[1]) as file:
			pgrm = file.read()
		brainfuckpy.brainfuck(pgrm)
	elif sys.argv[1] in {"-h", "--help"}:
		help_message()
	elif sys.argv[1]:
		pgrm = sys.argv[1]
		brainfuckpy.brainfuck(pgrm)
	else:
		incorrect_usage()


if __name__ == '__main__':
	main()