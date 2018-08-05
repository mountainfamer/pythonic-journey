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