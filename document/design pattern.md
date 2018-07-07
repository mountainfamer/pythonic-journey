#概念
OO是目标，设计原则是心法，设计模式是招数； 它们是从抽象到具体的演变。
- 设计模式: The lessons learned by those who've faed the same software design problems.(设计模式就过去人们面对同样的软件设计问题所学来的经验)，并有GOF首先总结提出； 
- OO: object oriented, 面向对象程序设计范型，它将对象作为程序的基本单元，将程序和数据封装其中，以提高软件的重用性、灵活性和扩展性。
- 设计原则： 设计原则是程序设计时遵循的高阶心法，以达到OO的目标。

## 基础->UML图及类之间的关系 ##
UML: Unified Modeling Language(统一建模语言).
类之间的关系：
- 继承关系：
![](https://i.imgur.com/fdzYc4D.png)
  子类或字接口继承父类或父接口，子类与父类之间是is-a的关系，父类一般是抽象的； 
- 实现关系：
![](https://i.imgur.com/OagMjLY.png)
  子类实现从父接口那里继承过来的接口； 
- 依赖关系：
![](https://i.imgur.com/TAP8rXz.png)
  类A与类B之间的关系具有偶然性，临时性，关系比较弱，但B类的变化会影响到A类；
- 关联关系：
  两个类或接口之间的一种强依赖关系，对比依赖关系，关联关系非偶然，非临时，一般是长期的；
![](https://i.imgur.com/FaQy9Qn.png)
- 聚合关系：
  聚合是关联关系的一种特例，体现整体与部分的，拥有的关系，是'has-a'的关系；
![](https://i.imgur.com/uAKGt7e.png)
- 组合关系：
  组合也是关联关系的一种特例，体现的是一种'contains-a'的关系，这种关系比聚合更强，他同样体现整体与部分的关系，但此时整体与部分是不可分的，部分的生命周期与整体的生命周期相同；
![](https://i.imgur.com/Mv4Yskj.png)
  组合->聚合->关联->依赖，体现了类之间的横向关系，这几种关系都是语义级别的，并非代码层面的； 它们之间是一种依次从强到弱的关系。

## OO Basics##
- Abstraction： 抽象
- Encapsulation： 封装
- Polymorphism： 多态
- Inheritance： 继承

##设计原则总览##
- Identify the aspects of your application that vary and separate them from what stays the same.(找出应用中可能需要变化之处，把它们独立出来， 不要和那些不需要变化的代码混在一起)
  Take what varies and "encapsulate" it so it won't affect the rest of yhour code. The result? Fewer unitiended consequences from code changes and more flexibility in your system!(把会变化的部分取出并“封装”起来，好让其他部分不会受到影响。结果如何？ 代码变化引起的不经意后果变少，系统变得更有弹性。)
- Program to an interface, not an mplementation.(针对接口编程， 而不是针对实现编程)
- Favor omposition over inheritance.(多用组合，少用继承)
- Strive for loosely coupled designs between objects that interact.(为了交互对象之间的松耦合设计而努力). Loosely coupled designs allow us to build flexible OO systems that can handle change because the minimize the interdependency between objects.(松耦合的设计之所以能让我们建立有弹性的OO系统，能够应对变化， 是因为对象之间的互相依赖降到了最低).
- Classed should be open for extension , but closed for modification.(类应该对扩展开放，对修改关闭).
- Dependency inversion priniple(依赖倒置原则)： Depend upon abstractions, Do not depend upon concrete classes.(要依赖抽象，不要依赖具体类). 
- Principle of Least Knowledge-talk only to your immediate friends.(最少知识原则：只和你的密友谈话).This principle prevents us from creating designs that have a large number of classes coupled together so that changes in one part of the system cascade to other parts.(这个原则希望我们在设计中，不要让太多的类耦合在一起，免得修改系统中一部分，会影响到其他部分).
- Don't call us, we'll call you.(别调用我们，我们会调用你).
- Single Responsibility principle,SRP(单一职责原则): A class should have only one reason to change.(一个应该只有一个引起变化的原因).Every responsibility of a class is an area of potential change. More than one responsibility means more than one area of change .This principle guides us to keep each class to a single responsibility.(类的每个责任都有改变的潜在区域。 超过一个责任，意味着超过一个改变的区域。这个原则告诉我们，尽量让每个类保持单一责任).

##设计模式## 
###一、strategy:策略模式###
参考：https://sourcemaking.com/design_patterns/strategy
####1. UML类图####
![](https://i.imgur.com/ndXKOrW.png)
这个模式设计设计三个角色：
- Context(环境): 持有一个Strategy的引用； 
- 抽象策略： 接口或算法的抽象； 
- 具体策略： 实现了抽象策略，包装了相关的算法或行为； 

**插播: 对策略的联想，策略的字面意思说明有“多种行为”方式可供选择，可以把“多种行为”看成是为解决问题而设计的“相关的算法或行为”。**

####2. intent(意图)####
- 定义了算法族，分别封装起来，让它们之间可以互相替代，此模式让算法的变化独立于使用算法的客户。
- 在接口中捕获抽象，在派生类中隐藏实现细节。

**插播: 为什么我在实际解决问题是想不到用什么设计模式呢？ 大概是因为对设计模式认识不深入，总寄希望于遇到问题后就找个设计模式来解决这个问题，殊不知，任何事情与设计模式之间都不是一一对应的关系，实际问题往往比单个设计模式复杂，或者是多个设计模式的组合，或者是设计模式加非设计模式的代码（这部分有可能被提炼成自己的设计模式）；因此，对于实际性问题，往往有先设计分解流程，在某个小模块的实现上，可以思考使用什么设计模式来提高程序的健壮性、弹性**

####3. scenes(场景)####
- 针对同一类型问题的"多种处理方式"，仅仅是具体行为有差别时； 
- 需要安全地封装"多种同样类型的操作"时；
- 同一抽象类有"多个子类"，而又需要使用if-else或者switch-case来选择具体子类时；

####4. codes(代码实例)####
Java 实现：
1. Define the interface of an interchangeable family of algorithms;
2. Bury algorithm implementation details in derived classes;
3. Derived classes could be implemented using the Template Method Pattern
4. Clients of the algorithm couple themselves strictly to he interface


	`interface Strategy{  //抽象接口
		void slove();
	}

	abstract class StrategySolution implements Strategy{ //算法族
		public void slove(){
			start();
    	    ........
		}
    	........
	}` 

	class FOO extends StrageSolution{	//具体算法
		........
	}

	abstract class StrategySearch implements Strategy{  //算法族
		public void slove(){
			start();
    	    ........
		}
    	........
	} 

	class BAR extends StrageSearch{		//具体算法
		........
	}
	
	//Clients couple strictly to the interface, Program to an interface, not an implementation;
	//Client as context;
	public class StrategyDemo{  		
		private static void execute(Strategy strategy){
			strategy.sole();	
		}
	
		public static void main(String[] args){
			Strategy[] algorithms = {new FOO(), new BAR()};
			for (Strategy algorithm : algorithms){
				execute(algorithm);
			}
		}
	}`

Python 实现：
    `import abc
	 
	 class Context:
	
		def __init__(self, strategy):
			self._strategy = strategy
		
		def context_interface(self):
			self._strategy.algorithm_interface()

	 class Stragety(metaclass=abc.ABCMeta):
		
		@abc.abstractmethod
		def algorithm_interface(self):
			pass
	 
	 class ConcreteStrategyA(Stragety):

		def algorithm_interface(self):
			pass

	 class ConcreteStrategyB(Stragety):

		def algorithm_interface(self):
			pass
	
	 def main():

		context_strategy_a = ConcreateStrategyA()
		context = Context(context_stragety_a)
		context.context_interface()

	 if __name__ == '__main__':
		main()`
说明：UML类图看涉及三个角色，在代码中保持着三部分的独立性、清晰性，有助于理解程序结构，包括后期维护方便。
###二、prototype:原型模式###
参考：https://sourcemaking.com/design_patterns/prototype
####1. UML类图####
![](https://i.imgur.com/ndXKOrW.png)
这个模式设计设计三个角色：
- Context(环境): 持有一个Strategy的引用； 
- 抽象策略： 接口或算法的抽象； 
- 具体策略： 实现了抽象策略，包装了相关的算法或行为； 

**插播: 对策略的联想，策略的字面意思说明有“多种行为”方式可供选择，可以把“多种行为”看成是为解决问题而设计的“相关的算法或行为”。**

####2. intent(意图)####
- 定义了算法族，分别封装起来，让它们之间可以互相替代，此模式让算法的变化独立于使用算法的客户。
- 在接口中捕获抽象，在派生类中隐藏实现细节。

**插播: 为什么我在实际解决问题是想不到用什么设计模式呢？ 大概是因为对设计模式认识不深入，总寄希望于遇到问题后就找个设计模式来解决这个问题，殊不知，任何事情与设计模式之间都不是一一对应的关系，实际问题往往比单个设计模式复杂，或者是多个设计模式的组合，或者是设计模式加非设计模式的代码（这部分有可能被提炼成自己的设计模式）；因此，对于实际性问题，往往有先设计分解流程，在某个小模块的实现上，可以思考使用什么设计模式来提高程序的健壮性、弹性**

####3. scenes(场景)####
- 针对同一类型问题的"多种处理方式"，仅仅是具体行为有差别时； 
- 需要安全地封装"多种同样类型的操作"时；
- 同一抽象类有"多个子类"，而又需要使用if-else或者switch-case来选择具体子类时；

####4. codes(代码实例)####
Java 实现：
1. Define the interface of an interchangeable family of algorithms;
2. Bury algorithm implementation details in derived classes;
3. Derived classes could be implemented using the Template Method Pattern
4. Clients of the algorithm couple themselves strictly to he interface


	`interface Strategy{  //抽象接口
		void slove();
	}

	abstract class StrategySolution implements Strategy{ //算法族
		public void slove(){
			start();
    	    ........
		}
    	........
	}` 

	class FOO extends StrageSolution{	//具体算法
		........
	}

	abstract class StrategySearch implements Strategy{  //算法族
		public void slove(){
			start();
    	    ........
		}
    	........
	} 

	class BAR extends StrageSearch{		//具体算法
		........
	}
	
	//Clients couple strictly to the interface, Program to an interface, not an implementation;
	//Client as context;
	public class StrategyDemo{  		
		private static void execute(Strategy strategy){
			strategy.sole();	
		}
	
		public static void main(String[] args){
			Strategy[] algorithms = {new FOO(), new BAR()};
			for (Strategy algorithm : algorithms){
				execute(algorithm);
			}
		}
	}`

Python 实现：
