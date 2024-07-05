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

ตัวแปรและชนิดข้อมูลใน Python:

### 1. ตัวแปร (Variables):

a. การสร้างและกำหนดค่าให้ตัวแปร:

```python
age = 25 #Integer
name = "สมชาย" #String
is_student = True #Boolean
height = 175.5 #Float
```

b. การเปลี่ยนชนิดข้อมูลของตัวแปร:

```python
x = 10
print(type(x))  # <class 'int'>
x = "สิบ"
print(type(x))  # <class 'str'>
x = 10 
x = str(x)
print(type(x)) # จะได้ "10" ที่เป็น String
```

c. กฎการตั้งชื่อตัวแปร:

- สามารถใช้ตัวอักษร ตัวเลข และขีดล่าง (_) ในการตั้งชื่อตัวแปรได้ แต่ต้องไม่ขึ้นต้นด้วยตัวเลข เช่น 123name = "" คือไม่ถูกต้อง
      
- ต้องขึ้นต้นด้วยตัวอักษรหรือขีดล่างก็ได้
      
- ห้ามใช้คำสงวน (reserved words) ของ Python เช่น class, def, if, for, while, etc.

```python
valid_name  "ถูกต้อง"
_also_valid  "ถูกต้องเช่นกัน"
name123  "ถูกต้อง"
# 123name  "ไม่ถูกต้อง"  # ขึ้นต้นด้วยตัวเลข
# class  "ไม่ถูกต้อง"  # class เป็นคำสงวน
```

d. ความแตกต่างระหว่างตัวพิมพ์ใหญ่และเล็ก:

```python
name = "สมชาย"
Name = "สมหญิง"
NAME = "สมศรี"
print(name, Name, NAME)  # สมชาย สมหญิง สมศรี
```

e. การใช้ type hints:

```python
age: int = 25
name: str = "สมชาย"
is_student: bool = True
height: float = 175.5
```

f. การกำหนดค่าหลายตัวแปรพร้อมกัน:

```python
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# การสลับค่าระหว่างสองตัวแปร
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

g. การใช้ตัวแปรในการคำนวณ:

```python
width = 5
height = 3
area = width * height
print(f"พื้นที่: {area}")  # พื้นที่: 15

count = 10
count += 5  # เท่ากับ count = count + 5
print(count)  # 15
```

h. ตัวแปรที่อ้างอิงถึงฟังก์ชันหรือเมธอด:

```python
def greet(name):
      return f"สวัสดี, {name}!"

say_hello = greet
print(say_hello("สมชาย"))  # สวัสดี, สมชาย!
```

   i. การใช้ตัวแปรกับ list comprehension:

```python
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers]
print(squared)  # [1, 4, 9, 16, 25]
```

   j. ตัวแปรแบบ global และ local:

```python
global_var = "ฉันเป็นตัวแปร global"

def test_function():
      local_var = "ฉันเป็นตัวแปร local"
      print(global_var)  # สามารถเข้าถึงตัวแปร global ได้
      print(local_var)

