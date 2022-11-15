# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Nothing is happening

👉 What is the problem here? Why is nothing happening?

```python
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

areaOfTriangle (5, 22)
```

<details> <summary> 👀 Answer </summary>

We need to assign a variable to `areaOfTriangle` and `print` it out.
```python
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

area = areaOfTriangle (5, 22)
print(area)
```


</details>

## Name Error

👉 Why is it saying area is not defined!? We see it inside the subroutine.


```python
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

areaOfTriangle (5, 22)
print(area)
```

<details> <summary> 👀 Answer </summary>

- This is where we see a concept called scope. Scope is a variable only available from *inside* the region it was created.
- Variables that are created for the first time in a subroutine are *only* available inside that subroutine.
- We cannot call the  variable `area` *outside* the subroutine.
- We need to create the variable `area` *inside* the subroutine.

```python
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

area = areaOfTriangle (5, 22)
print(area)
```

</details>