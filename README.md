# Python String Obfuscator

This project provides a Python AST-based string obfuscator that hides all string literals and byte constants in a centralized encrypted pool. It is designed to prevent static analysis and make reverse engineering of sensitive strings more difficult.

## Features

- Obfuscates string literals, byte strings, and docstrings.
- Handles f-strings correctly, preserving format specifiers.
- Skips critical literals like `"__main__"` to avoid breaking execution.
- Runtime decryption with a centralized pool and per-string random key.
- Compatible with Python 3.13.

## Installation

No installation required. Simply clone or download the script `obfuscator.py` and run it with Python 3.10+.

## Usage

### Command Line

```bash
python obfuscator.py input_script.py output_obfuscated.py
```

- `input_script.py` - your original Python script.
- `output_obfuscated.py` - the generated obfuscated Python script.

### Example

Suppose you have a Python file `example.py`:

```python
# example.py

SECRET = "This is a secret string"

def greet(name):
    return f"Hello {name}, secret: {SECRET}"

if __name__ == "__main__":
    print(greet("Alice"))
```

Obfuscate it:

```bash
python obfuscator.py example.py example_obf.py
```

Now you can run the obfuscated version:

```bash
python example_obf.py
```

Expected output:

```
Hello Alice, secret: This is a secret string
```

Even though the plaintext strings are hidden in the encrypted pool.

## How It Works

1. Parse the Python AST of the target script.
2. Replace all string and byte constants with references to a centralized encrypted pool.
3. Inject a runtime loader function `_l` to decrypt strings when accessed.
4. f-strings are rewritten to concatenate decrypted literals with formatted expressions.

## Notes

- Designed for obfuscation, not full cryptographic security.
- Can be extended with compression, C-level compilation (e.g., Nuitka), or bytecode-level obfuscation for stronger protection.
- Do not obfuscate critical Python literals that affect execution semantics.

## License

MIT License

