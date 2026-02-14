## SimpleScript v2.0.0

[![SimpleScript](https://github.com/Ammar-Raneez/Simple_Script/actions/workflows/simplescript.yml/badge.svg)](https://github.com/Ammar-Raneez/Simple_Script/actions/workflows/simplescript.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/ammar-raneez/simplescript/badge)](https://www.codefactor.io/repository/github/ammar-raneez/simplescript)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=Ammar-Raneez_Simple_Script&metric=alert_status)](https://sonarcloud.io/api/project_badges/measure?project=Ammar-Raneez_Simple_Script&metric=alert_status)

<p align="center">
      <img src="https://raw.githubusercontent.com/Ammar-Raneez/Simple_Script/main/misc/image_2022-01-21_11-25-43_resized.png" />
</p>

SimpleScript is a simple programming language interpreter that supports variables, conditional statements, loops, functions, and string operations.

## 📚 Documentation

- **README.md** (this file) - Complete project overview, installation, and usage
- **examples/** - Working code examples demonstrating all features
- **CONTRIBUTING.md** - Development guidelines and architecture
- **CHANGELOG.md** - Version history and changes
- **docs/** - Sphinx documentation (build with `sphinx-build`)
- **grammar.txt** - Formal language grammar specification

## Installation

### Quick Setup (Recommended)

```bash
git clone https://github.com/Ammar-Raneez/Simple_Script.git
cd Simple_Script
./setup.sh
```

This creates a virtual environment and installs everything automatically.

### Manual Installation

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install SimpleScript
pip install -e .

# Install dev dependencies (optional - for Sphinx docs, linting)
pip install -e ".[dev]"
```

### Verify Installation

```bash
simplescript --version
python -m unittest discover tests -v
```

## Quick Start

### Interactive REPL

```bash
# Activate virtual environment first
source venv/bin/activate

# Start REPL
simplescript
# or
python -m simplescript
```

Try these in the REPL:

```simplescript
simplescript > VAR x = 10 + 5
15
simplescript > FUNC square(n) -> n * n
<function SQUARE>
simplescript > square(7)
49
```

### Run Script Files

```bash
# Run example scripts
simplescript examples/arithmetic.simc
simplescript examples/functions.simc
simplescript examples/comprehensive_demo.simc
```

### Use as a Python Library

```python
import simplescript

# Run code
result, error = simplescript.run('<stdin>', 'VAR x = 10 + 5')
if error:
    print(error.as_string())
else:
    print(result)  # 15

# Run multi-line code
code = """
FUNC add(a, b) -> a + b
add(10, 20)
"""
result, error = simplescript.run('<script>', code)
print(result)  # 30
```

## Features

* Variables with `VAR` assignment and `SHOW` access
* Arithmetic expressions with operator precedence
* String type with single/double quotes and escape sequences
* List data structure with indexing and operations
* Named and anonymous function definitions
* Conditional expressions (IF/ELIF/ELSE)
* For and While loops
* Comparison and logical operators
* Error tracebacks with source location highlighting

## Syntax

### Variable Assignment

```
VAR identifier = expression
```

### Variable Access

```
SHOW identifier
```

### Function Definition

Named function (preferred):

```
FUNC function_name(param1, param2, ...) -> expression
```

Anonymous function:

```
VAR function_name = FUNC(param1, param2, ...) -> expression
```

### Function Call

```
function_name(arg1, arg2, ...)
```

### Conditionals

```
IF condition THEN expression ELIF condition THEN expression ELSE expression
```

### For Loop

```
FOR identifier = start TO end STEP increment THEN expression
```

### While Loop

```
WHILE condition THEN expression
```

### Lists
```
[element1, element2, ...]  # List literal
list + element              # Append element
list - index               # Remove element at index
list * other_list          # Extend list with another list
list / index               # Get element at index
```

## Examples

### Variables

```
simplescript > VAR A = 10
10
simplescript > SHOW A
10
simplescript > VAR B = 10*(5+2)
70
```

### Functions

```
simplescript > FUNC add(a, b) -> a + b
<function ADD>
simplescript > add(5, 3)
8
simplescript > FUNC square(x) -> x * x
<function SQUARE>
simplescript > square(7)
49
simplescript > VAR abs_val = FUNC(x) -> IF x < 0 THEN -x ELSE x
<function <anonymous>>
simplescript > abs_val(-15)
15
```

### Strings

```
simplescript > "Hello, " + "World!"
"Hello, World!"
simplescript > "ha" * 3
"hahaha"
simplescript > FUNC greet(name) -> "Hello, " + name
<function GREET>
simplescript > greet("Alice")
"Hello, Alice"
```

### Loops

```
simplescript > VAR A = 1
1
simplescript > FOR i=1 TO 6 THEN VAR A = A*i
simplescript > SHOW A
120
```

### Lists
```
simplescript > VAR mylist = [1, 2, 3]
[1, 2, 3]
simplescript > mylist + 4
[1, 2, 3, 4]
simplescript > mylist / 0
1
simplescript > [10, 20, 30] - 1
[10, 30]
simplescript > [1, 2] * [3, 4]
[1, 2, 3, 4]
```

### Errors

```
simplescript > VAR A = 10/0
Traceback (most recent call last):
  File <stdin>, line 1, in <simplescript>
Runtime Error: Division by zero

simplescript > SHOW undefined
Traceback (most recent call last):
  File <stdin>, line 1, in <simplescript>
Runtime Error: 'UNDEFINED' is not defined
```

## Project Structure

```
simplescript/
├── core/           # Lexer, parser, interpreter, constants
├── types/          # Runtime value types (Number, String, Function)
├── ast/            # AST node definitions
├── tokens/         # Token and Position classes
├── errors/         # Error class hierarchy
├── utils/          # Symbol table, result trackers, utilities
├── runtime.py      # Main run() entry point
└── cli.py          # Command-line interface
tests/              # Test suite
docs/               # Sphinx documentation
```

## Examples

See the `examples/` directory for ready-to-run scripts:

- `arithmetic.simc` - Basic math operations
- `strings.simc` - String handling
- `functions.simc` - Function definitions
- `loops.simc` - FOR and WHILE loops
- `comprehensive_demo.simc` - All features combined

Run with: `simplescript examples/<filename>.simc`

## Development

### Setup Development Environment

```bash
# Run setup script (creates venv, installs dependencies)
./setup.sh

# Or manually
source venv/bin/activate
pip install -e ".[dev]"
```

### Run Tests

```bash
# All tests
python -m unittest discover tests -v

# Specific test class
python -m unittest tests.test_integration.TestFunctionsNamed -v
```

### Build Documentation

```bash
# Requires dev dependencies
cd docs
sphinx-build -b html . _build/html
open _build/html/index.html  # macOS
# or: xdg-open _build/html/index.html  # Linux
```

### Code Quality

```bash
# Lint code
flake8 simplescript --count --max-line-length=127 --statistics

# Check for syntax errors
flake8 simplescript --count --select=E9,F63,F7,F82 --show-source
```

## Documentation

- **Examples**: See `examples/` directory
- **API Docs**: Build with Sphinx (see Development section)
- **Grammar**: See `grammar.txt` for formal specification
- **Contributing**: See `CONTRIBUTING.md`
- **Changelog**: See `CHANGELOG.md`

## Troubleshooting

### Command not found: simplescript

Make sure virtual environment is activated:

```bash
source venv/bin/activate
```

Or use: `python -m simplescript`

### Installation errors

Try recreating the virtual environment:

```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## License

[MIT License](LICENSE)

## Links

- **GitHub**: https://github.com/Ammar-Raneez/SimpleScript
- **Issues**: https://github.com/Ammar-Raneez/SimpleScript/issues
