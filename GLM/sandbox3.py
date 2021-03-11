from collections.abc import Mapping

class TestClass(Mapping):
    def __init__(self,a,b):
        self.payload = {}

        self.payload['a'] = a
        self.payload['b'] = b

    def __iter__(self):
        for k in self.payload.keys():
            yield k

    def __len__(self):
        return len(self.payload)        

    def __getitem__(self, key):
        return self.payload[key]

qq = {'c':3, 'd': 4}
print({**qq})


q = TestClass(1,2)


print({**q})
print(len(q))