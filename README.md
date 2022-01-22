## SimpleScript v1.0.0-beta [![SimpleScript](https://github.com/Ammar-Raneez/Simple_Script/actions/workflows/simplescript.yml/badge.svg)](https://github.com/Ammar-Raneez/Simple_Script/actions/workflows/simplescript.yml)

<p align="center">
      <img src="https://raw.githubusercontent.com/Ammar-Raneez/Simple_Script/main/misc/image_2022-01-21_11-25-43_resized.png?token=GHSAT0AAAAAABLIBHF66C7HL3U75W4AOM3SYPTQ7NA" />
</p>

SimpleScript is a basic command language that supports variable assignment and access.

## Please Note
Python version 3 will be required to run

## Quick Start
On your command line enter
```commandline
python main.py
```

## Features
* Ability to save and load a variable
* The variable can take mathematical expressions as a value, which will be evaluated first
* Error logs and tracebacks pointing out the location at which the error was caused 

## Accepted Commands
To save a variable
```commandline
SAVE
```

To access a variable
```commandline
SHOW
```

## Examples
```commandline
SAVE A 10
10

SHOW A
10

SAVE A 10*(10+5)
150

SAVE B 10^2
100

SAVE C 2 == 2 AND 4 == 5
0

SAVE D 2 == 2 AND 5 == 5
1

SAVE E IF 2==5 THEN 2 ELIF 3==5 THEN 3 ELSE 5
5

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

SAVEA 10
Invalid Syntax: Expected Keyword, '+', '-' or '('
File <stdin>, line 1

SAVEA 10
^^^^^^^^

SAVE A
Invalid Syntax: Expected Keyword, '+', '-' or '('
File <stdin>, line 1

SAVE A
      ^
      
SHOW C
Traceback (most recent call last):
  File <stdin>, line 1, in <simplescript>
Runtime Error: 'c' is not defined

SHOW C
```

## Repl
https://replit.com/@ammarraneez/SimpleScript
