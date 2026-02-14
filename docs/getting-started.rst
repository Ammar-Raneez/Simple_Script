Getting Started
===============

Installation
------------

From PyPI (when published)::

    pip install simplescript-lang

From source::

    git clone https://github.com/Ammar-Raneez/Simple_Script.git
    cd Simple_Script
    pip install -e .

Running the REPL
----------------

Start the interactive REPL::

    simplescript

Or::

    python -m simplescript

Running a Script
----------------

Create a file with the ``.simc`` extension::

    # example.simc
    VAR x = 10
    VAR y = 20
    SHOW x
    SHOW y

Run it::

    simplescript example.simc

Basic Usage
-----------

Variables
~~~~~~~~~

Assign variables with ``VAR`` and access them with ``SHOW``::

    VAR name = "Alice"
    VAR age = 25
    SHOW name
    SHOW age

Functions
~~~~~~~~~

Define functions with ``FUNC``::

    FUNC add(a, b) -> a + b
    add(5, 3)

    VAR square = FUNC(x) -> x * x
    square(7)

Conditionals
~~~~~~~~~~~~

Use ``IF``/``ELIF``/``ELSE``::

    VAR result = IF 5 > 3 THEN "yes" ELSE "no"

Loops
~~~~~

For loops::

    VAR sum = 0
    FOR i=1 TO 11 THEN VAR sum = sum + i

While loops::

    VAR count = 0
    WHILE count < 10 THEN VAR count = count + 1

Lists
~~~~~

Create and manipulate lists::

    VAR numbers = [1, 2, 3, 4, 5]
    VAR first = numbers / 0
    VAR extended = numbers + 6
    VAR removed = numbers - 2
    
    VAR list1 = [1, 2]
    VAR list2 = [3, 4]
    VAR combined = list1 * list2

Maps
~~~~

Create and manipulate maps::

    VAR person = {"name": "Alice", "age": 25}
    VAR name = person / "name"
    VAR updated = person + {"city": "NYC"}
    VAR removed = person - "age"
    
    VAR map1 = {"a": 1}
    VAR map2 = {"b": 2}
    VAR merged = map1 * map2
