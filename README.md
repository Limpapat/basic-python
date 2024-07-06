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

## Lists
 - Lists เป็นโครงสร้างข้อมูลที่ใช้เก็บข้อมูลแบบเรียงลำดับ (ordered sequence)ซึ่งสามารถเปลี่ยนแปลงค่าของสมาชิกภายในได้ (mutable) โดยใช้วงเล็บเหลี่ยม [ ] เพื่อล้อมรอบข้อมูลภายใน
- สามารถมีสมาชิกที่มีประเภทข้อมูลต่างกันได้ในรายการเดียวกัน
- สามารถเพิ่มหรือลบสมาชิกได้โดยใช้เมทอดต่างๆ เช่น append(), insert(), remove(), pop() เป็นต้น
ตัวอย่างการใช้งาน Lists:
```python
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```

# การเข้าถึงข้อมูลประเภทลิสต์ List
- เราสามารถเข้าถึงข้อมูล (Member) แต่ละตัวใน List ได้โดยการอ้างอิงหมายเลขอินเด็กซ์ไว้ภายในเครื่องหมาย [] square brackets โดยหมายเลขอินเด็กซ์จะเริ่มต้นที่ 0
ตัวอย่าง
การเข้าถึงข้อมูล (Member) ใน List
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #banana
```

# การเปลี่ยนแปลงข้อมูลในลิสต์ List
ในการเปลี่ยนค่าของlistเฉพาะให้อ้างอิงกับหมายเลขดัชนี
ตัวอย่าง
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']
```

# การตรวจสอบข้อมูลในลิสต์ List
ในการพิจารณาว่ามี list ที่ระบุอยู่ใน list หรือไม่ โดยใช้คีย์เวิร์ด in
ตัวอย่าง
```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") #Yes, 'apple' is in the fruits list
```

# การเพิ่มสมาชิกใน List
ในการเพิ่มlist ในตอนท้ายของlistให้ใช้วิธีการ append ()
ตัวอย่าง
```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```
# การลบข้อมูลออกจากลิสต์ List
- ลบข้อมูลด้วยเมธอด remove() เราสามารถลบข้อมูลออกจากลิสต์โดยใช้เมธอด remove()โดยมีวิธีใช้งานดังนี้
ตัวอย่าง
```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']
```
## Tuples
- เป็นโครงสร้างข้อมูลที่ใช้เก็บข้อมูลแบบเรียงลำดับ (ordered sequence) เช่นเดียวกับรายการ (lists) แต่ค่าภายในไม่สามารถเปลี่ยนแปลงได้ (immutable) หลังจากที่ถูกสร้างขึ้น
- ใช้วงเล็บวงกลม ( ) เพื่อล้อมรอบข้อมูลภายใน

```python
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10  # ไม่สามารถทำได้ เนื่องจากเป็น immutable
print(my_tuple[0])  # Output: 1
```
# การเข้าถึงสมาชิกภายใน Tuple
- สามารถเข้าถึง tuple โดยอ้างอิงถึงหมายเลขดัชนีภายในเครื่องหมายวงเล็บเหลี่ยม[]
ตัวอย่าง
```python
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #banana
```

# เปลี่ยนค่า Tuple
- เมื่อสร้างtuple นักเรียนจะไม่สามารถเปลี่ยนค่าได้ tupleจะไม่เปลี่ยนแปลงหรือไม่เปลี่ยนรูป แต่มีวิธีแก้ปัญหาคือ นักเรียนสามารถแปลง tuple เป็นlist เปลี่ยนlistและแปลงlistกลับเป็น tuple ได้นั่นเอง
ยกตัวอย่าง
```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) #("apple", "kiwi", "cherry")
```

# ความยาว Tuple
- ในการกำหนดจำนวนlist tuple มีให้ใช้วิธี len () len(ตัวแปรหรือข้อมูล)
ตัวอย่าง
```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #3
```

