# 1 Python primer(基础) #
##1.1 Python Overview(概述)##
###1.1.1 Python Overview(概述)###
python is an interpreted language(Python就解释语言).

Commands are executed by python sinterpreter(Python命令被解释器执行)

a series of commands and saves  source code or a script(Python源代码或脚本有一系列的命令组成)

Python脚本执行方式：

- python demo.py;
- Python  -i demo.py (执行后停在交付模式)

###1.1.2 Preview of a python program(先看一个Python程序)###

Python语法很大程度依赖于空格

语句由换行符结束，语句也可以占用多行（每行用\结束)，或定界符（{},{}之间可换行）

##1.2 Python的对象(概述)##

Pyhton是面向对象的语言，类是python最基本的数据类型，Python有一些内建的类，比如：int, float, str等； 

###1.2.1 identifiers(标识符), Objects（对象）, and the Assignment statement（赋值语句）###

Asignments statements是python最重要的语句, 如: 
**temperature = 98.6**

在上面的语句中，temperature是identifier(也叫name),98.6是object,=建立这两者的联系; 

identifier reference an instance of float class having value 98.6.

Identifiers in python are case-sensitive(标识符对大小写敏感，即大小写不同的标识符标识不同的name或identifier)；  

identifier不能使用reserved words(保留字)

python的identifier的语义（semantic）类似Java和C++的变量,Each identifier is  implicitly associated with the memory address of the 
object to which it refers(name隐含指向它对应对象的内存地址)

A Python identifier may be assigned to a special object
named None(Python标识符也可以指向一个空对象)

Unlike Java and C++, Python is a dynamically typed language(不像Java与C++，Python是动态语言), there is no
advance declaration associating an identifier with a particular data type(python的identifier使用时不需要提前声明)，An identifier
can be associated with any type of object, and it can later be reassigned to
another object of the same (or different) type(name可以指向任何类型，并可以再指向其他相同或不同的类型)

A programmer can establish an alias by assigning a second identifier to an
existing object（**original = temperature**，//original是temperature的别名，他们都指向相同的对象）

If that object supports behaviors that affect its state, changes enacted
through one alias will be apparent when using the other alias (because they refer to
the same object)(如果对象支持改变，对象改变后，两个name都会改变). However, if one of the names is reassigned to a new value using
a subsequent assignment statement, that does not affect the aliased object, rather it
breaks the alias.（如果其中一个指向了另外一个对象，则不会影响另外一个identifier）
(记住：标识符与对象之间是一一对应的关系，与其他的标识符与对象没关系，除非这个对应关系被明确的改变)

**temperature = temperature + 5.0**  //temperature指向新的对象，而original还是指向原来的对象； 

###Creating and Using Objects###

**Instantiation**: 对象实例化	，实例化的方法:

- 如果Widget是一个对象, **w = Widget()**,Widget对象无参实例化后分配给w identifier；
- python的内建对象实例化方法，将字面量分配给identifier，如：temperature = 98.6； 
- 调用内建方法或函数，其返回值为一个对象，并赋给name； 

**Calling Methods**: 方法调用:

Some methods return information about the state of an object, but do not change
that state(有些方法获取对象的状态，有些可以改变对象的状态)

获取对象状态的方法，称为accessor, 改变对象的方法叫mutator/update method.

###1.2.3 Python's Build-in Class(Python的内建类)### 

python的内建类分为可变类与不可变类；

**The bool Class**:  逻辑类

逻辑类只有两个实例：True，False, 逻辑类的构造器**bool()**，返回False； 另外，构造器中可以跟一个对象，如：**bool(foo)**, 如果foo非空，则构造器返回True，反之返回False； 

**The int Class**

Python的int类不像Java那样分int, short, long那么多级别，Python automatically chooses the internal representation for an integer
based upon the magnitude of its value（python根据value的大小，自动选择表达方式(分配内存)） 

