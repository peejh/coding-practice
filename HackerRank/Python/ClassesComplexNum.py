# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
       
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        mul_real = self.real * no.real - self.imaginary * no.imaginary
        mul_imag = self.real * no.imaginary + self.imaginary * no.real
        return Complex(mul_real, mul_imag)

    def __truediv__(self, no):
        denominator = no.real**2 + no.imaginary**2
        div_real = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        div_imag = (self.imaginary * no.real - self.real * no.imaginary) / denominator
        return Complex(div_real, div_imag)

    def mod(self):
        mod_real = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(mod_real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')