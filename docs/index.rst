SimpleScript Documentation
==========================

SimpleScript is a simple programming language interpreter that supports
variables, conditional statements, loops, functions, and string operations.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting-started
   language-reference
   api/index


Getting Started
---------------

Install SimpleScript::

    pip install simplescript-lang

Or run from source::

    git clone https://github.com/Ammar-Raneez/Simple_Script.git
    cd Simple_Script
    python -m simplescript


Quick Example
-------------

Start the REPL and try these expressions::

    simplescript > VAR x = 10 + 5
    15
    simplescript > FUNC square(n) -> n * n
    <function SQUARE>
    simplescript > square(x)
    225


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