test_function()
print(global_var)  # สามารถเข้าถึงตัวแปร global ได้
# print(local_var)  # จะเกิด error เพราะไม่สามารถเข้าถึงตัวแปร local นอกฟังก์ชันได้
```

   k. การใช้ตัวแปรกับ f-strings:

```python
name = "สมชาย"
age = 30
message = f"สวัสดี, ฉันชื่อ {name} อายุ {age} ปี"
print(message)  # สวัสดี, ฉันชื่อ สมชาย อายุ 30 ปี
```

### 2. ชนิดข้อมูล (Data Types):
   
a. จำนวนเต็ม (int):

- ใช้เก็บตัวเลขจำนวนเต็มบวก ลบ หรือศูนย์
- สามารถทำการคำนวณทางคณิตศาสตร์ได้
- สามารถใช้ underscore เพื่อทำให้ตัวเลขอ่านง่ายขึ้น

```python
a = 10
b = -5
c = a + b  # c จะมีค่าเท่ากับ 5
large_number = 1_000_000  # เทียบเท่ากับ 1000000
```

b. จำนวนทศนิยม (float):

- ใช้เก็บตัวเลขที่มีจุดทศนิยม
- มีความแม่นยำจำกัด อาจเกิดข้อผิดพลาดในการคำนวณได้

```python
pi = 3.14159
result = 1.1 + 2.2  # อาจไม่ได้ 3.3 พอดี เนื่องจากข้อจำกัดของ float
```

c. สตริง (str):

- ใช้เก็บข้อความ
- สามารถใช้เครื่องหมาย ' หรือ " ล้อมรอบได้
- สามารถทำการต่อสตริง (concatenation) และทำซ้ำ (repetition) ได้
- สามารถใช้ f-strings เพื่อจัดรูปแบบสตริงได้สะดวก

```python
greeting = "สวัสดี"
name = 'คุณ'
message = greeting + " " + name  # "สวัสดี คุณ"
repeat = "เฮ" * 3  # "เฮเฮเฮ"
formatted = f"{greeting}, {name}!"  # "สวัสดี, คุณ!"
```

d. บูลีน (bool):

- มีค่าเพียงสองค่าคือ True และ False
- ใช้ในการตัดสินใจและการควบคุมการทำงานของโปรแกรม
- สามารถใช้ร่วมกับ boolean operators (and, or, not)

```python
is_student = True
has_passed = False
can_graduate = is_student and has_passed
is_eligible = not has_passed or is_student
```

e. ลิสต์ (List):

- เก็บข้อมูลหลายๆ ค่าในลำดับที่กำหนด
- สามารถแก้ไข เพิ่ม หรือลบสมาชิกได้ (mutable)
- ใช้วงเล็บเหลี่ยม [ ]
- สามารถใช้ list comprehension ได้

```python
fruits = ["แอปเปิ้ล", "กล้วย", "ส้ม"]
fruits.append("มะม่วง")  # เพิ่ม "มะม่วง" เข้าไปในลิสต์
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

f. ทูเพิล (Tuple):

- คล้ายกับลิสต์ แต่ไม่สามารถแก้ไขค่าภายในได้ (immutable)
- ใช้วงเล็บกลม ( )

```python
coordinates = (10, 20)
# coordinates[0] = 30  # จะเกิด error เพราะไม่สามารถแก้ไขค่าใน tuple ได้
```

g. พจนานุกรม (Dictionary):

- เก็บข้อมูลในรูปแบบคู่ของ key และ value
- ใช้วงเล็บปีกกา { }

```python
student = {"ชื่อ": "อลิซ", "อายุ": 20, "คะแนน": 85.5}
print(student["ชื่อ"])  # แสดงผล: อลิซ
student["วิชา"] = "Python"  # เพิ่ม key-value pair
del student["คะแนน"]  # ลบ key-value pair
```

h. เซต (Set):

- คอลเลกชันของสมาชิก
- ไม่มีลำดับที่แน่นอน
- ใช้วงเล็บปีกกา { } หรือฟังก์ชัน set()

```python
unique_numbers = {1, 2, 3, 3, 4, 4, 5}  # {1, 2, 3, 4, 5}
```

i. None:

- ค่าพิเศษที่ใช้แทนการไม่มีค่าหรือค่า null

```python
result = None
```
      
### การตรวจสอบและแปลงชนิดข้อมูล:
    ```python
    x = 10
    y = "Hello"
    z = [1, 2, 3]

    print(type(x))  # <class 'int'>
    print(type(y))  # <class 'str'>
    print(type(z))  # <class 'list'>

    a = int("5")  # แปลงสตริงเป็นจำนวนเต็ม
    b = float("3.14")  # แปลงสตริงเป็นจำนวนทศนิยม
    c = str(42)  # แปลงจำนวนเต็มเป็นสตริง
    ```
