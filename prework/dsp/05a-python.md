# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

**Lists and tuples are both data structures which have an ordered sequence of objects. But lists are mutable while tuples are not.  This means the elements of a list can be edited directly.**

```python
>>> my_list = [0, 1, 2]
>>> my_list[0] = 3
>>> print my_list
[3, 1, 2]
```

**Since tuples are immutable, they are also hashable.  This allows Python to look up dictionary values faster with tuples than with lists.  For this reason, tuples can be keys in dictionaries, while lists cannot.**

```python
>>> my_tup = ('haq', 'hasan')   
>>> my_dict = {my_tup: "312-555-1212"}
>>> my_dict[('haq', 'hasan')]
'312-555-1212'
```
---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

**Lists and sets are both mutable data structures.  However, the elements within a set are immutable and unordered.  A set cannot be indexed.**

```python
>>> my_set = set(['one', 'two', 'three'])
>>> my_set.add("four")
>>> my_set
set(['four', 'three', 'two', 'one'])
>>> my_set[0]
TypeError: 'set' object does not
            support indexing
```
**Because the elements within a set are hashable, they are more efficient for lookups (like tuples).**

**Also, sets cannot contain duplicates.**
```python
>>> my_set.add("one")
>>> my_set
set(['four', 'three', 'two', 'one'])
```

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

**The *lambda* function allow you to call an anonymous function at runtime. This function has no name and therefore cannot be called outside of the code that is being executed.  It is often used when working with iterators to avoid nested loops and therefore speed up code.**

**The *key* argument in *sorted()* tells the function which attribute to sort on.  We can use a lambda function in this for a quick and easy way to specify the attribute.**

```python
>>> data  = [("John", "Male"), ("Jenny", "Female"), ("Alex", "Male"),
... ("Tammy", "Female"), ("Mike", "Male")]
>>> sorted(data, key = lambda x: (x[1], x[0]))
[('Jenny', 'Female'), ('Tammy', 'Female'), ('Alex', 'Male'), ('John', 'Male'),
('Mike', 'Male')]
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

<ul>
<li><b>List comprehensions* are a way to quickly construct a list from other lists without having to use nested loops.
<li>The map() and filter() functions are also helpful in creating new lists quickly.  They do not allow for iteration with loops which limits their functionality.
<li>With a pre-defined function (not lambda), map() and filter() functions have tested to be slightly faster than list comprehension.</b>
</ul>

**DEMONSTRATE LIST COMPREHENSION = MAP()**
```python
>>> oldlist = range(1,11)
>>> oldlist
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> newlist1 = [x*2 for x in oldlist]
>>> newlist1
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> newlist2 = map(lambda x: x*2, oldlist)
>>> newlist2
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

**DEMONSTRATE LIST COMPREHENSION = FILTER()**
```python
>>> newlist1 = [x for x in oldlist if x % 2 == 0]
>>> newlist1
[2, 4, 6, 8, 10]
>>> newlist2 = filter(lambda x: x % 2 == 0, oldlist)
>>> newlist2
[2, 4, 6, 8, 10]
```

**DEMONSTRATE SET COMPREHENSION**
```python
>>> oldset = set(range(1,11))
>>> oldset
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
>>> newset1 = set(x*2 for x in oldset)
>>> newset1
set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
```

**DEMONSTRATE DICTIONARY COMPREHENSION**
```python
>>> olddict = {'a': 1, 'b': 2, 'c': 3}
>>> olddict
{'a': 1, 'c': 3, 'b': 2}
>>> newdict1 = {k: v*2 for (k, v) in olddict.iteritems()}
>>> newdict1
{'a': 2, 'c': 6, 'b': 4}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

**937 days**

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

**513 days**

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

**7,850 days**

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

**DONE**

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

**DONE**

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)

**DONE**
