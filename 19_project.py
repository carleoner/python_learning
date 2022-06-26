from secrets import choice
# ../data/19_database.txt


class Library:
    def __init__(self, bookslist, name):
        self.name = name
        self.bookslist = bookslist
        self.lendDic = {}

    def displayBooks(self):
        print(f"Books in {self.name} catalogue:")
        for book in self.bookslist:
            print(book)
    
    def displayBorrowed(self):
        print("Borrowed books: ")
        for bookBorrowed in self.lendDic.keys():
            print(f"\"{bookBorrowed}\" borrowed by: {self.lendDic[bookBorrowed]}")
    
    def addBook(self, book):
        if book in bookslist:
            print("Book already exists")
        else:
            self.bookslist.append(book)
            bookDatabase = open(databaseName, 'a')
            bookDatabase.write('\n')
            bookDatabase.write(book)
            bookDatabase.close()
            print("Book added")

    def lendBook(self, book, user):
        if book in bookslist:
            if book not in self.lendDic.keys():
                self.lendDic.update({book: user})
                print(f"Book \"{book}\" has been lended to {user}")
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

    def removeBook(self, book):
        if book in self.bookslist:
            self.bookslist.remove(book)
            bookDatabase = open(databaseName, "r")
            all_bookDatabase_lines = bookDatabase.readlines()
            bookDatabase.close()

            bookDatabase = open(databaseName, "w")
            for book_line in all_bookDatabase_lines:
                if book_line.strip("\n") != book:
                    bookDatabase.write(book_line)
            bookDatabase.close()
            print("Book removed from the DataBase")
        else:
            print("You cannot remove a book that do not exist in a DataBase")

def main():
    while(True):
        print(f"\nWelcome to {lib.name}")

        choice = '''
        1. Display BookList
        2. Lend a Book
        3. Add a Book
        4. Return a Book
        5. Remove a Book from the DataBase
        6. Borrowed books with names
        '''

        print(choice)
        
        userInput = input("Press Q to quit, press C to continue: ")
        if userInput == 'C':
            try:
                userChoice = int(input("Select an option: "))
            except ValueError as e:
                print("It should be a number!!!")
            finally:
                if userChoice == 1:
                    lib.displayBooks()
                elif userChoice == 2:
                    book = input("Name: ")
                    user = input("User: ")
                    lib.lendBook(book, user)
                elif userChoice == 3:
                    book = input("Name: ")
                    lib.addBook(book)
                elif userChoice == 4:
                    book = input("Name: ")
                    lib.returnBook(book)
                elif userChoice == 5:
                    book = input("Name: ")
                    lib.removeBook(book)
                elif userChoice == 6:
                    lib.displayBorrowed()
                else:
                    print("Enter a valid option")
        elif userInput == 'Q':
            break
        else:
            print("Enter a valid option")

# Program execution
if __name__ == '__main__':
    bookslist = []
    databaseName = input("Enter name of the DataBase file with extension: ")
    bookDatabase = open(databaseName, "r")
    for book in bookDatabase:
        bookslist.append(book.strip())
    bookDatabase.close()
    lib = Library(bookslist, "PythonX_library")
    main()
    
    del bookslist