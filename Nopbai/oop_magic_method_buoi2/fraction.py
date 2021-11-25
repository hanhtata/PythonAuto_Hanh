
class Fraction:
    def __init__(self,nr,dr) :
        if(dr>0):
            self.nr=nr
            self.dr=dr
        else:
            self.nr=-nr
            self.dr=-dr
        
    @property
    def nr(self):
        return self._nr
    @property
    def dr(self):
        return self._dr
    @dr.setter
    def dr(self,dr):
            self._dr=dr
    @nr.setter
    def nr(self,nr):
            self._nr=nr
    def fr(self):
        return (str(self.nr)+"/"+str(self.dr))
    def hcf(self) :
        while self.dr != 0:
            m = self.nr % self.dr
            self.nr = self.dr
            self.dr = m
        return self.nr
    def reduce(self):
        x = self.nr
        y = self.dr
        while self.dr != 0:
            m = self.nr % self.dr
            self.nr = self.dr
            self.dr = m
        if(int(y/self.nr) == 1):
            return str(int(x/self.nr))
        return (str(int(x/self.nr))+"/"+str(int(y/self.nr)))
        
    def __add__(self,other):
        if isinstance(other, int) or isinstance(other, float)  :
            z = self.dr*other+self.nr
            return (str(z) +"/" +str(self.dr)) 
        elif isinstance(other, Fraction):
            z = self.dr*other.nr+ self.nr*other.dr
            return (str(z)+"/"+ str(other.dr*self.dr))
        else : return("Nhập đúng định dạng")
    
a=Fraction(22,-6)
b=1.2
print(a+b)


def hcf(x, y):
    x, y = abs(x), abs(y)
    hcf = x if x < y else y

    while hcf > 0:
        if x % hcf == 0 and y % hcf == 0:
            break

        hcf -= 1

    return hcf if hcf > 0 else None


class Fraction:
    def __init__(self, nr, dr=1):
        if dr == 0:
            raise ZeroDivisionError("Mẫu số phải khác 0")

        if dr < 0:
            self.nr = nr * -1
            self.dr = dr * -1
        else:
            self.nr = nr
            self.dr = dr

        self._reduce()

    def __repr__(self):
        return "0" if self.nr == 0 else str(self.nr) if self.dr == 1 else f"{self.nr}/{self.dr}"

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) + (other.nr * self.dr), self.dr * other.dr)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) - (other.nr * self.dr), self.dr * other.dr)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.nr, self.dr * other.dr)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.dr, other.nr * self.dr)

    def _reduce(self):
        n = hcf(self.nr, self.dr)

        if n:
            self.nr = int(self.nr / n)
            self.dr = int(self.dr / n)


fr = Fraction(2, 3)
other = Fraction(1.2, -5)
print(fr, other)

print()

print(fr + other)
print(fr - other)
print(fr * other)
print(fr / other)

print()

fr = Fraction(1, 2)
print(fr + 1)
print(fr - 1.5)
print(fr * 2)
print(fr / 2)
