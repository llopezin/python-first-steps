class Library():
    total_books = 0
    book_list = []
    READIBILITY_THRESHOLDS = {'short': 100, 'medium': 500}
    READIBILITY_VALUES = {'short': 'short', 'medium': 'mid sized', 'long': 'long'}

    @staticmethod
    def order_books(books):
        return list(sorted(books, key=lambda book: book['author'], reverse=True))

    @classmethod
    def from_string(cls, bookData):
        
        if not(isinstance(bookData, str)):
            raise Exception('Library - fromString expects a string as an argument')
        
        title, author, pages = bookData.split(',')
        return cls(title, author, int(pages))
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
    @classmethod
    def get_all_books(cls):
        return cls.book_list
    
    @classmethod
    def increment_book_total(cls):
        cls.total_books +=1
   
    @classmethod
    def add_book(cls, book):
        cls.book_list.append(book)
    
    def __init__(self, title, author, pages):
        self.title = title
        self._author=author
        self._pages=pages
        self._book={'title': title, 'author': author, 'pages': pages}
        Library.increment_book_total()
        Library.add_book(self._book)
    
    def get_author(self):
        return self._author
    
    def get_title(self):
        return self.title
    
    def get_readibility(self):
           if self._pages <= Library.READIBILITY_THRESHOLDS['short']:
                return Library.READIBILITY_VALUES['short']
           elif self._pages <= Library.READIBILITY_THRESHOLDS['medium']:
                return Library.READIBILITY_VALUES['medium']
           else:
               return Library.READIBILITY_VALUES['long']
           

def main():
    print('Hello, welcome to the library')
    my_py_book=Library.from_string('Learning Python, Rita Banana, 400')
    my_book=Library.from_string('Climbing like Monkeys, Lau Banana, 89')

    print('Total books is ' + str(Library.get_total_books()))
    print('Recommended book '+ my_py_book.get_title() +', by '+ my_py_book._author +', is '+ my_py_book.get_readibility())
    print('Recommended book '+ my_book.get_title() +' is '+ my_book.get_readibility())

    # I know this use below is unusual, it is creating a learning opportunity for staticmethods
    print('The available books are ')
    for book in Library.order_books(Library.book_list):
        print(book)

if __name__ == "__main__":
    main()



        

        


    














main()