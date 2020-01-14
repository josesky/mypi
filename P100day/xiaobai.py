class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42

obj_a = TestA()

print(obj_a.attr)
print(TestA.__dict__)
print(obj_a.__dict__)
