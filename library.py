#Library.py (Lab 10) [Shane Roeseberg]

class Library:
	def __init__(self):
		self.book = {}

	def add_book(self, book):
		if isinstance(book, Book):
			if not book.author in self.book.keys():
				self.book[book.author] = []
			self.book[book.author].append(book)
		else:
			pass

	def get_authors(self):
		return self.book.keys()

	def get_books_per_author(self):
		return self.book

class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

	def __str__(self):
		return str(self.title) + " " + str(self.author)
	def __unicode__(self):
		return unicode(self.__str__())
	def __repr__(self):
		return self.__str__()