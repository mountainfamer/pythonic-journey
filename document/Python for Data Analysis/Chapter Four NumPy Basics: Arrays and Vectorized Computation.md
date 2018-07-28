#4.1 The NumPy ndarray: A Multidimensional Array Object#
**Note**: array,NumPy array, ndarray => the ndarray object;

**example**: create ndarray,throuth array();
- data1 = [6,7,8,5.8,0,1]; *Note: include int and float*
- arr1 = np.array(data1)

**example**: create ndarray,throuth nested sequences;
- data1 = [[1,2,3,4],[5,6,7,8]]
- arr2 = np.array(data2)

**Note**: through nested sequences create a multidimensional array;
- arr2.ndim = 2; arr2.shape = (2,4)

**Note**: np.array tries to infer a good data type for the array that is creates;
- arr1.dtype=dtype('float64')
- arr2.dtype=dtype('int64')

**example**: create ndarray use np.zeros() and np.empty();
- np.zeros(10)
- np.zeros((3, 6))
- np.empty((2, 3, 2))

**example**: create ndarry use np.arange()
- np.arange(10)=array([0,1,2,3,4,5,6,7,8,9])

*Table Array creation functions:*

| Function | Desc. |
|----------|-------|
|array||
|asarray||
|arange||
|ones,||
|ones_like,||
|zeros,||
|zeros_like||
|empty,||
|empty_like,||
|full,||
|full_like,||
|eye,identify||

**Data Types for ndarrays**
**example**: create nparray and pass data type(dtype);
- np.array([1,2,3], dtype=np.float64)
- np.array([1,2,3], dtype=np.int32)

*Table NumPy data types*

| Type|Type Code|desc.
|--------|--------|
|int8,uint8|i1,u1 |..|
|...|...|...|

**example**: convert or cast an array from one dtype to another.

     arr = np.array([1,2,3,4,5])
     arr.dtype
     dtype('int64')
     float_arr = arr.astype(np.float64)
     arr.dtype
     dtype('int64')
     float_arr.dtype
     dtype('float64')

**example**: converst str array to numeric form:
- mumeric_strings = np.array(['1.25','-9.6','42'], dtype=np.string_)
- int_array = numeric_strigs.astype(float)
- int.array.astype(arr.dtype) #use another array's dtype attribute;

**Note**: astype always create a new array;




