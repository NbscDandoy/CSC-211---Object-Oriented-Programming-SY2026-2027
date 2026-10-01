class ReadingList:
    def __init__(self):
        self._books = [] 

    def add_book(self, title):
        self._books.append(title)

    def titles(self):
        return list(self._books)  

    def account(self):
        return len(self._books)


personal = ReadingList()
team = ReadingList()
personal.add_book("Python Basic")
personal.add_book("OOP")
team.add_book("Testing")
external = personal.titles()
external.append("Outside")
print(personal.account())
print(team.account())