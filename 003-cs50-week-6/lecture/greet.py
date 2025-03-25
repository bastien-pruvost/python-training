from sys import argv

if (len(argv) > 1):
    print(f"Hello, {argv[1]}")
else:
    print("Usage: 'python greet.py {name}'")
