#!/bin/bash
# Setup script for SimpleScript development environment

set -e  # Exit on error

echo "🚀 Setting up SimpleScript..."
echo ""

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Please run this from the project root."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install package in editable mode
echo "📥 Installing SimpleScript..."
pip install -e .

# Install dev dependencies
echo "📥 Installing dev dependencies (Sphinx, flake8, etc.)..."
pip install -e ".[dev]"

# Run tests
echo ""
echo "🧪 Running tests..."
python -m unittest discover tests -v

# Check installation
echo ""
echo "✅ Setup complete!"
echo ""
echo "SimpleScript version:"
simplescript --version

echo ""
echo "📚 Next steps:"
echo ""
echo "  1. Activate virtual environment (do this in every new terminal):"
echo "     source venv/bin/activate"
echo ""
echo "  2. Run the REPL:"
echo "     simplescript"
echo ""
echo "  3. Run examples:"
echo "     simplescript examples/arithmetic.simc"
echo ""
echo "  4. Build documentation:"
echo "     cd docs && sphinx-build -b html . _build/html"
echo ""
echo "  5. Run tests:"
echo "     python -m unittest discover tests -v"
echo ""
