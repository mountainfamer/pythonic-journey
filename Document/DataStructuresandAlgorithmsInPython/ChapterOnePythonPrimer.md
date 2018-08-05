#Chapter 1#
##1.1 Python Overview(概述)##
###1.1.1 Python Overview(概述)###
- python is an interpreted language(Python就解释语言).
- Commands are executed by python sinterpreter(Python命令被解释器执行)
- a series of commands and saves  source code or a script(Python源代码或脚本有一系列的命令组成)
- Python脚本执行方式：
  python demo.py;
  Python  -i demo.py (执行后停在交付模式)

###1.1.2 Preview of a python program(先看一个Python程序)###
- Python语法很大程度依赖于空格
- 语句由换行符结束，语句也可以占用多行（每行用\结束)，或定界符（{},{}之间可换行）

##1.2 Object in python##
Pyhton是面向对象的语言，类是python最基本的数据类型，Python有一些内建的类，比如：int, float, str等；

###1.2.1 Identifiers, Objects, and the Assignment Statement
**example**: temperature = 98.6

**Note**: 在上面的语句中，temperature是identifier(也叫name),98.6是object,=建立这两者的联系;temperature指向浮点对象(类)的实例98.6, python中一切皆对象，数值型也是对象；对象存放在内存中，标识符（变量\引用）指向这个地址；

- Identifier reference an instance of float class having value 98.6.
- Identifiers in python are case-sensitive(标识符对大小写敏感，即大小写不同的标识符标识不同的name或identifier)；
- identifier不能使用reserved words(保留字);
- Each identifier is  implicitly associated with the memory address of the object to which it refers(name隐含指向它对应对象的内存地址);
- A Python identifier may be assigned to a special object named None(Python标识符也可以指向一个空对象);
- Unlike Java, Python is a dynamically typed language(不像Java与，Python是动态语言), there is no advance declaration associating an identifier with a particular data type(python的identifier使用时不需要提前声明)，An identifier can be associated with any type of object, and it can later be reassigned to another object of the same (or different) type(name可以指向任何类型，并可以再指向其他相同或不同的类型);
- A programmer can establish an alias by assigning a second identifier to an existing object（**original = temperature**，//original是temperature的别名，他们都指向相同的对象）;If that object supports behaviors that affect its state, changes enacted through one alias will be apparent when using the other alias (because they refer to the same object)(如果对象支持改变，对象改变后，两个name都会改变).
- However, if one of the names is reassigned to a new value using a subsequent assignment statement, that does not affect the aliased object, rather it breaks the alias.（如果其中一个指向了另外一个对象，则不会影响另外一个identifier） (记住：标识符与对象之间是一一对应的关系，与其他的标识符与对象没关系，除非这个对应关系被明确的改变)
**example**: original = temperature
**Note**: original和temperature一样，指向同一个对象;

**example**: temperature = temperature + 5.0
**Note**:  先执行右边的表达式，结果为103.6,是另外一个浮点对象的实例；然后，temperature重新指向这个浮点对象的地址；而original没有变化，仍然指向原来的地址;
###1.2.2 Create and Using Objects###
**example**: w=Widget()
**Note**: 这是实例化一个无参的类,乍一看和函数有点相似,但注意,类名一般以大写开头;

**example**: temperature = 98.6
**Note**: 像前面的i例子,这也是实例化一个对象,实例化的是一个浮点数,像浮点数这种类在python中,称为literal form(字面量形式);

**example**: w=sorted(range(5))
**Note**: 通过一个函数创建了一个对象,对象类型为list;
Some methods return information about the state of an object, but do not change
that state(有些方法获取对象的状态，有些可以改变对象的状态)
获取对象状态的方法，称为accessor, 改变对象的方法叫mutator/update method.

###1.2.3 Python's Bulid-in Classes###
- python内置的可变类：list, set, dict;
- python内置的不可变类：int,bool,float,tuple,str,frozenset;

**Note**: 不可变对象实例不能修改，但是同一标识符可以指向另外的实例;

**The bool Class**:
- the only two instance,as the literals True and False,即:逻辑类的实例只有两个(字面量),True和False;
- default constructor: bool(), and return False;
- create of a Boolean value from a nonboolean type using the syntax bool(foo) for value foo,即:可以将一个变量传递给构造器,产生一个逻辑类实例, 非0非空的参数产生True;

**The int Class**:
- python 的int类支持任意大小的数值,并会依照其大小分配地址空间,不想java和c++分不同的整形类型;
- python 的int类支持不同的进制表示,如0B1011,0O52,0X7f;
- int的构造器:int(),返回0;
- int的构造器带数值型的参数,返回数值整数部分的int,如int(3.14)=3, int(-3.9)=3;
- int的构造器中可以带数值表示的字符串,返回对应的int型,如:int('137')=137; 带非数值表示的字符串,返回ValueError异常;
- 当参数为字符串时,可以用一个参数表示进制,如果不带此参数,默认为10i进制,如int('77',16)=119, 而int('77',8)=63, int('77')=77

