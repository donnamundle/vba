import numpy as np
import matplotlib.pyplot as plt
c = 1 # 尺度系数
k = 2 # 形状系数

def weib(x):
    """
威布尔分布函数
    @param x:
    @return:
    """
    return (k / c) * (x / c) ** (k - 1) * np.exp(-(x / c) ** k)

def weibull_fig():
    """
做威布尔概率密度函数
    """
    x = np.arange(1, 2500.) / 100.
    plt.plot(x, weib(x))
    plt.show()

if __name__ == '__main__':
    weibull_fig()