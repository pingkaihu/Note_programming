## Python 2 vs Python 3

There are some differences between Python 2 and Python 3.

#### Print function

In Python 2, the print function works like:
```
	print 'Hello World!'
```
In Python 3,
```
	print('Hello World!')
```
It seems that it's more convenient to print something in Python 2, and Python 3 asks you to do extra work. 
However, it's easier to print multiple items in Python 3, For example,
```
	a = 2
    print('a =', a)
```

#### Range

In Python 2, `range()` creates a list. 
In Python 3, `range()` has the same function in a `for` loop, but it's equivalent to `xrange()` in Python 2 in order to save memory usage.
The way to create a list by `range()` is as follow:
```
	a = list(range(10))
```

#### `int` or `float` output during division

In Python 2, one `int` divided by another `int` always gives you an integer output. For example,
```
	print 5/2
    >>> 2
```
In Python 3, it could be a `float` output:
```
	print(5/2)
    >>> 2.5
```