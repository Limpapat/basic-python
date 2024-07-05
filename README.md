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
```

## Variables and Data Types
ตัวแปร:
ตัวแปรคือที่เก็บค่าข้อมูล ใน Python คุณสามารถสร้างตัวแปรได้โดยการกำหนดค่าให้กับชื่อ ตัวอย่างเช่น:

```python
x = 5
name = "Alice"
```

ในที่นี้ `x` และ `name` เป็นตัวแปรที่เก็บค่าจำนวนเต็ม 5 และสตริง "Alice" ตามลำดับ

ประเภทข้อมูล:
Python มีประเภทข้อมูลที่มีอยู่แล้วหลายประเภท ที่พบบ่อยที่สุดคือ:

1. จำนวนเต็ม (int): ตัวเลขที่ไม่มีทศนิยม เช่น 5, -3, 1000
2. จำนวนทศนิยม (float): ตัวเลขที่มีจุดทศนิยม เช่น 3.14, -0.5, 2.0
3. สตริง (str): ข้อความที่อยู่ในเครื่องหมายคำพูด เช่น "สวัสดี", 'Python'
4. บูลีน (bool): ค่าความจริง True หรือ False
5. ลิสต์ (List): คอลเลกชันที่เรียงลำดับได้และแก้ไขได้ เช่น [1, 2, 3]
6. ทูเพิล (Tuple): คอลเลกชันที่เรียงลำดับได้แต่แก้ไขไม่ได้ เช่น (1, 2, 3)
7. พจนานุกรม (Dictionary): คู่ของคีย์และค่า เช่น {"ชื่อ": "Alice", "อายุ": 30}

คุณสามารถตรวจสอบประเภทของตัวแปรโดยใช้ฟังก์ชัน `type()`:

```python
x = 5
print(type(x))  # ผลลัพธ์: <class 'int'>

y = "สวัสดี"
print(type(y))  # ผลลัพธ์: <class 'str'>
```
