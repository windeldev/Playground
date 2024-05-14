from publication import Publication

class Book(Publication):
	def __init__(self, title: str, type: str, genre: str) -> None:
		self.genre = genre
		super().__init__(title, type)

	def get_book_details(self):
		print("Title:", self.title)
		print("Type:", self.type)
		print("Genre:", self.genre)

curr_book = Book("Harry Potter", "Book", "Fiction")
curr_book.get_book_details()
