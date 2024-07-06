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

## Basic Operators
### ตัวดำเนินการพื้นฐานในภาษา Python

Python เป็นภาษาการเขียนโปรแกรมที่มีพลังและมีตัวดำเนินการหลากหลายเพื่อทำงานต่าง ๆ นี่คือตัวดำเนินการพื้นฐานที่คุณต้องรู้สำหรับผู้เริ่มต้น:

### 1. ตัวดำเนินการทางคณิตศาสตร์
ตัวดำเนินการทางคณิตศาสตร์ใช้สำหรับทำงานทางคณิตศาสตร์ เช่น การบวก การลบ การคูณ และการหาร

- **การบวก (`+`)**: บวกสองจำนวนเข้าด้วยกัน
  ```python
  a = 5
  b = 3
  result = a + b  # ผลลัพธ์คือ 8

- **การลบ (`-`)**: ลบจำนวนที่สองจากจำนวนแรก
  ```python
  result = a - b  # ผลลัพธ์คือ 2

- **การคูณ (`*`)**: คูณสองจำนวนเข้าด้วยกัน
  ```python
  result = a * b  # ผลลัพธ์คือ 15

- **การหาร (`/`)**: หารจำนวนแรกด้วยจำนวนที่สอง
  ```python
  result = a / b  # ผลลัพธ์คือ 1.666...

- **การหารปัดเศษลง (`//`)**: หารจำนวนแรกด้วยจำนวนที่สองและปัดลงเป็นจำนวนเต็มที่ใกล้ที่สุด
  ```python
  result = a // b  # ผลลัพธ์คือ 1

- **การหารเอาเศษ (`%`)**: คืนค่าที่เหลือจากการหารจำนวนแรกด้วยจำนวนที่สอง 
  ```python 
  result = a % b  # ผลลัพธ์คือ 2

- **การยกกำลัง (`**`)**: ยกจำนวนแรกเป็นกำลังของจำนวนที่สอง
  ```python 
  result = a ** b  # ผลลัพธ์คือ 125

### 2. ตัวดำเนินการเปรียบเทียบ
ตัวดำเนินการเปรียบเทียบใช้เปรียบเทียบค่าสองค่าและคืนค่า True หรือ False

- **เท่ากับ (`==`)**: ตรวจสอบว่าค่าสองค่ามีค่าเท่ากันหรือไม่
  ```python
  result = (a == b)  # ผลลัพธ์คือ False

- **ไม่เท่ากับ (`!=`)**: ตรวจสอบว่าค่าสองค่าไม่เท่ากันหรือไม่
  ```python
  result = (a != b)  # ผลลัพธ์คือ True

- **มากกว่า (`>`)**: ตรวจสอบว่าค่าแรกมากกว่าค่าที่สองหรือไม่
  ```python
  result = (a > b)  # ผลลัพธ์คือ True

- **น้อยกว่า (`<`)**: ตรวจสอบว่าค่าแรกน้อยกว่าค่าที่สองหรือไม่
  ```python
  result = (a < b)  # ผลลัพธ์คือ False

- **มากกว่าหรือเท่ากับ (`>=`)**: ตรวจสอบว่าค่าแรกมากกว่าหรือเท่ากับค่าที่สองหรือไม่
  ```python
  result = (a >= b)  # ผลลัพธ์คือ True

- **น้อยกว่าหรือเท่ากับ (`<=`)**: ตรวจสอบว่าค่าแรกน้อยกว่าหรือเท่ากับค่าที่สองหรือไม่
  ```python
  result = (a <= b)  # ผลลัพธ์คือ False

### 3. ตัวดำเนินการทางตรรกะ
ตัวดำเนินการทางตรรกะใช้ในการรวมเงื่อนไขต่าง ๆ เข้าด้วยกัน

- **AND (`and`)**: คืนค่า True ถ้าเงื่อนไขทั้งสองเป็นจริง
  ```python
  result = (a > 0 and b < 5)  # ผลลัพธ์คือ True

- **OR (`or`)**: คืนค่า True ถ้าเงื่อนไขหนึ่งในสองเป็นจริง
  ```python
  result = (a > 0 or b > 5)  # ผลลัพธ์คือ True

- **NOT (`not`)**: กลับค่าของเงื่อนไข
  ```python
  result = not(a > 0)  # ผลลัพธ์คือ False

