class A:
    def simple(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t
        self.simple_interest = (p * r * t) / 100
        print("The simple interest is:", self.simple_interest)


class B(A):
    def compound(self, n):
        self.n = n
        self.compound_interest = self.p * (1 + self.r / (100 * n)) ** (n * self.t) 
        print("The compound interest is:", self.compound_interest)


class C(B):
    def difference(self):
        self.difference = self.compound_interest - self.simple_interest
        print("The difference of compound interest and simple interest is:", self.difference)


# Main program
obj1 = C()

p = float(input("Enter the value of principal (p): "))
r = float(input("Enter the rate of interest (r): "))
t = float(input("Enter the time in years (t): "))
n = int(input("Enter the number of times interest is compounded per year (n): "))

obj1.simple(p, r, t)
obj1.compound(n)
obj1.difference()
