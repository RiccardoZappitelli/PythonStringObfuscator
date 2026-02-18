"""
Module docstring: this should be obfuscated too.
"""

import math

GLOBAL_MESSAGE = "Global string constant"
RAW_PATH = r"C:\Users\kim\Desktop\project\file.txt"
BYTE_DATA = b"\x48\x65\x6c\x6c\x6f"

def greet(name):
    """Function docstring with sensitive info."""
    local_message = "Hello"
    return f"{local_message}, {name}! Pi ~= {math.pi:.4f}"

def string_ops():
    a = "alpha"
    b = "beta"
    c = "gamma"

    combined = a + "-" + b + "-" + c
    formatted = "Value: {}".format(12345)
    percent_fmt = "Hex: %x" % 255

    multi = """This is a
multi-line
string literal."""

    raw = r"\n should not become newline"

    return combined, formatted, percent_fmt, multi, raw

def byte_test():
    header = b"HEAD"
    payload = b"\xde\xad\xbe\xef"
    return header + payload

def edge_cases():
    empty = ""
    single_char = "X"
    unicode_str = "προσπάθεια 🚀"
    escaped = "Line1\nLine2\tTabbed"
    return empty, single_char, unicode_str, escaped

if __name__ == "__main__":
    print("Starting test execution...\n")

    print("GLOBAL:", GLOBAL_MESSAGE)
    print("RAW_PATH:", RAW_PATH)
    print("BYTE_DATA:", BYTE_DATA)

    print("\nGREET:", greet("kim"))

    results = string_ops()
    print("\nSTRING OPS:")
    for r in results:
        print("  ->", r)

    print("\nBYTE TEST:", byte_test())

    print("\nEDGE CASES:")
    for r in edge_cases():
        print("  ->", r)

    print("\nTest completed successfully.")

