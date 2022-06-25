from secrets import choice


class library:
    def __init__(self, name, bookslist):
        self.name = name
        self.bookslist = bookslist
        self.lendDic = {}

    def displayBooks(self):
        print(f"Books in {self.name} catalogue:")
        for book in self.bookslist:
            print(book)
    
    def addBook(self, book):
        if book in self.bookslist:
            print("Book already exists")
        else:
            self.bookslist.append(book)
            print("Book added")

    def lendBook(self, book, user):
        if book in self.bookslist:
            if book not in self.lendDic.keys():
                self.lendDic.update({book: user})
                print(f"Book {book} lended to {user}")
            else:
                print(f"Book already lended to {self.lendDic[book]}")
        else:
            print(f"Book not in {self.name} library")

    def returnBook(self, book):
        if book in self.lendDic.keys():
            self.lendDic.pop(book)
            print(f"{book} returned")
        else:
            print("This book does not exist in Database, return to other library")

def main():

    lib = library("sak", "")
    while(True):
        print(f"Welcome to {lib.name}")

        choice = '''1. Display BookList
        2. Lend a Book
        3. Add a Book
        4. Return a Book'''

        print(choice)
        
        userInput = input("Press Q to quit, press C to continue")
        if userInput == 'C':
            userChoice = int(input("Select an option: "))
            if userChoice == 1:
                lib.displayBooks()
            elif userChoice == 2:
                book = input("Name: ")
                user = input("User: ")
                lib.lendBook()
            elif userChoice == 3:
                book = input("Name: ")
                lib.addBook(book)
            elif userChoice == 4:
                book = input("Name: ")
                lib.returnBook(book)
            else:
                print("Invalid option.")
        elif userInput == 'Q':
            break
        else:
            print("Invalid option")