# Call by Object

Python is neither "**call by value**" or "**call by reference**".

Let's see this example:

```python
def func(x):
	x.append(0)
    x = [1]
    
y = [0]
func(y)

print(y)
```

If it's "**call by value**", the output should by `[0]`. 

On the other hand, "**call by reference**" gives `[1]`.

However, the real output is `[0,0]`.

In the `func(x)`, the variable `x` points to the object connected to variable `y`. The object can be changed, so `[0]` -> `[0,0]` with `x.append(0)`. 

In the statement `x=[1]`, the variable `x` is assigned to a different object, so result of `print(y)` stays `[0,0].`