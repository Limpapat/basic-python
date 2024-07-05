# Introduction to Python

Welcome to the introduction to Python! This guide will walk you through the basics of Python programming.

## Table of Contents
- [Introduction to Python](#introduction-to-python)
  - [Table of Contents](#table-of-contents)
  - [What is Python?](#what-is-python)
  - [Setting Up Python](#setting-up-python)
  - [Basic Syntax](#basic-syntax)
  - [Basic Operators](#basic-operators)
    - [ตัวดำเนินการพื้นฐานในภาษา Python](#ตัวดำเนินการพื้นฐานในภาษา-python)
    - [1. ตัวดำเนินการทางคณิตศาสตร์](#1-ตัวดำเนินการทางคณิตศาสตร์)
    - [2. ตัวดำเนินการเปรียบเทียบ](#2-ตัวดำเนินการเปรียบเทียบ)

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