import os

def squared(n: int) -> int:
    return n * n

def print_multiple_times(text: str):
    print(text)
    print(text)

def main():
    print_multiple_times(f"Hello there {squared(10)} !!!")
    print("Hello world from Daftcode!")
