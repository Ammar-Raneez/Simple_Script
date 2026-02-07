## SimpleScript v1.0.0 [![SimpleScript](https://github.com/Ammar-Raneez/Simple_Script/actions/workflows/simplescript.yml/badge.svg)](https://github.com/Ammar-Raneez/Simple_Script/actions/workflows/simplescript.yml)

<p align="center">
      <img src="https://raw.githubusercontent.com/Ammar-Raneez/Simple_Script/refs/heads/main/misc/image_2022-01-21_11-25-43_resized.png" />
</p>

SimpleScript is a basic command language that supports saving and accessing of variables, conditional statements, loops, and functions.

## Please Note
Python version 3 will be required to run

## Quick Start
On your command line enter
```commandline
python main.py
```

## Features
* Ability to define and call functions with parameters
* Ability to VAR and load a variable
* The variable can take mathematical expressions as a value, which will be evaluated first
* Support for conditional statements (IF/ELIF/ELSE)
* Support for loops (FOR and WHILE)
* Error logs and tracebacks pointing out the location at which the error was caused 

## Accepted Commands
To define a variable
```commandline
VAR
```

To access a variable
```commandline
SHOW
```

To define a function
```commandline
FUNC
```

## Syntax
### Variable Assignment
```commandline
VAR identifier = expression
```

### Variable Access
```commandline
SHOW identifier
```

### Function Definition
There are two ways to define functions:

**Named function (preferred):**
```commandline
FUNC function_name(param1, param2, ...) -> expression
```

**Anonymous function assigned to variable:**
```commandline
VAR variable_name = FUNC(param1, param2, ...) -> expression
```

### Function Call
```commandline
function_name(arg1, arg2, ...)
```

### Conditionals
```commandline
IF condition THEN expression ELIF condition THEN expression ELSE expression
```

### For Loop
```commandline
FOR identifier = start TO end STEP increment THEN expression
```

### While Loop
```commandline
WHILE condition THEN expression
```

## Examples
### Basic Variables
```commandline
VAR A = 10
10

SHOW A
10

VAR A = 10*(10+5)
150

VAR B = 10^2
100

VAR C = 2 == 2 AND 4 == 5
0

VAR D = 2 == 2 AND 5 == 5
1

VAR E = IF 2==5 THEN 2 ELIF 3==5 THEN 3 ELSE 5
5

VAR F = 10+5
15

VAR G = F + 5
20

SHOW A
150

SHOW B
100

SHOW C
0

SHOW D
1

SHOW E
5

SHOW F
15

SHOW G
20
```

### Functions
```commandline
FUNC add(a, b) -> a + b
<function ADD>

add(5, 3)
8

FUNC square(x) -> x * x
<function SQUARE>

square(7)
49

FUNC abs_val(x) -> IF x < 0 THEN -x ELSE x
<function ABS_VAL>

abs_val(-15)
15

FUNC formula(a, b, c) -> a^2 + b^2 + c^2
<function FORMULA>

formula(3, 4, 5)
50

FUNC multiply(x, multiplier) -> x * multiplier
<function MULTIPLY>

VAR result = multiply(5, 10)
50

SHOW result
50
```

### Loops
```commandline
VAR A = 1
1
FOR i=1 TO 6 THEN VAR A = A*i
SHOW A
120

VAR A = 1
1
FOR i=5 TO 0 STEP -1 THEN VAR A = A*i
SHOW A
120

VAR A = 1
1
WHILE A < 50 THEN VAR A = A+1
SHOW A
50
```

### Errors
```commandline
VARA 10
Invalid Syntax: Expected Keyword, '+', '-' or '('
File <stdin>, line 1

VARA 10
^^^^^^^^

VAR A
Invalid Syntax: Expected Keyword, '+', '-' or '('
File <stdin>, line 1

VAR A
      ^
      
SHOW C
Traceback (most recent call last):
  File <stdin>, line 1, in <simplescript>
Runtime Error: 'c' is not defined

SHOW C
```

## Repl
https://replit.com/@ammarraneez/SimpleScript
