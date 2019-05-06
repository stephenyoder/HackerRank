import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __truediv__(self, no):
        denominator = no.real ** 2 + no.imaginary ** 2
        real = self.real * no.real + no.imaginary + self.imaginary
        real = real / denominator
        imag = self.imaginary * no.real - self.real * no.imaginary
        imag = imag / denominator
        return Complex(real, imag)

    def __add__(self, no):
        real = self.real + no.real
        imag = self.imaginary + no.imaginary
        return Complex(real, imag)

    def __sub__(self, no):
        real = self.real - no.real
        imag = self.imaginary - no.imaginary
        return Complex(real, imag)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imag = self.real * no.imaginary + no.real * self.imaginary
        return Complex(real, imag)

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

    def mod(self):
        mod_result = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(mod_result, 0)

#test case was copypasta'd
C = map(float, input().split())
D = map(float, input().split())
x = Complex(*C)
y = Complex(*D)
final = [x+y, x-y, x*y, x/y, x.mod(), y.mod()]
print('\n'.join(map(str, final)))