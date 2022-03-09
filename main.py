import numpy as np
import math
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


class Wave:
    # конструктор, на выход выборка и ссылка на вейвлет функцию
    def __init__(self, selection, psi):
        self.__selection=selection.copy() #выборка
        self.__c = min(selection) #минимальное значения выборки
        self.__d = max(selection) #максимальное значение выборки
        self.__n = len(selection) #количество элементов в выборке
        self.__N = 9 #число членов ряда (параметр сглаживания)
        self.psi=psi # ссылка на вейвлет функцию

    def ProbabilityDensity(self, t):
        result=0
        for i in range(self.__n):
            result+=self.Wn(t,self.__selection[i])
        return result/self.__n

    #функция дубль-в
    def Wn (self, t, x):
        koef=1/(math.sqrt(self.__d-self.__c))
        result=0
        for i in range(self.__N):
            result+=koef*self.psi_i(i, (t-self.__c)/(self.__d-self.__c) )*koef*self.psi_i(i, (x-self.__c)/(self.__d-self.__c) )
        return result

    # функция пси i-ая, на вход i и аргумент функции
    def psi_i (self, i, t):
        if i==0:
            return 1
        list_koef=self.getKoefForPsi_i(i+1)
        k=list_koef[0]
        j=list_koef[1]
        return (math.pow(2,k/2)*self.psi( math.pow(2,k) * t - (j-1) ))

    # Функция которая вернет k и j списком [k,j]  для пси i-ой
    def getKoefForPsi_i(self,i):
        k = 0
        j = 1
        while True:
            while (j <= math.pow(2, k)):
                if (i == math.pow(2, k) + j):
                    return [k, j]
                j += 1
            j = 1
            k += 1





# получить набор случайных чисел, по нормальному распределению
def getRandomNormalArray(size):
    return np.random.normal(size=size)

# зписать содержимое массива ar в файл с именем name, на случай атомной войны
def writeArrayToFile(ar,name):
    f=open(f'{name}', 'w')
    for i in range(len(ar)):
        f.write(ar[i] + " ")
    f.close()

# Гаусс третьего порядка
def gauss3(x):
    return x * (3 - x * x) * math.exp(-x * x / 2)

    # Гаусс четвертого порядка
def gauss4(x):
    return -(3 - 6 * math.pow(x, 2) + math.pow(x, 4)) * math.exp(-x * x / 2)



if __name__ == '__main__':
    print('No inplementation')


test_section=getRandomNormalArray(50)
test=Wave(test_section, gauss3)

x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
f_x=[]
for i in x:
    f_x.append(test.ProbabilityDensity(i))

plt.plot(x, f_x)
plt.show()