**The float Class**:
- 简单的说明,浮点数带小数位;
- float()=0.0
- float(2)=2.0
- float('3.14')=3.14

**Sequence Types: The list, tuple, and str Classes**
- list,tuple,str都是集合类,都有顺序的性质;
- list和tuple可存放不同类型的类的实例;
- tuple是list的不可变版本;

**The list Class**
- list类实例可以存放一系列的对象实例;
- a list is a referential structure,as it technically store a sequence of references to its elements.即，list
中存放的是指向一系列元素的地址(**引用**);
- list的创建，使用［］定界符，其中没有元素;
- list的创建 ,定界符中放字面量［１，２，３］；
- list的创建，定界符符放变量, 如:a=1,b=2,[a,b]相当于[1,2];
- 使用构造器创建: list(),其中不加参数返回空列表;
- 使用构造器创建: 加参数时，接受可迭代对象；可迭代对象有：strings,list,tuples,set ,dict;

list的内部表现形式：
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

			    2   3   5   7   11  13  17  19  23  29  31     //对象实例
     prime:   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |   //引用

**example**:list('hello')=['h','e','l','l','o']
**example**:通过构造器复制list:
a=[1, 2, 3, 4]; b = a #指向同一个列表；c = list(a) #复制一个列表；
则： a与b指向同一个list，而c指向内容与a/b相同的另外一个list；
所以： id(a) == id(b) , id(c) != id(a) ; a is b , 而 a is not c;
**example**:list的有些方法直接影响源list，而不会可打印返回结果，如：insert, remove, sort， 这些方法可以允许级联使用，如listA.insert().remove().sort()

**The tuple Class**
- list的定界符为[],而tuple的定界符为();
- 当用定界符i表示tuple,而且元素只有一个时,元素后面一定要跟一个',',而有多个元素是,可跟可不跟;因为(17)是一个表达式;

**The str Class**
- 表示字符的序列;
- 支持转义字符;

**The set and frozenset Classes**
- 无重复的对象序列;
- set不维护对象的顺序;
- 不可变对象才能加入set;
- list,set,disk由于是可变对象不能加入set,如果要把set加入set,可以用frozensetg将set转换成不可变对象后加入;
**NOte**: 因为set要使用hash table计算元素的hash值,而只有固定对象才有hash值;
- set的定界符为{};如:{17},{'red','green','blue'}
**NOte**: 由于历史原因,{}并不表示set,而表示的是dict;
- set()是构造器,返回一个空set;
- set()接受可迭代参数,并返回一个set;

**example**: set('hello')={'h','e','l','o'};

**The dict Class**
- dict:dictionary or mapping;
- a set of distinct(不同的) keys to associated(关联的) values;即:key是唯一的,不重复的;key和value是对应关系;
- dict与set的某些特征相同(A. 如无序; B. (key)唯一; C. key必须是不可变对象,即可hash),不同的是还存储了关联的值;
- dict的定界符也是{};
- dict的构造器是dict();
- dict的构造器无参数时,产生一个空的dict;
- dict的构造器接受key-value对作为参数;
**example**: dict([(1,1),(2,2)])={1: 1, 2: 2}

##1.3 表达式,运算符和优先级##
**Equality Operation**: 相等运算,即判断两个对象是否相等;
- is / is not
- == / !=

**Comparison Operation**
- < <= > >=

**Bitwise Operations**
- ~ & | ^ << >>

**Sequence Operation(序列[str,tuple,list]运算)**
- s[j]: element at index j
- s[start:stop:step]:slice(切片)
- s + t: 连接
- k * s: k times
- in / not in

**Set and frozenset supported Operation**:
- Equality Operation: in  not in == !=
- Comparision Operation: > < <= >=
- Bitwise Operation: | & - ^
**Note**:
s1 | s2: the unioin of s1 and s2: s1与s2的全集;
s1 & s2: s1与s2的交集;
s1 - s2: elements in s1 bu not in s2;
s1 ^ s2: ?

**Dict support Operation**
- == !=
- key in d / key not in d
- del d[key]
- d[key] = value

**Extended Assignment Operation(扩展赋值操作)**
- python 支持 binary operation(二元u操作);
- +=在可变与不可变对象上的差异:
  **Note**: 不可变对象经过+=操作后,变量指向新的对象; 而可变对象经过+=操作后,仍指向原来的对象;
	**Note**: 而a=a+b,这样的操作,不管是可变对象还是不可变对象,都指向新的对象;
