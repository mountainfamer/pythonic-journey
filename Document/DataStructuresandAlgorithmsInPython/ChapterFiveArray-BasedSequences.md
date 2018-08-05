5.基于数组的数据结构
5.2 低级数组
数组将一组有联系的变量存放在计一段连续的内存中，不同的变量都有对应的内存地址，变量的地址可以
通过数组的起始地址计算出来；其中存放的是int或characters，即 primary data,不是references；　
5.2.1 基于数组的其他数据类型
list和tuple这种指示型数据结构，可以把它的每个元素看成某个类的实例；　list中存放的是这些实例的参考；　
当对list进行切片时，结果是一个新的list对象，这个list中存放的也是实例的参考，参考对应的元素并没有变；　
primes = [2,3,5,7,11,13,17,19]
temp = primes[3:6]
temp[0] = primes[3]  	#指向相同的元素；　
temp[1] = primes[4]	#指向相同的元素；　
temp[2] = primes[5]	#指向相同的元素；　
当执行temp[2] = 15时，改变的只是temp[2]的参考，而不会对primes产生任何影响；　
浅拷贝：
对于list的＂浅＂拷贝，backup = list(primes)，产生一个新的数组，和primes一样其中存放的也是参考，
他们指向相同的元素对象；
初始化一个存放int类型元素的数组：counters = [0]*8,这８个cells均指向相同的object；
当执行了counters[2]+=1后，counters[2]指向的是另一个object；其他cells指向的还是相同object;
执行primes.extend(extras)后，primes后追加的不是object，而是references；　
5.2.2 compact Array(简洁数组)
compact Array中存放的是primary　data，不是references，它的好处是占用空间小，它不像reference　araray，
除了原始数据占用空间，references也要占用空间；　
compact array的定义: 
primes = array('i',[])  #'i'为类型代码；　
5.3 