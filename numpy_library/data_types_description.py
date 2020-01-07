'''
NumPy supports a much greater variety of numerical types than Python does. 
The following table shows different scalar data types defined in NumPy.
Sr.No.	Data Types & Description
1	
bool_
Boolean (True or False) stored as a byte

2	
int_
Default integer type (same as C long; normally either int64 or int32)

3	
intc
Identical to C int (normally int32 or int64)

4	
intp
Integer used for indexing (same as C ssize_t; normally either int32 or int64)

5	
int8
Byte (-128 to 127)

6	
int16
Integer (-32768 to 32767)

7	
int32
Integer (-2147483648 to 2147483647)

8	
int64
Integer (-9223372036854775808 to 9223372036854775807)

9	
uint8
Unsigned integer (0 to 255)

10	
uint16
Unsigned integer (0 to 65535)

11	
uint32
Unsigned integer (0 to 4294967295)

12	
uint64
Unsigned integer (0 to 18446744073709551615)

13	
float_
Shorthand for float64

14	
float16
Half precision float: sign bit, 5 bits exponent, 10 bits mantissa

15	
float32
Single precision float: sign bit, 8 bits exponent, 23 bits mantissa

16	
float64
Double precision float: sign bit, 11 bits exponent, 52 bits mantissa

17	
complex_
Shorthand for complex128

18	
complex64
Complex number, represented by two 32-bit floats (real and imaginary components)

19	
complex128
Complex number, represented by two 64-bit floats (real and imaginary components
`numpy.dtype(object, align, copy)`
The parameters are −
Object − To be converted to data type object
Align − If true, adds padding to the field to make it similar to C-struct
Copy − Makes a new copy of dtype object. If false, the result is reference to builtin data type object
'''
# using array-scalar type 
import numpy as np  

dt = np.dtype(np.int32)
print(dt)

#int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc.
dt = np.dtype('i4')
print(dt)

'''
The following examples show the use of structured data type. Here, the field name and 
the corresponding scalar data type is to be declared.
'''

# first create structured data type 
dt = np.dtype([('age', np.int8)])
print(dt)
# now apply it to ndarray object 
a = np.array([10,20,30], dtype=dt)
print(a)
# file name can be used to access content of age column 
print(a['age'])
'''
The following examples define a structured data type called student with 
a string field 'name', an integer field 'age' and a float field 'marks'. This dtype is applied to ndarray object.
'''

student = np.dtype([('name','S20'), ('age','i1'), ('marks','f4')])
print(student)