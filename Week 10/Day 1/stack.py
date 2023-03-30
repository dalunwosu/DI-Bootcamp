class Superstack():
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(int(data))

    def pop(self):
        self.stack.pop()
    
    def inc(self, nums, add):
        for i in range (int(nums)):
            self.stack[i]+= int(add)
    
    def run (self, commands: list):
        operations = {
            'push' : self.push,
            'pop': self.pop,
            'inc': self.inc
        }

        for command in commands:
            com, *args = command.split(' ')

            if com == 'push':
                self.push(*args)
            if com == 'pop':
                self.pop()
            if com == 'inc':
                self.inc(*args)

    def print(self):
        for items in self.stack:
            print(items)
    
            
super_stuck = Superstack()
super_stuck.run(['push 4', 'push 5', 'push 6',
                'inc 2 1', 'inc 1 3', 'pop', 'pop'])

super_stuck.print()
            
