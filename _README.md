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
## คำสั่ง if,else
ใช้สำหรับการตัดสินใจแบบมีเงื่อนไข
ตรวจสอบเงื่อนไข และดำเนินการตามเงื่อนไขนั้นๆ
สามารถมี else เพิ่มเติมเพื่อกำหนดการทำงานเมื่อเงื่อนไขไม่เป็นจริง
```python
age = int(input("กรุณาใส่จำนวนปี: "))

if age >= 18:
  print("คุณมีสิทธิ์เลือกตั้ง")
else:
  print("คุณยังไม่มีสิทธิ์เลือกตั้ง")
```
## คำสั่ง elif
ใช้สำหรับการตรวจสอบเงื่อนไขเพิ่มเติมในคำสั่ง if
ตรวจสอบเงื่อนไขถัดไปหากเงื่อนไขแรกไม่เป็นจริง
จะมีเพียงหนึ่งบล็อกจาก if หรือ elif ที่ทำงานเท่านั้น
```python
grade = int(input("กรุณาใส่คะแนน: "))

if grade >= 90:
  print("เยี่ยมยอด!")
elif grade >= 80:
  print("ดีมาก!")
else:
  print("สู้ต่อไป!")
```
## วนรอบ for
ใช้สำหรับการวนซ้ำผ่านลำดับข้อมูล
ทำงานกับแต่ละไอเท็มในลำดับวนซ้ำ
```python
fruits = ["แอปเปิ้ล", "กล้วย", "เชอร์รี่"]

for fruit in fruits:
  print(fruit)
```
## วนรอบ while
ใช้สำหรับการวนซ้ำตราบใดที่เงื่อนไขยังเป็นจริง
ทำซ้ำบล็อกโค้ดจนกว่าเงื่อนไขจะไม่เป็นจริง
```python
x = 1

while x < 6:
  print(x)
  x += 1
```