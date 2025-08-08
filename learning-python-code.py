# This is learning of print
print("This is learning of print")
a1,a2,a3 = 1,2,3
print('s1 is %#10x,s2 is %+d,s3 is %10d'% (a1, a2, a3))
print('s1 is {0:^10d},s3 is {2:2=10d},s2 is {1:5<+#10o}'.format(a1, a2, a3))
print(f'this is f\'\' {id(a:=10)= :#x}')

# id is the memory address of the variable
print("id is the memory address of the variable")
print('%#20x' % (id(b:=20)))

# This is bin oct hex
print("This is bin oct hex")
print(bin(15),oct(15),hex(15),sep='\t'*3)

# This is bit manipulation
print("This is bit manipulation")
print(~b, b<<2, b>>2, b&3, b|3, b^3, sep='\t')

# This is boolean operations
print("This is boolean operations")
c1,c2=1,2
print(c1 and c2, c1 or c2, not c1, sep='\t'*3)

# This is identity and equality ;use id() compare memory address
print("This is identity and equality")
print(c1 is c2, c1 is not c2, c1 is not None, sep='\t'*3)

# This is membership test
print("This is membership test")
print(c1 in [1, 2, 3], c1 not in [1, 2, 3], sep='\t'*3)

# This is exception handling
# try except else finally
print("This is exception handling")
try:
    print('this is test')
    x = 1 / 0
except:
    print('error')
    # this will raise the exception again
    # raise  # except ZeroDivisionError as e:
                 # print(f'ZeroDivisionError: {e}')
else:
    print('no error')
finally:
    print('this is finally block')
    
# This is assert statement
# assert condition, message
# assert x != 0, 'x should not be zero'  # this can run

#This is list comprehension
print("This is list comprehension"+'*'*50)
squares = [x * x for x in range(10)]
print(f'squares: {squares}')
squares.append(100)
print(f'squares after append: {squares}')
squares.extend([121, 144])
print(f'squares after extend: {squares}')
squares.insert(0, 0)
print(f'squares after insert: {squares}')
squares.remove(100)
print(f'squares after remove: {squares}')
squares.pop()
print(f'squares after pop: {squares}')
squares2=squares.copy()
print(f'squares2 is a copy of squares: {squares2}')
squares.clear()
print(f'squares after clear: {squares}')
del squares
print('squares is deleted \'del squares\'')
del squares2
print('squares2 is deleted \'del squares2\'')
squares = [x * x for x in range(10)]
print(f'squares: {squares}')
print(f'length of squares: {len(squares)}')
print(f'min of squares: {min(squares)}')
print(f'max of squares: {max(squares)}')
print(f'sum of squares: {sum(squares)}')
print(f'squares count of 25: {squares.count(25)}')
print(f'squares\' search index of 25: {squares.index(25)}')
print(f'{squares.reverse()}\rreverse function reversing') # Return None
print(f'squares after reverse: {squares}')
print(f'{squares.sort()}\rsort function sorting') # Return None
print(f'squares after sort: {squares}')  
print(f'squares sorted: {sorted(squares)}')
print(f'squares reversed: {list(reversed(squares))}')
del squares  # delete squares again to avoid confusion

# This is tuple comprehension
print("This is tuple comprehension"+'*'*50)
squares_tuple = tuple(x * x for x in range(10)) # squares_tuple = tuple([x * x for x in range(10)])  # this can create tuple
print(f'squares_tuple: {squares_tuple}')
print(f'length of squares_tuple: {len(squares_tuple)}')
print(f'min of squares_tuple: {min(squares_tuple)}')
print(f'max of squares_tuple: {max(squares_tuple)}')
print(f'sum of squares_tuple: {sum(squares_tuple)}')
print(f'squares_tuple count of 25: {squares_tuple.count(25)}')
print(f'squares_tuple\' search index of 25: {squares_tuple.index(25)}')
print(f'25 in squares_tuple: {25 in squares_tuple}')
print(f'25 not in squares_tuple: {25 not in squares_tuple}')
print(f'100 in squares_tuple: {100 in squares_tuple}')
print(f'100 not in squares_tuple: {100 not in squares_tuple}')
print(f'squares_tuple sorted: {tuple(sorted(squares_tuple))}')
print(f'squares_tuple reversed: {tuple(reversed(squares_tuple))}')
squares_tuple2 = list(squares_tuple)
print(f'{squares_tuple2.sort()}\rsquares_tuple2 sort function sorting') # Return None
print(f'squares_tuple after sort: {tuple(squares_tuple2)}')
del squares_tuple2  # delete squares_tuple2 to avoid confusion
print("delete squares_tuple2 to avoid confusion")
squares_tuple2 = list(squares_tuple)
print(f'{squares_tuple2.reverse()}\rsquares_tuple2 reverse function reversing') # Return None
print(f'squares_tuple after reverse: {tuple(squares_tuple2)}')
del squares_tuple2  # delete squares_tuple2 to avoid confusion
print("delete squares_tuple2 to avoid confusion")
print(f'squares_tuple is {squares_tuple=}')
del squares_tuple  # delete squares_tuple to avoid confusion
print('squares_tuple is deleted \'del squares_tuple\'')

