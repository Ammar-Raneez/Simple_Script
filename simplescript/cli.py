"""Command-line interface for the SimpleScript interpreter.

Provides the interactive REPL (Read-Eval-Print Loop) and file execution
capabilities for SimpleScript.
"""

import sys
import simplescript
from simplescript.__version__ import __version__


def repl() -> None:
    """Start the SimpleScript interactive REPL.

    Continuously reads input from the user, evaluates it, and prints
    the result or error. Exit with Ctrl+C or Ctrl+D.
    """
    print(f'SimpleScript v{__version__} - Interactive REPL')
    print('Type your expressions below. Press Ctrl+C to exit.\n')

    while True:
        try:
            text = input('simplescript > ')
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye!')
            break

        if not text.strip():
            continue

        result, error = simplescript.run('<stdin>', text)
        if error:
            print(error.as_string())
        elif result:
            print(result)


def run_file(file_path: str) -> None:
    """Execute a SimpleScript file.

    Reads the file and executes each line sequentially.

    Args:
        file_path: Path to the .simc file to execute.
    """
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue

        result, error = simplescript.run(file_path, line)
        if error:
            print(error.as_string())
            sys.exit(1)
        elif result:
            print(result)


def main() -> None:
    """Main entry point for the SimpleScript CLI.

    Usage:
        simplescript              Start the interactive REPL
        simplescript <file.simc>  Execute a SimpleScript file
        simplescript --version    Show version information
        simplescript --help       Show usage information
    """
    if len(sys.argv) == 1:
        repl()
    elif sys.argv[1] in ('--version', '-v'):
        print(f'SimpleScript v{__version__}')
    elif sys.argv[1] in ('--help', '-h'):
        print('Usage: simplescript [options] [file]')
        print()
        print('Options:')
        print('  -h, --help     Show this help message')
        print('  -v, --version  Show version information')
        print()
        print('If no file is provided, starts the interactive REPL.')
        print('Supported file extension: .simc')
    else:
        run_file(sys.argv[1])


if __name__ == '__main__':
    main()
