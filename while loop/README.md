# Python While Loop Practice

## What is a While Loop?

A `while` loop is used to repeat a block of code **as long as a condition is True**.

Use a while loop when:

* You want the code to continue until something happens.
* You do not know exactly how many times the loop will run.
* The loop depends on a condition.
* You need to wait for a correct input.
* You want a program to keep running while something is True.


### Syntax

```python
while condition:
    # code to repeat
```

## Example 1: Print Numbers

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Output

```text
1
2
3
4
5
```
## How It Works

* The loop starts with `number = 1`.
* The condition checks if `number <= 5`.
* If the condition is `True`, the code runs.
* `number += 1` increases the number by 1.
* The loop stops when the condition becomes `False`.


## Example 2: Condition-Based Loop

number = 1
while number <= 5:
    print(number)
    number += 1

The loop continues while:

number <= 5

is True.

⸻

## Example 3: Ask Until the Correct Password

password = ""
while password != "1234":
    password = input("Enter password: ")
print("Login successful!")

We don’t know how many times the user will enter the wrong password.

So, while is useful here.

## Important: Update the Condition

A while loop must have a way to become False.

Example:

number = 1
while number <= 5:
    print(number)
    number += 1

Here:

number += 1

changes the value and eventually makes the condition False.

⸻

## ⚠️ Infinite Loop

Be careful:

number = 1
while number <= 5:
    print(number)

This can run forever because number never changes.

## Golden Rule

Always make sure a while loop has a way to stop.

⸻

## Easy Rule

Use while when you want to continue UNTIL a condition becomes False.

Think:

WHILE = “Until when?”

⸻

## Common Situations

Situation	Use while?
Continue until the user gives correct input	✅ Yes
Continue while a condition is true	✅ Yes
You don’t know the exact number of repetitions	✅ Yes
Keep a game running	✅ Yes
Keep checking something	✅ Yes
Stop when a condition changes	✅ Yes

⸻

Golden Rule

If you don’t know exactly how many times the loop should run, but you know the condition that should stop it, think while first.

## Important

Always make sure the loop condition can eventually become `False`.

Otherwise, you may create an **infinite loop**.

```python
while True:
    print("This will run forever!")
```

## Topics I Practiced

* Basic `while` loops
* `while` loops with `if/else`
* `break`
* `continue`
* Nested `while` loops
* Sentinel values
* Number patterns and triangles