**example**: 扩展赋值运算符在可变对象和不可变对象上的差别:
a = 1
print id(a)     # 14408840
a += 1
print id(a)     # 14408816
b = 1
print id(b)     # 14408840
b = b+1
print id(b)     # 14408816
如上所示，两种方式对不可变对象的结果相同，都会改变；
L1 = [1,2,3]
print id(L1)    #32964264
L2 = L1
print id(L2)    #32964264
L2 += [4,5]
print L1        #[1, 2, 3, 4, 5]
print L2        #[1, 2, 3, 4, 5]
print id(L1)    #32964264
print id(L2)    #32964264
L3 = [1,2,3]
print id(L3)    #33038920
L4 = L3
print id(L4)    #33038920
L4 =L4 + [4,5]
print L3        #[1, 2, 3]
print L4        #[1, 2, 3, 4, 5]
print id(L3)    #33038920
print id(L4)    #33040216
如上所示，　+= 不会改变原来的对象，而＝会改变；

###1.3.1 混合表达式和优先级###

##1.4 Control Flow##

###1.4.1 Conditionals###

if response   =>    if response != ''

##1.5 Functions##
- function and method的区别:function描述传统的,没有状态(上下文,类,实例)的调用;method是特定的对象的调用,是面向对象的消息传递;

###1.5.1 Information Passing###
- 实参, 形参;
- 变参, 默认参;

函数定义是使用的是formal parameters, 函数调用时用的是actual parameters，实参到形参之间相当于是assigenmet statement(赋值语句);
如：

	`def count(data, target):
    	n = 0
    	for item in data:
    	    if item == target: # found a match
    	    n += 1
    	return n

     prizes = count(grades, 'A'), as follows:
     data = grades
     target = 'A'`

**Note**:These assignment statements(赋值语句) establish identifier data as an alias for grades and target as a name for the string literal A:   grades --> |list| <-- data      target --> 'A'.
The communication of a return value from the function back to the caller(调用者与函数之间通过返回语句通信) is similarly implemented as **an assignment(像赋值语句一样)**.
An advantage to Python’s mechanism for passing information to and from a function(函数传递参数这种机制的好处) is that **objects are not copied（参数不是拷贝的）**. This ensures that the invocation(调用) of a function is efficient, even in a case where a parameter or return value is a complex object(**形参实参指向同以对象的好处是函数调用的效率高**).

**Mutable Parameters**: 可变参数

Because the formal parameter is an alias for the actual parameter（因为形参是实参的别名）, the body of the function may interact with the object(函数体可以和对象之间相互影响) in ways that change its state.

**Note**: 以count函数为例，count(data, target), 如果函数体中有这样的语句：**data.append('F')**，函数体中的语句影响到调用上下文中的data对象**（改变了实参）**; 另外，如果函数体中有这样的语句：data = []，这个赋值语句不会影响到实参，因为[]定义了一个新的对象，改变了data实参和data形参之间的关系，形参data再也不是实参data的别名了，他们分别指向不同的对象。

**Default Parameter Values**

Python provides means for functions to support more than one possible calling signature(多种调用签名). Such a function is said to be polymorphic（多态）(which is Greek for “many forms”).(由于函数可以定义默认参数，这位函数调用提供了多种的形式【**可变数量的实参**】), 如：

**Example**:

	`def foo(a, b=15, c=27)
	 foo(4, 12, 8): 		=> a=4, b=12, c=8
	 foo(4):				=> a=4, b=15, c=27
	 foo(8, 20):			=> a=8, b=20, c=27`

仔细体会下面的例子：

	`def range(start, stop=None, step=1):
		if stop is None:
		stop = start
		start = 0`
**Note**: 当调用range(n)时，n并没赋值给start，而是传给了stop参数；

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

**Note**: print can output string or no string instance, print () outputs a single newline character. print has follow keyword parameters:

- The default separate character is space, The separator can be customized by 'sep=', the separator string can be a single character, or empty string, or a longer string.
- you can customize the end use 'end=' parameters.
- print can output to standard console, yet output to file.

**The input Function**
- input(prompt string): input从键盘接收输入,返回输入字符串对应表达式;
- raw_input(prompt string): 与inputag相比,返回的是字符串;

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
**example: 压包**
data = 2,4,6,8 #虽然后面的序列没有括号,但前面只有一个变量,后面自动压包成tuple,赋值给data;
return x, y

**example: 解包**
a, b, c, d = range(7, 11)
quotient, remainder = divmod(a, b)
for x, y in [ (7, 2), (5, 8), (6, 4) ]:
for k, v in mapping.items( ):

**Simultaneous Assignments**
**Note**:  combination of automatic packing and unpacking forms, as:x, y, z = 6, 2, 5

##1.10 Scopes and Namespaces##
**First-Class Objects**
**example**:
- scream = print #assign name ’scream’ call that function(函数(**函数也是对象**)可以赋予变量);
- scream( Hello ) #to the function denotedas’print
- max(a, b, key=abs)  #abs函数赋予key形参;



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