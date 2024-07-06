# Introduction to Python

Welcome to the introduction to Python! This guide will walk you through the basics of Python programming.

## Table of Contents
1. [What is Python?](#what-is-python)
2. [Setting Up Python](#setting-up-python)
3. [Basic Syntax](#basic-syntax)
4. [Variables and Data Types](#variables-and-data-types)
5. [Basic Operators](#basic-operators)
6. [Control Flow](#control-flow)
7. [Functions](#functions)
8. [Lists and Tuples](#lists-and-tuples)
9. [Dictionaries](#dictionaries)
10. [File Handling](#file-handling)
11. [Conclusion](#conclusion)

## What is Python?
Python is a high-level, interpreted programming language known for its easy readability and versatile use cases. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

## Setting Up Python
1. **Download Python:** Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python.
2. **Install Python:** Follow the installation instructions for your operating system.
3. **Verify Installation:** Open your terminal or command prompt and type:
    ```sh
    python --version
    ```

## Basic Syntax
Python uses indentation to define blocks of code. Here’s a simple example:

```python
print("Hello, World!")
print("halo")
```

## Functions
Functions เป็นส่วนสำคัญใน Python ที่ช่วยให้เราสามารถระบุกลุ่มของคำสั่งที่ต้องการทำซ้ำๆ 

### Example 1 ฟังก์ชันสำหรับบวกเลข

```python
def add_numbers(a, b):
    """ฟังก์ชันสำหรับบวกเลข a และ b"""
    sum = a + b
    return sum

# เรียกใช้งานฟังก์ชัน
result = add_numbers(5, 3)
print("ผลรวม:", result)  # ผลลัพธ์คือ 8
```

### Example 2 ฟังก์ชันสำหรับคำนวณความยาวด้านของสามเหลี่ยมตามหลักพีทาโกรัส

```python

def calculate_triangle_hypotenuse(a, b):
    hypotenuse = (a**2 + b**2)**0.5
    return round(hypotenuse, 2)

# ตัวอย่างการใช้งานฟังก์ชัน
side1 = 3
side2 = 4
hypotenuse = calculate_triangle_hypotenuse(side1, side2)
print(f"ความยาวด้านของสามเหลี่ยมที่มีด้านที่หนึ่งเท่ากับ {side1} และด้านที่สองเท่ากับ {side2} คือ {hypotenuse} เซนติเมตร")
```