# This is set comprehension
print("This is set comprehension"+'*'*50)
set1 = {x * x for x in range(10)}
print(f'set1: {set1}')
print(f'length of set1: {len(set1)}')
print(f'min of set1: {min(set1)}')
print(f'max of set1: {max(set1)}')
print(f'sum of set1: {sum(set1)}')
print(f'25 in set1: {25 in set1}')
print(f'100 in set1: {100 in set1}')
print(f'25 not in set1: {25 not in set1}')
print(f'100 not in set1: {100 not in set1}')
set1.add(100)
print(f'set1 after add 100: {set1}')
set1.update([121, 144]) # [121, 144] or (121, 144) or {121, 144}
print(f'set1 after update [121, 144]: {set1}') 
set1.remove(100)
print(f'set1 after remove 100: {set1}')
set1.discard(200)  # this will not raise error if the element is not found
print(f'set1 after discard 200: {set1}')
popped_element = set1.pop()  # remove and return an arbitrary element
print(f'set1 after pop {popped_element}: {set1}')
set2 = set1.copy()
print(f'set2 is a copy of set1: {set2}')
set1.clear()
print(f'set1 after clear: {set1}')
del set1
print('set1 is deleted \'del set1\'')
del set2
print('set2 is deleted \'del set2\'')
set1 = {x * x for x in range(10)}
print(f'set1: {set1}')
set1.intersection_update({1, 4, 9, 16, 25})
print(f'set1 after intersection_update with {{1, 4, 9, 16, 25}}: {set1}')
set1.difference_update({1, 4})
print(f'set1 after difference_update with {{1, 4}}: {set1}')
set1.symmetric_difference_update({9, 16, 25, 36})
print(f'set1 after symmetric_difference_update with {{9, 16, 25, 36}}: {set1}')
del set1  # delete set1 again to avoid confusion
print("delete set1 to avoid confusion")
set1 = {x * x for x in range(10)}
set2 = {x + 1 for x in range(5)}
print(f'set1: {set1}')
print(f'set2: {set2}')
print(f'set1 union set2: {set1 | set2}')
print(f'set1 update set2: {set1.union(set2)}')
print(f'set1 intersection set2: {set1 & set2}')
print(f'set1 intersection set2: {set1.intersection(set2)}')
print(f'set1 difference set2: {set1 - set2}')
print(f'set1 difference set2: {set1.difference(set2)}')
print(f'set1 symmetric_difference set2: {set1 ^ set2}')
print(f'set1 symmetric_difference set2: {set1.symmetric_difference(set2)}')
del set1  # delete set1 again to avoid confusion   
del set2  # delete set2 again to avoid confusion
print('set1 is deleted \'del set1\'')
print('set2 is deleted \'del set2\'')
frozenset1 = frozenset(x * x for x in range(10))
print(f'created frozenset1: {frozenset1}')
del frozenset1
print('frozenset1 is deleted \'del frozenset1\'')

