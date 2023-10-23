class IteratorAttrs:

    def __iter__(self):
        print(self.__dict__.items())
        return iter(self.__dict__.items())


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone('model', 'size', 'memory')
for attr, value in phone:
    print(attr, value)
