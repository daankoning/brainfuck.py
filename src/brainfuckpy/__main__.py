import brainfuckpy
import sys


def main():
	if len(sys.argv) == 1:
		pgrm = sys.stdin.read()
		brainfuckpy.brainfuck(pgrm)


if __name__ == '__main__':
	main()