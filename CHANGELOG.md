# Changelog

All notable changes to SimpleScript will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-02-14

### Added
- List data structure with square bracket syntax `[1, 2, 3]`
- List operations: append (`+`), remove by index (`-`), extend (`*`), get by index (`/`)
- Support for empty lists, nested lists, and mixed-type lists
- 24 comprehensive unit tests for list functionality
- List example scripts: `lists_basic.simc`, `lists_operations.simc`, `lists_advanced.simc`
- List documentation in README, language reference, and getting started guide
- Map (dictionary) data structure with JSON-like syntax `{"key": value}`
- Map operations: get value (`/`), add/update (`+`), remove key (`-`), merge (`*`)
- Support for empty maps, nested maps, and maps with any value types
- 20 comprehensive unit tests for map functionality
- Map example scripts: `maps_basic.simc`, `maps_operations.simc`, `maps_advanced.simc`
- Map documentation in README, language reference, and getting started guide

## [2.0.0] - 2026-02-08

### Added
- Complete project restructuring into a proper Python package
- Full type hint coverage across all modules
- Google-style docstrings for all classes and public methods
- Sphinx documentation with API reference
- CLI entry point (`simplescript` command) with REPL and file execution
- `pyproject.toml` for modern Python packaging
- String type with single/double quotes and escape character support
- Function definitions (named and anonymous) with parameter support
- Variable assignment now requires `=` sign (`VAR x = 10`)
- Comprehensive test suite with 53 integration tests
- CONTRIBUTING.md with development guidelines

### Changed
- Reorganized flat file structure into `simplescript/` package with submodules
- Moved types into `simplescript/types/` to avoid naming conflicts with Python stdlib
- Renamed `parse.py` to `parser.py` to follow conventions
- Renamed `string_type.py` to `string.py` (now safe inside `types/` package)
- Renamed `value.py` to `base.py` (clearer purpose)
- Improved test organization with descriptive test classes

### Fixed
- Circular import between `function.py` and `interpreter.py`
- Escape character handling in string lexer
- Single quote string support
- Function call parsing (was bypassing `call()` method)
- Tuple unpacking bug in `make_minus_or_arrow` lexer method
