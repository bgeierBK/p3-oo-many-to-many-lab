class Author:
    def __init__(self, name:str):
        self.name = name
    
    def contracts(self):
        my_contracts = [contract for contract in Contract.all if contract.author == self ]
        return my_contracts
    
    def books(self):
        my_books = [contract.book for contract in Contract.all if contract.author == self ]
        return my_books
    
    def sign_contract(self, book: "Book", date:str, royalties:int):
    
    
      
      return Contract(author=self, book=book, date=date, royalties=royalties)
    
    def total_royalties(self):
        my_royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        return sum(my_royalties)
      
       
        
        


class Book:
    def __init__(self, title:str):
        self.title = title
    
    def contracts(self):
        my_contracts = [contract for contract in Contract.all if contract.book == self ]
        return my_contracts
    
    def authors(self):
        my_authors = [contract.author for contract in Contract.all if contract.book == self ]
        return my_authors


class Contract:
    all =[]
    
    
    def __init__(self, author:Author, book:Book, date:str, royalties:int):
        self.author = author
        self.book = book
        self.date = date
        self.royalties=royalties
        Contract.all.append(self)

        
    @property
    def author(self):
        return self._author
    
    @author.setter 
    def author(self, value):
        if type(value) == Author:
            self._author = value
        else:
            raise Exception("Author must be an author")
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if type(value) == Book:
            self._book = value
        else:
            raise Exception("Book must be an book")
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if type(value) == str:
            self._date = value
        else:
            raise Exception("Date must be an string")
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if type(value) == int:
            self._royalties = value
        else:
            raise Exception("Royalties must be an integer")
        

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
        