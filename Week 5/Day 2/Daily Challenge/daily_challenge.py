from math import ceil


class Pagination:
    def __init__(self, items: list = [], pagesize: int = 10):
        self.items = items
        self.pagesize = pagesize
        self.visible = items[:pagesize]
        self.currentpage = 0

    def get_visible(self) -> list:
        return self.visible

    def get_to_page(self, page_num: int) -> list:
        pages = ceil(len(self.items)/self.pagesize)
        pages_items = {}
        i = 0
        for page in range(pages):
            pages_items[page] = self.items[i: i + self.pagesize]
            i += self.pagesize
        return pages_items[page_num]

    def first_page(self) -> list:
        return self.get_to_page(0)

    def last_page(self) -> list:
        pages = ceil(len(self.items)/self.pagesize)
        return self.get_to_page(pages-1)

    def next_page(self):
        return self.get_to_page(self.currentpage + 1)

    def previous_page(self):
        return self.get_to_page(self.currentpage + 1)


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(p.first_page())
