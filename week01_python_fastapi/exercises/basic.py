#统计词出现次数
def wordcount(text:str) ->dict[str,int]:
    words = text.lower().split()
    result = {}

    for word in words:
        result[word] = result.get(word,0)+1
    
    return result

if __name__ =="__main__":
    text = "LLM is useful and LLM is powerful"
    print (wordcount(text)) 





 # 读取文件
def read_file(path:str) -> str:
    with open(path,'r',encoding="utf-8") as f:
        return f.read()
    
if __name__ == "__main__":
    print(read_file("D:/llm-learning-journey/week01_python_fastapi/exercises/sample.txt"))
     





# 定义一个用户类：
class User:
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and my user ID is {self.user_id}."

if __name__ == "__main__":
    user = User("Alice", 123)
    print(user.greet())





#异常处理
def safe_divide(a:float,b:float) ->float:
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return 0.0
    
if __name__ == "__main__":
    print(safe_divide(10.0,2.0))
    print(safe_divide(10.0,0.0))





 #类型标注
def build_prompt(question:str,context:str|None = None) -> str:
    if context:
        return f"Question: {question}\nContext: {context}"
    else:
        return f"Question: {question}"
    
if __name__ == "__main__":
    print(build_prompt("FastApi 是什么？"))
    print(build_prompt("FastApi 是什么？", "FastApi 是一个现代、快速（高性能）的 Web 框架，用于构建 API。"))



# 装饰器题目

# 题目1：判断下面代码输出什么？
def log(func):
    def wapper():
        print("start execute")
        func()
        print("over")
    return wapper

@log   # say_hallo = log(say_hallo)
def say_hallo():
    print("Hello, World!")

say_hallo()




# 题目2：@log的作用是什么
@log
def say_hi():
    print("hi")
# 在不修改say_hi函数的情况下，让say_hi函数拥有其他的功能。




# 题目3：写一个装饰器，在函数执行前打印“函数即将运行”
def before_run(func):
    def wapper():
        print("func ready to run")
        func()
    return wapper

@before_run
def say_hello():
    print("1")

say_hello()





 # 题目4：
def log(func):
    def wapper():
        print("start")
        func()
        print("end")
    return wapper

@log
def add(a,b):
    return a+b

print(add(1,2)) 

 # 这里出现了报错，首先wapper()没有接收参数，但是调用的是add(1,2)
# 由于@log 装饰之后，add函数被wapper函数替代，而wapper函数没有接收参数。
# 解决方法是让wapper函数接收任意数量的参数，并将它们传递给原函数。
def log(func):
    def wapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wapper

@log
def add(a,b):
    return a+b

print(add(1,2))





# 题目5： 写一个装饰器，用于计算函数执行时间
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()

        result = func(*args,*kwargs)

        end = time.time()
        print(f"maybe {end - start} seconds")

        return result
    return wrapper

@timer
def slow_task():
    time.sleep(2)
    print("Slow task completed")

slow_task()







# 生成器题目

# 题目1： 判断代码输出什么？
def nums():
    yield 1
    yield 2
    yield 3

for n in nums():
    print(n)

# 1,2,3




# 题目2：nums()返回的是什么？
def nums():
    yield 1
    yield 2
    yield 3

result = nums()
print(result)
# 返回了一个生成器对象，不是列表，因为这里你并没有拿到里面的值，这只是一个生成器
# 正确的输出是：<generator object nums at 0x...>
# 想要在生成器中取出值，有两个办法，第一个办法 是使用 for 循环遍历生成器。
for n in result:
    print(n)    
# 第二个方法是： g = nums()  print(next(g))     print(next(g))





# 题目3：下面代码输出什么？
def demo():
    print("A")
    yield 1

    print("B")
    yield 2

    print("C")
    yield 3

for d in demo():
    print(d)
""" g = demo()
print(next(g))
print(next(g))
print(next(g)) """






# 题目4：yield和return 有什么区别？
# return是一次性返回所有的结果，而yield是逐个返回结果


#题目5：写一个生成器，生成1到5
def one_to_five():
    for i in range(1,6):
        yield i

for n in one_to_five():
    print(n)





# 题目6： 写一个生成器，模拟大模型流式输出
def stream_output():
    yield "FastApi"
    yield "is"
    yield "a"
    yield "modern"
    yield "and"
    yield "fast"
    yield "web"
    yield "framework"

for chunk in stream_output():
    print(chunk,end=" ")






# 装饰器和生成器一起使用
def log_generator(func):
    def wrapper(*args, **kwargs):
        print("开始")
        for item in func(*args, **kwargs):
            yield item
        print("结束")
    return wrapper


@log_generator
def stream():
    yield "A"
    yield "B"


for item in stream():
    print(item)
# 生成器真正迭代结束后再打印。