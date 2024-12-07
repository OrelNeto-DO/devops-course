class Book: #now wtf is going no here
 def __init__(self, title, author, copies):
  self.title = title
  self.author = author
  self.copies = copies
 def __str__(self):
  return f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}"

class Library:
  def __init__(self, name):
    self.books = []
    self.name = name

  def add_book(self, book):
    self.books.append(book)

  def __str__(self) -> str:
    return f"Library contains {len(self.books)}"

  def list_books(self):
     for book in self.books:
       print(book)

  def find_by_title(self, title):
      """
      Search for a book by its title in the library's collection.

      Args:
          title (str): The title of the book to search for.

      Returns:
          Book: The book object if the title is found, otherwise None.
      """
      for book in self.books:
          if book.title == title:
              return book
      return None
      
  def most_popular_book(self):
    popular = self.books[0]
    for book in self.books[1:]:
        if book.copies > popular.copies:
            popular = book
    
    return popular

  def most_popular_book_using_sort(self):
    # sort books and return the last element
    sorted_books = sorted(self.books, key=lambda x: x.copies)
    return sorted_books[-1]


  
def main():
  library = Library("Sela1144 Library")
  b1 = Book("Python 101", "John Doe", 3)
  b2 = Book("Data Science Handbook", "Jane Smith", 5)
  library.add_book(b1)
  library.add_book(b2)
  library.add_book(Book("Harry Potter", "J.K. Rowling", 8))
  library.add_book(Book("Harry Potter 2", "J.K. Rowling", 100))
  library.add_book(Book("Harry Potter 3", "J.K. Rowling", 3))


  library.list_books()

  harry_potter_book = library.find_by_title("Harry Potter")
  if harry_potter_book:
      print("Harry Potter found")
  else:
      print("Harry Potter Not found")

  popular_book = library.most_popular_book_using_sort()
  print(f"The most popular book is {popular_book.title} by {popular_book.author}")
  

# MAIN
if __name__ == "__main__":
  main()