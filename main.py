class SampleClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"SampleClass with value: {self.value}"

    def __repr__(self):
        return f"SampleClass({self.value})"

    def __len__(self):
        return len(self.value)

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __delitem__(self, key):
        del self.value[key]

    def __iter__(self):
        return iter(self.value)

    def __next__(self):
        if not self.value:
            raise StopIteration
        return self.value.pop()

    def __call__(self, x):
        return self.value + x

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        return SampleClass(self.value + other.value)

    def __sub__(self, other):
        return SampleClass(self.value - other.value)

    def __mul__(self, other):
        return SampleClass(self.value * other.value)

    def __div__(self, other):  # Note: The __div__ method is for Python 2, use __truediv__ for Python 3.
        return SampleClass(self.value / other.value)


# Creating objects and using the dunder methods
obj1 = SampleClass([1, 2, 3])
obj2 = SampleClass([4, 5, 6])

# __init__
print(obj1)  # Output: SampleClass with value: [1, 2, 3]

# __str__
print(str(obj1))  # Output: SampleClass with value: [1, 2, 3]

# __repr__
print(repr(obj1))  # Output: SampleClass([1, 2, 3])

# __len__
print(len(obj1))  # Output: 3

# __getitem__
print(obj1[1])  # Output: 2

# __setitem__
obj1[1] = 10
print(obj1)  # Output: SampleClass with value: [1, 10, 3]

# __delitem__
del obj1[1]
print(obj1)  # Output: SampleClass with value: [1, 3]

# __iter__ and __next__
for item in obj1:
    print(item)  # Output: 1, 3

# __call__
print(obj1(5))  # Output: [1, 3, 5]

# __eq__, __lt__, __gt__
print(obj1 == obj2)  # Output: False
print(obj1 < obj2)   # Output: True
print(obj1 > obj2)   # Output: False

# __add__, __sub__, __mul__
result = obj1 + obj2
print(result)  # Output: SampleClass with value: [1, 3, 4, 5, 6]

result = obj1 - obj2
print(result)  # Output: SampleClass with value: [-3]

result = obj1 * obj2
print(result)  # Output: SampleClass with value: [1, 3, 1, 3, 1, 3]
