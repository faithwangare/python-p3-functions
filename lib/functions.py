#!/usr/bin/env python3
def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

greet("Guido")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()


def add(num1, num2):
    sum = num1 + num2
    return sum

add(45, 55)

def halve(number):
    return number / 2

halve(100)