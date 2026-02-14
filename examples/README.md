# SimpleScript Examples

This directory contains example scripts demonstrating various features of SimpleScript.

## Running Examples

Run any example with:
```bash
simplescript examples/example_name.simc
```

Or:
```bash
python3 -m simplescript examples/example_name.simc
```

## Available Examples

### Basic Examples

#### `arithmetic.simc`
Demonstrates basic arithmetic operations:
- Addition, subtraction, multiplication, division
- Power/exponentiation
- Variable usage in expressions

```bash
simplescript examples/arithmetic.simc
```

#### `strings.simc`
Shows string operations:
- String literals
- Concatenation with `+`
- Repetition with `*`
- String variables

```bash
simplescript examples/strings.simc
```

#### `functions.simc`
Function definitions and usage:
- Named functions
- Function calls
- Functions with conditionals
- Absolute value, max functions

```bash
simplescript examples/functions.simc
```

#### `loops.simc`
Loop constructs:
- FOR loops (sum, factorial)
- WHILE loops (countdown)

```bash
simplescript examples/loops.simc
```

#### `lists_basic.simc`
List literals and basic usage:
- Integer lists
- String lists
- Mixed type lists
- Empty lists
- Nested lists

```bash
simplescript examples/lists_basic.simc
```

#### `lists_operations.simc`
List operations:
- Appending elements with `+`
- Removing elements with `-`
- Extending lists with `*`
- Accessing elements with `/`

```bash
simplescript examples/lists_operations.simc
```

#### `lists_advanced.simc`
Advanced list usage:
- Lists with functions
- Lists in conditionals
- Using loops with lists

```bash
simplescript examples/lists_advanced.simc
```

### Advanced Examples

#### `comprehensive_demo.simc`
A comprehensive demonstration showing:
- Variables and arithmetic
- Functions
- Loops
- Conditionals
- String operations
- All major language features

```bash
simplescript examples/comprehensive_demo.simc
```

#### `string_operations.simc`
Advanced string handling:
- Escape sequences (`\n`, `\t`)
- Single and double quotes
- String concatenation
- String functions

```bash
simplescript examples/string_operations.simc
```

#### `loops_and_conditionals.simc`
Complex control flow:
- FOR loops with STEP
- WHILE loops
- IF/ELIF/ELSE conditionals
- Combining loops with conditionals

```bash
simplescript examples/loops_and_conditionals.simc
```

## Creating Your Own Scripts

1. Create a file with `.simc` extension
2. Write SimpleScript code
3. Run with `simplescript your_file.simc`

### Template

```simplescript
VAR x = 10
VAR y = 20

FUNC add(a, b) -> a + b

add(x, y)
```

## Language Syntax Quick Reference

### Variables
```simplescript
VAR name = value
```

### Functions
```simplescript
FUNC name(param1, param2) -> expression
```

### Conditionals
```simplescript
IF condition THEN value1 ELSE value2
IF condition THEN value1 ELIF condition2 THEN value2 ELSE value3
```

### Loops
```simplescript
FOR identifier = start TO end THEN expression
FOR identifier = start TO end STEP increment THEN expression
WHILE condition THEN expression
```

### Operators
- Arithmetic: `+`, `-`, `*`, `/`, `^` (power)
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `AND`, `OR`, `NOT`
- String: `+` (concatenation), `*` (repetition)
- List: `+` (append), `-` (remove), `*` (extend), `/` (index)

## Tips

- Each statement returns a value (displayed when run in a script)
- Use `SHOW variable` in REPL to display variable values
- Strings can use single or double quotes
- Functions can reference themselves for recursion (use anonymous functions)
- No semicolons needed

## Need More Help?

- See `QUICKSTART.md` for detailed syntax guide
- See `README.md` for installation and overview
- See `docs/` for full documentation
- See `grammar.txt` for formal grammar specification
