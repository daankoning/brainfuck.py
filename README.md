# brainfuck.py
A simple lightweight pure python brainfuck interpreter and visualizer. 

## Installation
The package is available on PyPI, as such simply run:

    $ pip install brainfuckpy

## Usage
Basic can be used by simply providing the command line tool with a brainfuck program. Either by piping it in, by passing it as an argument or by passing a file containing a program. As such these are all valid and equivalent uses:

    $ python -m brainfuckpy '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'

    $ cat hello.bf | python -m brainfuckpy

    $ python -m brainfuckpy hello.bf
Additionally, the evaluation may be visualized by adding the `-vis` flag.

If more control is required the package also gives access to the underlying functions. In general, passing the program to `brainfuckpy.brainfuck` should cover 90% of usecases. The other 10% should be solveable by calling `brainfuckpy.evaluate_processed` and changing the callbacks it uses (see documentation).

## Future development
- Compiling _to_ brainfuck.
- Better documentation