**int()**, int类的构造器，无参是返回0，其参数可以是其他类型(‘其他类型必须可以转换成int’)，如float类型，'224'(数字字符串); int(1.2) = 1 , int('224') = 224; Int的构造器中还可以加‘进制’参数，如：int('7f', 16 = 127);

**The float Class**

**Sequence Types: The list, tuple, and str Classes**

list, tuple, str是Python的sequence type(序列类型)

The list class is the most general,representing a sequence of arbitrary objects(list表示**任意类型**对象的序列)

The tuple class is an immutable version of the list class, benefiting from a streamlined internal representation(tuple元组是list的不可变版本)

str类是一组不可变的字符的序列，注意**python没有单字符类型**

**The list class**

A list instance stores a sequence of objects(list实例存储一系列的对象). A list is a referential structure(引用结构), as it technically stores a sequence of references to its elements(它**存储的元素的引用**)

Elements of a list may be arbitrary objects (including the None object: 元素可以是任意类型，包括None). Lists are array-based sequences and are zero-indexed, thus a list of length n has elements indexed from 0 to n−1 inclusive

Lists are perhaps themost used container type(list是容器类型)

**Python的定义**:

- []
- ['red','green','blue'];
- [a,b]      //a,b 是变量;
- list()     //通过构造器定义，默认返回一个空表；构造器接受任何iterable type(**可迭代**类型) 参数,如：string, list,tuple,set,dict等; list('hello') = ['h','e','l','l','o']；
- list(data) //data是一个list，list(data)返回一个新list，和data指向相同的内容；

list的内部表现形式：
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

			    2   3   5   7   11  13  17  19  23  29  31     //对象实例
     prime:   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |   //引用

**The tuple Class**

与list相对应，tuple的定义方式为：(), (17,) //注意后面的逗号，(17)是一个表达式，而非一个元祖定义; 
如：(17,) = (17,), (17) = 17;

**The str Class**

represent an immutable sequence of characters: 表示一个不可变的字符序列； 

String literals can be enclosed in single quotes(str的字面量可以用单引号包围), as in hello , or double quotes, as in "hello"，如果str需要包含单引号，可以用转义字符\'表示；其他一些转义字符的表示：\\, \n \t等，还可以表示 Unicode； 