# This is dictionary comprehension
print("This is dictionary comprehension"+'*'*50)
dict1 = {i : x * x for x in range(10) for i in range(10)}
print(f'dict1: {dict1}')
print(f'length of dict1: {len(dict1)}')
print(f'min of dict1: {min(dict1)}')
print(f'max of dict1: {max(dict1)}')
print(f'sum of dict1: {sum(dict1.keys()), sum(dict1.values())}')
print(f'keys of dict1: {dict1.keys()}')
print(f'values of dict1: {dict1.values()}')
print(f'items of dict1: {dict1.items()}')
print(f'1 in dict1: {1 in dict1}')
print(f'100 in dict1: {100 in dict1}')
print(f'1 not in dict1: {1 not in dict1}')
print(f'100 not in dict1: {100 not in dict1}')
dict1[100] = 10000
print(f'dict1 after adding key 100 with value 10000: {dict1}')
dict1.update({200: 20000, 300: 30000})
print(f'dict1 after update with {{200: 20000, 300: 30000}}: {dict1}')
dict1.pop(100) # remove key 100 and return its value
print(f'dict1 after pop key 100: {dict1}')
dict1.popitem()  # remove and return an arbitrary key-value pair
print(f'dict1 after popitem: {dict1}')
dict2 = dict1.copy()
print(f'dict2 is a copy of dict1: {dict2}')
dict1.clear()
print(f'dict1 after clear: {dict1}')
del dict1
print('dict1 is deleted \'del dict1\'')
del dict2
print('dict2 is deleted \'del dict2\'')
dict1 = dict.fromkeys([1, 2, 3], 'default_value')  # create a new dictionary with keys from the iterable and all values set to 'default_value'
print(f'dict1 created dict.fromkeys from keys [1, 2, 3] with default value: {dict1}')
del dict1  # delete dict1 to avoid confusion
print('dict1 is deleted \'del dict1\'')

# This is string manipulation
print("This is string manipulation"+'*'*50)
s1='abcdefghijklmnopqrstuvwxyz'
print(''.join(str(ord(i)) for i in s1))
a,b,c=2,0,0
print(f'{a=}, {b=}, {c=}')
a='%c' % 97
print(a)
print(chr(97), ord('a'), sep='\t')  # chr() converts an integer to a character, ord() converts a character to an integer
print(bytes.fromhex('68 65 6c6c6f20776f726c64').decode('utf-8')) # 'hello world'
print('啊'.encode(),'a'.encode(),sep='\t')
print(bin(11), oct(11), hex(11),int('11',base=8), sep='\t')
print(f'Testing BOM {''.encode('utf-16')}')
s2='数字是: {:o}'
print(s2.zfill(5))
print(s2.format(12))
s1=b'ab'
print(f'this is bytes_obj.hex function {s1.hex()}')
print(f'notice !!! this is not bytes.fromhex but s1.fromhex {s1.fromhex("616263")=}') # s1 should be bytes
del s1  # delete s1 to avoid confusion
# This is string methods
print("This is string methods"+'*'*50)
s1 = 'hello world'
print(f's1: {s1}')
print(f'reverse s1: {s1[::-1]}')
print(f'length of s1: {len(s1)}')
print(f'min of s1: {min(s1)}') 
print(f'max of s1: {max(s1)}')
print(f'super s1: {s1.upper()}')
print(f'sub s1: {s1.lower()}')
print(f's1 capitalize: {s1.capitalize()}')
print(f's1 title: {s1.title()}')
print(f's1 swapcase: {s1.swapcase()}')
print(f's1 count of "l": {s1.count("l")}')
print(f's1 index of "l": {s1.index("l")}')
print(f'rindex s1: {s1.rindex("l")}')
print(f's1 find "l": {s1.find("l")}')
print(f's1 rfind "l": {s1.rfind("l")}')
print(f's1 replace "l" with "L": {s1.replace("l", "L")}')
print(f's1 strip: {s1.strip()}')
print(f's1 lstrip: {s1.lstrip()}')
print(f's1 rstrip: {s1.rstrip()}')
print(f'expandtabs s1: {s1.expandtabs(4)}')
print(f'translate s1: {s1.translate(str.maketrans("h", "H"))}')
print(f'market s1: {s1.maketrans("h", "H")}')
print(f's1 split: {s1.split()}')
print(f's1 rsplit: {s1.rsplit()}')
print(f's1 splitlines: {s1.splitlines()}')
print(f's1 partition " ": {s1.partition(" ")}')
print(f's1 rpartition " ": {s1.rpartition(" ")}')
print(f's1 join: {"-".join(s1)}')
#testing string
print(f'isalnum s1: {s1.isalnum()}')
print(f'isalpha s1: {s1.isalpha()}')
print(f'isascii s1: {s1.isascii()}')
print(f'isdigit s1: {s1.isdigit()}')
print(f'isdecimal s1: {s1.isdecimal()}')
print(f'isnumeric s1: {s1.isnumeric()}')
print(f'isidentifier s1: {s1.isidentifier()}')
print(f'isprintable s1: {s1.isprintable()}')
print(f'islower s1: {s1.islower()}')
print(f'isupper s1: {s1.isupper()}')
print(f'istitle s1: {s1.istitle()}')
print(f'isspace s1: {s1.isspace()}')
print(f's1 starts with "he": {s1.startswith("he")}')
print(f's1 ends with "ld": {s1.endswith("ld")}')
del s1  # delete s1 to avoid confusion

