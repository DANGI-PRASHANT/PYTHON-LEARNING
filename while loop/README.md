# Python While Loop Practice

## What is a While Loop?

A `while` loop is used to repeat a block of code **as long as a condition is True**.

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