string的其他定界符(delimiter): ''' """ "，其中'''与"""可以接受多行字符；

**The set and frozenset Classes**

Python’s set class represents the mathematical notion of a set(数学概念中的集合 ), namely a collection of elements（顾名思义,一组元素）, without duplicates(没有重复), and without an inherent order（没有顺序） to those elements

The major advantage of set: 检查set中是否包含某个元素，为什么set可以高效的完成，是因为set的包含操作基于hash table的data structure;

set的两个restrictions(限制: 由于其算法基于hash table，因此其中的对象必须可hash，可变对象不可hash):

- 无序；
- 只有不可变对象实例可以加入set；

注意：set使用{和}包围它的元素，但{}确不表示一个空set，而是表示dict；要表示空set，使用set()表示；

**set的constructor**:set()，其参数可以是一个**可迭代**对象，如：set('hello')={'h','e','l','l','o'}

forzenset: 不可变类型的set(因为不可变，所以存在hash值)； 

备注：set是可变对象，虽然其元素是不可变对象，frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。

**The dict Class**

dict表示一个dictionary，或mapping，from a set of distinct(有区别的) keys(set,没有重复) to associated values(每个key对应一个value)；

**dict的表示**：

- {}
- {'ga' : 'Irish' , 'de' : 'German' }
- dict(a)   //a为dict
- dict(a)   //a为键值对的序列，如a=[('ga', 'Irish'),('de','German')]

**Expressions, Operations, and Precedence**(表达式，运算符及其优先级)

**Sequence Operators**(内建序列类型: str,tuple,list支持)	

序列操作格式：  s[start:stop:step], in, not in, *, +;
index -1 ： 表示last one element;
index -2 :  表示second to last

**Operators for Set and Dictionaries**
	
in, not in, ==, !=, <=, >=, |, &, -,  ^(集合操作符)；

**Extended Assignment Operators**(追加操作)

+=, 注意对可变与不可变对象操作时的变化；

##1.4 Control Flow##
 
###1.4.1 Conditionals###

if response   =>    if response != ''

###1.4.2 Loops###

**while loops**: 基于逻辑条件测试的反复处理；

while condition:

   body

**for loops**: 遍历可迭代对象时使用起来很方便； 

##1.5 Functions##

###1.5.1 Information Passing信息传递###

函数定义是使用的是formal parameters, 函数调用时用的是actual parameters，实参到形参之间相当于是assigenmet statement(赋值语句);

如：

	`def count(data, target):  
    	n = 0  
    	for item in data:  
    	    if item == target: # found a match  
    	    n += 1  
    	return n`

prizes = count(grades, 'A'), as follows:

data = grades

target = 'A'

These assignment statements(赋值语句) establish identifier data as an alias for grades and target as a name for the string literal A

grades --> |list| <-- data      target --> str

The communication of a return value from the function back to the caller(调用者与函数之间通过返回语句通信) is similarly implemented as an assignment(像赋值语句一样).

An advantage to Python’s mechanism for passing information to and from a function(函数传递参数这种机制的好处) is that objects are not copied（参数不是拷贝的）. This ensures that the invocation of a function is efficient, even in a case where a parameter or return value is a complex object.

**Mutable Parameters**: 可变参数

Because the formal parameter is an alias for the actual parameter（因为形参是实参的别名）, the body of the function may interact with the object(函数体可以和对象之间相互影响) in ways that change its state.

以count函数为例，count(data, target), 如果函数体中有这样的语句：**data.append('F')**，函数体中的语句影响到调用上下文中的data对象**（改变了实参）**; 另外，如果函数体中有这样的语句：data = []，这个赋值语句不会影响到实参，因为[]定义了一个新的对象，改变了data实参和data形参之间的关系，形参data再也不是实参data的别名了，他们分别指向不同的对象。

**Default Parameter Values**

Python provides means for functions to support more than one possible calling signature(多种调用签名). Such a function is said to be polymorphic（多态）(which is Greek for “many forms”).(由于函数可以定义默认参数，这位函数调用提供了多种的形式【**可变数量的实参**】), 如：

def foo(a, b=15, c=27)

foo(4, 12, 8): 		=> a=4, b=12, c=8
	
foo(4):				=> a=4, b=15, c=27

foo(8, 20):			=> a=8, b=20, c=27 

仔细体会下面的例子：

	`def range(start, stop=None, step=1):  
		if stop is None:  
		stop = start  
		start = 0`
当调用range(n)时，n并没赋值给start，而是传给了stop参数；

**Keyword Parameters**

传统的实参到形参定义，基与positional arguments（位置参数）的概念; 如对于: foo(a=10, b=20, c=30), foo(5)表示a=5, 其他参数取默认值；

同时，Python也支持所谓的关键字参数, 如：f(c=5), 表示c=5, 而其他参数取默认值； 

###1.5.2 Python's Built-In Functions###

内建函数可以分成下面这些类：

- 输入/输出；
- 字符编码；
- 书写函数；
- 顺序类函数； 
- 集合/迭代类函数； 

|调用语法|描述                             |      
|-------|---------------------------------|   
|abs(x) |绝对值|
|all(iterable) |return True if bool(e) for e in iterable|
|any(iterable) |return True if any bool(e) is True for e in iterable|
|char(integer) |int=> char|
|divmod(x,y)   |return (x//y, x%y) as tuple, if x and y are integers|
|hash(obj)     |...|
|id(obj)|unique integer...|
|input(prompt)|return a string from standard input; |
|isinstance(obj, cls)|...|
|iter(iterable)|return a new iterator object for the parameter|
|len(iterable)| the number of elements in iterable obj|
|map(f, iter1, iter2)|return an iterator yielding the result of function calls f(e1,e2)e1属于iter1,e2属于iter2|
|max(iterable)|return the largest element|
|max(a,b,c)|...|
|min(iterable)|...|
|min(a,b,c)|...|
|next(iterator)|next element|
|open(filename, mode)|...|
|ord(char)|unicode code|
|pow(x,y)|x**y|
|print(obj1,obj2)|...|
|range(stop)|...|
|range(start,stop)|...|
|range(start,stop,step)|...|
|reversed(sequence)|倒序|
|round(x)|取整|
|sorted(iterable)|排序|
|sum(iterable)|求和|
|type(obj)|类型|

##1.6 简单输入输出##

###1.6.1 console input and output###

**The print Function**

print can output string or no string instance, print () outputs a single newline character. print has follow keyword parameters:

- The default separate character is space, The separator can be customized by 'sep=', the separator string can be a single character, or empty string, or a longer string.
- you can customize the end use 'end=' parameters.
- print can output to standard console, yet output to file.

**The input Function**

**A sample Program**

###1.6.2 Files###

|调用语法|描述                                   |      
|------------|---------------------------------|   
|fp.read()   |读取文件剩余的所有内容|
|fp.read(k)  |读取k bytes|
|fp.readline(k)|读取一行|
|fp.readlines(k)|读取剩余所有行|
|for line in fp:|Iterate all lines|
|fp.seek(k)|移动当前位置像后k byte|
|fp.tell()|返回当前位置|
|fp.write(string)|写文件|
|fp.writelines(seq)|写文件|
|print(..., file=fp)|重定向打印到文件|

##1.7 Exception Handling##

**common Exception Types**

###1.7.1 Raising an Exception###

raise statement:  raise Exception instance

###1.7.2 Cathing an Exception###

##1.8 Iterators and Generators##

container types (容器类型): list, tuple, set, string, dict, customize class. 

iteration has follow conventions(约定):

- next(i): produces a subsequent element; 
- iter(obj): produces an iterator; 

**iterable and iterator**: iterable obj support 'for i in seq', but not support next(), iterator support next(); iterable 转换成 iterator, iter(obj) //obj is iterable.

**generators**: A generator is implemented with a syntax that is very similar to a function, but instead of returning values, a yield statement is executed to indicate each element of the series.

traditional function:

    `def factors(n):              # traditional function that computes factors
        results = [ ]             # store factors in a new list
        for k in range(1,n+1):
            if n % k == 0:        # divides evenly, thus k is a factor
                results.append(k) # add k to the list of factors
        return results            # return the entire list`

generator:

    `def factors(n): # generator that computes factors
        for k in range(1,n+1):
            if n % k == 0: # divides evenly, thus k is a factor
                yield k # yield this factor as next result`

//生成器：lazy evaluation(懒惰), 当需要的时候才产生；

##1.9 Additional Python Conveniences(方便)##
###1.9.1 条件表达式###
expr1 if condition else expr2
###1.9.2 Comprehension Syntax 列表推导式###
[ expression for value in iterable if condition ]

###1.9.3 Packing and Uppacking of Sequence(压包与解包)###

**Simultaneous Assignments**

##1.10 Scopes and Namespaces##

##1.11 模块和import语句##

**Create a New Module**

###1.11.1 系统自带Module###

|模块名称|描述                                   |      
|------------|---------------------------------|   
|array  |数组，存放原始类型|
|collections||
|copy|copy objects|
|heapq|堆队列|
|math|数学常量和函数|
|os|操作系统模块|
|random|生成随机数的模块|
|re|正则表达式模块|
|sys|sys模块|
|time|时间模块|

**Pseudo-Random Number Generation**

|语法|描述                                   |      
|------------|---------------------------------|   
|seed(hashable)|初始化随机数生成器|
|random()|0-1之间的随机数|
|randint(a,b)|产生a到b之间的整形随机数|
|randrange(start,stop,step)|产生指定递增基数集合中的一个随机数|
|choice(seq)|产生seq中随机一个元素|
|shuffle(seq)|将排序随机排列|

##1.12 练习##



