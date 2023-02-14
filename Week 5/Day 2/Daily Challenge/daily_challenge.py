class Pagination:
    def __init__(self,items:list,pagesize=10):
        self.items = items
        self.pagesize = pagesize

alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

p = Pagination(alphabetList, 4)

