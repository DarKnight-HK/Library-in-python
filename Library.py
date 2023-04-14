#Main class
class Library:

#Function to define books
    def __init__(self, books):
        self.listbook = books
#List all the books
    def listbooks(self):
#Checks if the list isn't empty and prints the list
        if not self.is_empty():
            for index, i in enumerate(self.listbook):
                print(index,":",i)
        else:
            print("We ran out of books")


#Function to issue books
    def issueBook(self, book):
        self.book = book
        if self.book in self.listbook:
            print(f"Your book \"{self.book}\" has been issued")
            self.listbook.remove(self.book)
        else:
            print("That book is not available at the moment")
#Function to return books       
    def returnBook(self,book):
        self.book = book
        self.listbook.append(self.book)
        print(r"Thanks for returning/adding the book")
        print(r"=========Here's the updated list=========: ")
        self.listbooks()
#Function to check is the list is empty        
    def is_empty(self):
        return len(self.listbook)==0
#List of books
blist = ["Django", "Python","C++"]
lib = Library(blist)


while True:
    print(r''' =========Welcome to our Library========= 
    1. Get list of all the books
    2. Issue a book
    3. Return/Add a book
    4. Exit ''')
    a = int(input("Enter your choice: "))
    if a == 1:
        print("=========Here's a list of all the books=========")
        lib.listbooks()
    elif a == 2:
        while True:
            print("=========Here's a list of all the books=========")
            lib.listbooks()
            b = int(input("Enter your choice or enter 69 to go back: "))
            if b !=69:
                try:
                    lib.issueBook(blist[b])
                except Exception as e:
                    print(e)              
            else:
                break
    elif a == 3:
        a = input("Enter the name of the book you want to return/add: ")
        lib.returnBook(a)
    elif a==4:
        print("Thanks for choosing our Library")
        break
    else:
        print("Enter a valid option: ")
        continue