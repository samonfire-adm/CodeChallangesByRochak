# Python Sets Operations

## Problem Statement
This problem focuses on performing various operations on sets in Python. You will be required to:

1. Find the union of two sets.
2. Find the intersection of two sets.
3. Find the difference between two sets.

## How to Solve

### 1. Find Union of Two Sets
To find the union of two sets, use the `union()` method or the `|` operator. The union of two sets is a set containing all elements from both sets, without duplicates.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using union() method
union_set = set1.union(set2)

# Using | operator
union_set = set1 | set2
```

### 2. Find Intersection of Two Sets
To find the intersection of two sets, use the `intersection()` method or the `&` operator. The intersection of two sets is a set containing only the elements that are common to both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using intersection() method
intersection_set = set1.intersection(set2)

# Using & operator
intersection_set = set1 & set2
```

### 3. Find Difference of Two Sets
To find the difference between two sets, use the `difference()` method or the `-` operator. The difference of two sets is a set containing elements that are in the first set but not in the second.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using difference() method
difference_set = set1.difference(set2)

# Using - operator
difference_set = set1 - set2
```

## Solution
[Link to the solution code](#)

## Video Solution
[Link to the video explanation](#)

## Homework Question

### 1. Find Union of Three Sets
To find the union of three sets, use the `union()` method or the `|` operator.

```python
set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}

# Using union() method
union_set = set1.union(set2).union(set3)

# Using | operator
union_set = set1 | set2 | set3
```

### 2. Find Intersection of Three Sets
To find the intersection of three sets, use the `intersection()` method or the `&` operator.

```python
set1 = {1, 2}
set2 = {2, 3}
set3 = {2, 4}

# Using intersection() method
intersection_set = set1.intersection(set2).intersection(set3)

# Using & operator
intersection_set = set1 & set2 & set3
```

### 3. Find Difference of Three Sets
To find the difference between three sets, use the `difference()` method or the `-` operator.

```python
set1 = {1, 2, 3, 4}
set2 = {2, 3}
set3 = {3, 4}

# Using difference() method
difference_set = set1.difference(set2).difference(set3)

# Using - operator
difference_set = set1 - set2 - set3
```


## Solution
[Link to the solution code](#)

## Video Solution
[Link to the video explanation](#)
