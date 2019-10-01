# Conditionals
- [Conditionals](#conditionals)
  - [Comparing values](#comparing-values)
  - [If](#if)
  - [else](#else)
  - [elif](#elif)
- [Examples](#examples)
  - [Simple IF](#simple-if)
  - [Multiple Conditions in one if statement](#multiple-conditions-in-one-if-statement)
- [Exercise](#exercise)

In most software, we want an action to happen, if some condition is satisfied. The way we think about this is: 

>Only do **X** if *Y* condition is true

## Comparing values
Below is a table containing the Comparison signs we use in python. Those signs should be used in statements that require a comparison.

| Comparing Sign |      Meaning         |
|:--------------:|:--------------------:|
| ==             | equals               |
| >              | Greater than         |
| >=             | Greater or equal     |
| <              | Less than            |
| <=             | Less or equal        |

You can also add two keywords to include more than one condition in the statement:

- **and**: Adds another condition, and both conditions have to be true
- **or**: Adds another condition, and at least one of the conditions have to be true


## If
We use this everyday in our life, in many different places:

- You can **eat some candy** if you *eat your lunch*
- I will **schedule a meeting for today** if i *have a free time on my agenda*

In python, we use a syntax like the following:

```python
if condition:
  action()
```
Using it in an simple example, we can ask for the user age, and say if the user is allowed to drive, or not, based on the age:

```python
age = int(input('what is your age'))

if age > 18:
  print('You can drive')
```

## else

But, what if the user does not meet the condition? Should we add another *if* statement? We could, but there is a better way to do it.

The *else* statement is used to represent the case when the *if* statement is false, or when the condition is not fulfilled.

> Remember: The else statement does not have a condition

Updating the driving example:

```python
age = int(input('what is your age'))

if age > 18:
  print('You can drive')
else:
  print('Sorry, you can't drive')
```
In this way, we make it very clear which message will be shown to the user.

## elif
Okay, *if* for a condition, and *else* for when the condition is not fulfilled. But what i should i do if i have more than one case?
You could create multiple *if*s, but doing this way you will need one *else* statement for every case.

But we do have a better way to do this. we can use one, or multiple, *elif* statements. elif means "else if", and it allows you to check multiple conditions, if the last one was not successfull

The *elif* statement will be placed between the *if* and the *esle* statements:

```python
age = int(input('what is your age'))

if age > 18:
  print('You can drive')
elif age == 18:
  print('you can also drive')
else:
  print('Sorry, you can't drive')
```

# Examples

## Simple IF
Check if one condition is true

```python
# Declaring variables to compare
a = 10
b = 20

# Comparing
if a < b:
  print('a is greater than b')

```

## Multiple Conditions in one if statement
This is used when you need multiple conditions to enter the *if* or *elif* block:

```python
# Declaring variables to compare
a = 10
b = 20
c = 30

if a < b and a < c:
  print('a is has the lowest value')
```
>You can add multiple conditions using the keyword *and*.

# Exercise
> The exercise is an update of the last class exercise. Your *main.py* file already has the complete exercise from the last class.

Update the exercise from last class to show a message to the user, based on the average number of cups of coffee taken:

| < 5        | 5    | > 5                |
|:----------:|:----:|:------------------:|
| Drink more | Good | You drank too much |
