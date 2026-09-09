## Python for Loop

What is a for loop?

A for loop is used to repeat code for each item or for a known number of times.

When should I use a for loop?

## Use a for loop when:

* You know how many times you want to repeat the code.
* You want to go through every item in a list.
* You want to go through characters in a string.
* You want to work with a range().
* You already know what you want to repeat or what items you want to process.

⸻

## Basic Syntax:

```python

for variable in sequence:
    # code to repeat
```


## Example 1: Repeat a Code

```python

for i in range(5):
    print("Hello")

The code runs 5 times.
```

⸻

## Example 2: Work with a List
```python

names = ["Ram", "Shyam", "Hari"]
for name in names:
    print(name)

The loop takes each name from the list one by one.
```
⸻

## Example 3: Work with a String

``` python

word = "Python"
for letter in word:
    print(letter)

The loop prints each letter one by one.
```
⸻

## Example 4: Use range()

``` python
for number in range(1, 6):
    print(number)

Output:

1
2
3
4
5
```
⸻

## Easy Rule

Use for when you know WHAT you want to go through or HOW MANY times you want to repeat.

## Think:

FOR = “How many?” / “What items?”

⸻

## Common Situations

Situation	Use for?
Repeat 10 times	✅ Yes
Print numbers 1–100	✅ Yes
Go through a list	✅ Yes
Go through a string	✅ Yes
Process every item in a collection	✅ Yes
Number of repetitions is known	✅ Yes

⸻

## Golden Rule

If you know the items or the number of repetitions, think for first.