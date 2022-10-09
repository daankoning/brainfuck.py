import brainfuckpy
from rich.console import Console
import time

console = Console()

CODE_ACCENT = "bold red"
TAPE_ACCENT = "bold red"


def _clear():
	console.print("\033c", end="")


def write_visualization(program: str, tape: list[int], code_pointer: int, head_position: int):
	"""Writes a single cycle of the visualization, means clearing and displaying the information."""
	_clear()

	# print the tape
	tape_with_highlight = [i for i in tape]
	tape_with_highlight[head_position] = f"[{TAPE_ACCENT}]{tape[head_position]}[/{TAPE_ACCENT}]"
	console.print(", ".join(str(i) for i in tape_with_highlight[:30]))  # FIXME: BAD bodge

	console.print("\n"*2)

	# print the program
	program_str = program[:code_pointer] + f"[{CODE_ACCENT}]" + program[code_pointer] + f"[/{CODE_ACCENT}]" + program[code_pointer+1:]
	console.print(program_str)

	time.sleep(0.1)

