class person():
    def __init__(self,n,o):
        print("hey i m a human")
        self.name=n
        self.occ=o
    # def func():
    #     print("Agrim Awesome!!")
    def info(self):
        # print(f"{self.name} is a {self.occ}")
        print(self.name, "is a", self.occ)
a=person("Agrim", "HR")
# b=func()
a.info()