# This is bytes manipulation
print("This is bytes manipulation"+'*'*50)
s1 = b'hello world'
print(f'bytes s1: {s1=} {bytes(10)=}')
print(f'bytes length of s1: {len(s1)}')
print(f'bytes min of s1: {min(s1)}')
print(f'bytes max of s1: {max(s1)}')
print(f'bytes sum of s1: {sum(s1)}')
print(f's1 count of "l": {s1.count(b"l")}')
print(f's1 index of "l": {s1.index(b"l")}')
print(f's1 rindex of "l": {s1.rindex(b"l")}')
print(f's1 find "l": {s1.find(b"l")}')
print(f's1 rfind "l": {s1.rfind(b"l")}')
print(f's1 replace "l" with "L": {s1.replace(b"l", b"L")}')
print(f's1 split: {s1.split()}')

# This is function annotation
print("This is function annotation"+'*'*50)
def add_annotation(x:int =10, y:int =20) -> int:
    return x + y
add=add_annotation(1,2)
print(f'function add_annotation with annotation: {add=}, {add_annotation.__annotations__=}')
# This is ord and chr
s1='abcdefghijklmnopqrstuvwxyz'
print(''.join(str(ord(_)) for _ in s1))

# This is map function with function annotation
print("This is map function with function annotation"+'*'*50)
def square(x: int) -> int:
    """Returns the square of a number."""
    return x * x
x=list(map(square, range(10)))
print(f'square function with annotation: {x=}, {square.__annotations__=}')

# This is filter function with function annotation
print("This is filter function with function annotation")
def is_even(x: int) -> bool:
    """Returns True if the number is even, False otherwise."""
    return x % 2 == 0
x=list(filter(is_even, range(10)))
print(f'is_even function with annotation: {x=}, {is_even.__annotations__=}')

# This is lambda function
print("This is lambda function"+'*'*50)
lambda_square = lambda x: x * x
print(""f'lambda_square function: {lambda_square(5)=}, {lambda_square.__annotations__=}')

# This is embedded function
print("This is embedded function"+'*'*50)
def outer_function(x: int) -> int:
    """Outer function that takes an integer and returns a function."""
    def inner_function(y: int) -> int:
        """Inner function that takes an integer and returns the sum of x and y."""
        return x + y
    return inner_function
inner = outer_function(10)
print(f'outer_function with annotation: {inner(5)=}, {outer_function.__annotations__=}, {inner.__annotations__=}')

# This is generator function
print("This is generator function"+'*'*50)
def generator_function(n: any) -> any:
    """Generator function that yields squares of numbers from 0 to n."""
    for i in range(n):
        yield i * i
gen = generator_function(5)
print(f'generator_function with annotation: {list(gen)=}, {generator_function.__annotations__=}')

# This is decorator function
print("This is decorator function"+'*'*50)
def decorator_function(func: callable) -> callable:
    """Decorator function that modifies the behavior of the input function."""
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper
@decorator_function
def decorated_function(x: int, y: int) -> int:
    """Function that adds two numbers."""
    return x + y
print(f'decorated_function with annotation: {decorated_function(5, 10)=}, {decorated_function.__annotations__=}')

# This is decorator with arguments
print("This is decorator with arguments"+'*'*50)
def decorator_with_args(arg1: str, arg2: str) -> callable:
    """Decorator that takes arguments."""
    def decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {arg1}, {arg2}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@decorator_with_args("Hello", "World")
def decorated_function_with_args(x: int, y: int) -> int:
    """Function that adds two numbers."""
    return x + y
print(f'decorated_function_with_args with annotation: {decorated_function_with_args(5, 10)=}, {decorated_function_with_args.__annotations__=}')