### 4. ตัวดำเนินการกำหนดค่า
ตัวดำเนินการกำหนดค่าใช้ในการกำหนดค่าตัวแปร

- **กำหนดค่า (`=`)**: กำหนดค่าด้านขวาให้กับตัวแปรด้านซ้าย
  ```python
  a = 5

- **บวกและกำหนดค่า (`+=`)**: บวกค่าด้านขวากับตัวแปรด้านซ้ายและกำหนดผลลัพธ์ให้กับตัวแปรด้านซ้าย
  ```python
  a += 3  # เท่ากับ a = a + 3, ดังนั้น a จะเป็น 8

- **ลบและกำหนดค่า (`-=`)**: ลบค่าด้านขวาจากตัวแปรด้านซ้ายและกำหนดผลลัพธ์ให้กับตัวแปรด้านซ้าย
  ```python
  a -= 3  # เท่ากับ a = a - 3, ดังนั้น a จะเป็น 5

- **คูณและกำหนดค่า (`*=`)**: คูณตัวแปรด้านซ้ายด้วยค่าด้านขวาและกำหนดผลลัพธ์ให้กับตัวแปรด้านซ้าย
  ```python
  a *= 3  # เท่ากับ a = a * 3, ดังนั้น a จะเป็น 15

- **หารและกำหนดค่า (`/=`)**: หารตัวแปรด้านซ้ายด้วยค่าด้านขวาและกำหนดผลลัพธ์ให้กับตัวแปรด้านซ้าย
  ```python
  a /= 3  # เท่ากับ a = a / 3, ดังนั้น a จะเป็น 5.0

- **หารเอาเศษและกำหนดค่า (`%=`)**: หารเอาเศษจากตัวแปรด้านซ้ายด้วยค่าด้านขวาและกำหนดผลลัพธ์ให้กับตัวแปรด้านซ้าย
  ```python
  a %= 3  # เท่ากับ a = a % 3, ดังนั้น a จะเป็น 2.0

- **ยกกำลังและกำหนดค่า (`**=`)**: ยกตัวแปรด้านซ้ายเป็นกำลังของค่าด้านขวาและกำหนดผลลัพธ์ให้กับตัวแปรด้านซ้าย
  ```python
  a **= 3  # เท่ากับ a = a ** 3, ดังนั้น a จะเป็น 8.0

- **หารปัดเศษลงและกำหนดค่า (`//=`)**: หารตัวแปรด้านซ้ายด้วยค่าด้านขวา ปัดลงเป็นจำนวนเต็มที่ใกล้ที่สุด และกำหนดผลลัพธ์ให้กับตัวแปรด้านซ้าย
  ```python
  a //= 3  # เท่ากับ a = a // 3, ดังนั้น a จะเป็น 2.0

### 5. ตัวดำเนินการอัตลักษณ์ (Identity Operators)
ใช้สำหรับการเปรียบเทียบว่าวัตถุสองอย่างเป็นวัตถุเดียวกันหรือไม่

- **Is ('is')** : เหมือนกัน
  ```python
  5 is 5  # ผลลัพธ์ คือ True
  4 is 5  # ผลลัพธ์ คือ False

- **Is not ('is not')** : ไม่เหมือนกัน
  ```python
  5 is not 5  # ผลลัพธ์ คือ False
  4 is not 5  # ผลลัพธ์ คือ Ture
  
### 6. Membership operators (ตัวดำเนินการแบบเป็นสมาชิก)
ใช้สำหรับการตรวจสอบว่าค่าหนึ่งอยู่ในลำดับหรือไม่ 

- **In ('in')** : อยู่ใน
  ```python
  listA = [1,2,3,4]
  2 in listA  # ผลลัพธ์ คือ True
  6 in listA  # ผลลัพธ์ คือ False

- **not In ('not in')** : อยู่ใน
  ```python
  listA = [1,2,3,4]
  2 not in listA  # ผลลัพธ์ คือ False
  6 not in listA  # ผลลัพธ์ คือ True

### 7. ลำดับความสำคัญของ Operator

1. (),[] 
2. !
3. *,/,%
4. +,-
5. <<,>>
6. <, <= , >, >=
7. ==, !=
8. &
9. ^
10. |
  ```python
  4+5*5  # ผลลัพธ์ คือ 29
  (4+5)*5 # ผลลัพธ์ คือ 45