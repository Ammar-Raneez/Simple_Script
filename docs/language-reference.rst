Language Reference
==================

Grammar
-------

SimpleScript follows this grammar, ordered by operator precedence
(lowest to highest):

.. code-block:: text

    expr        : KEYWORD:VAR IDENTIFIER EQ expr
                | comp-expr ((KEYWORD:AND|KEYWORD:OR) comp-expr)*

    comp-expr   : NOT comp-expr
                | arith-expr ((EE|LT|GT|LTE|GTE) arith-expr)*

    arith-expr  : term ((PLUS|MINUS) term)*

    term        : factor ((MUL|DIV) factor)*

    factor      : (PLUS|MINUS) factor
                | power

    power       : call (POW factor)*

    call        : atom (LPAREN (expr (COMMA expr)*)? RPAREN)?

    atom        : INT | FLOAT | STRING | IDENTIFIER
                | LPAREN expr RPAREN
                | if-expr | for-expr | while-expr | list-expr | map-expr | func-def

    if-expr     : KEYWORD:IF expr KEYWORD:THEN expr
                  (KEYWORD:ELIF expr KEYWORD:THEN expr)*
                  (KEYWORD:ELSE expr)?

    for-expr    : KEYWORD:FOR IDENTIFIER EQ expr KEYWORD:TO expr
                  (KEYWORD:STEP expr)? KEYWORD:THEN expr

    while-expr  : KEYWORD:WHILE expr KEYWORD:THEN expr
    
    list-expr   : LSQUARE (expr (COMMA expr)*)? RSQUARE
    
    map-expr    : LBRACE (expr COLON expr (COMMA expr COLON expr)*)? RBRACE

    func-def    : KEYWORD:FUNC IDENTIFIER?
                  LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN
                  ARROW expr


Data Types
----------

Numbers
~~~~~~~

Integers and floating-point numbers::

    42
    3.14
    -7

Strings
~~~~~~~

Single or double quoted, with escape sequence support::

    "hello world"
    'single quotes work too'
    "escaped \"quotes\""
    "newline\\nhere"
    "tab\\there"

Lists
~~~~~

Ordered collections of values::

    [1, 2, 3, 4, 5]
    ["hello", "world"]
    [1, "two", 3.5]
    []
    [[1, 2], [3, 4]]

Maps
~~~~

Key-value dictionaries::

    {"name": "Alice", "age": 25}
    {"x": 10, "y": 20}
    {}
    {"outer": {"inner": 42}}

Operators
---------

Arithmetic: ``+``, ``-``, ``*``, ``/``, ``^``

Comparison: ``==``, ``!=``, ``<``, ``>``, ``<=``, ``>=``

Logical: ``AND``, ``OR``, ``NOT``

String: ``+`` (concatenation), ``*`` (repetition)

List: ``+`` (append), ``-`` (remove by index), ``*`` (extend), ``/`` (get by index)

Map: ``+`` (add/update), ``-`` (remove key), ``*`` (merge), ``/`` (get value)

Keywords
--------

``VAR``, ``SHOW``, ``IF``, ``THEN``, ``ELIF``, ``ELSE``,
``FOR``, ``TO``, ``STEP``, ``WHILE``, ``FUNC``, ``AND``, ``OR``, ``NOT``
