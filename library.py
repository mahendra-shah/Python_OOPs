class Library:

    def l__init__(self, book):
        self.booklist = lis
        self.name = name
        self.lendDict = {}


    def displayBook(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)


    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated, you can take the book now!")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.booklist.remove(book)



if __name__ == '__main__':
    mahendra = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'Python Basics', 'Game of Thrones', 'Dark'],'Mahendra')
    
    while (True):
        print("Welcome to the {mahendra.name} library, Enter your choice to continue")
        print("1, Display Book")
        print("2, Lend a Book")
        print("3, Add a Book")
        print("4, Return a Book")
        userChoice = int(input("Type a option: "))
        if userChoice == 1:
            mahendra.displayBook()

        elif userChoice == 2:
            book = input("Enter the name of the book you want to lend")
            name = input("Enter book name: ")
            mahendra.lendBook(user, book)
        
        elif userChoice == 3:
            book = input("Enter the name of the book you want to add")
            name = input("Enter book name: ")
            mahendra.returnBook(book)

        elif userChoice == 4:
            pass

        else:
            print("Not a valid option :(")
        
        print("Press q to quit or c to continue")
        userChoice2 = ''
        while (userChoice2 != 'c' and userChoice2 != 'q'):
            userChoice2 = input()
            if userChoice2 == 'c':
                continue
            elif userChoice2 == 'q':
                exit()
        