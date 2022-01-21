## SimpleScript v1.0.0-beta

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

SHOW A
150

SHOW B
100

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
```

## Limitations
* A variable can only have alphabetical characters
* Running from a script is not supported yet (Will be added on v1.0.0)

## Repl
https://replit.com/@ammarraneez/SimpleScript
