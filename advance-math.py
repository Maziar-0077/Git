import random

def f(x: float) -> float:
    return x ** 2

def df(x: float) -> float:
    return 2 * x



def Optimizer(max_iterations: int, lr: float) -> float:
    x = random.randint(0, 1)
    for i in range(max_iterations):
        dx = df(x)
        x -= lr * dx
    return x

print(Optimizer(100, 0.1))
