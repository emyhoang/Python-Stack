class MathDojo():
    def __init__(self):
        self.result = 0

    def get_sum(self, args):
        sum = 0 
        for i in range (len(args)):
            if type(args[i]) is list:
                for j in range (len(args[i])):
                    sum += args[i][j]
            else:
                sum += args[i]
        return sum

    def add(self, *args): 
        self.result += self.get_sum(args)
        return self

    def subtract(self, *args):  
        self.result -= self.get_sum(args)
        return self

x = MathDojo().add(2).add([2],5,1).subtract(3,2).result
print(x) 