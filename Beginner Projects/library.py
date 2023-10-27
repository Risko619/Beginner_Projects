''' In this project, I created a Dictionary to store books, Tuples to store a books info and Sets to store Authors
'''

# Create variables and set Tuples with 3 values
hamlet_info = ("William Shakespeare", "Tragedy", 1603)
martian_chronicles_info = ("Ray Bradbury", "Science fiction", 1950)

# Create a variable to store and display books previously created
my_books = {
  "Hamlet":hamlet_info, "The Martian Chronicles":martian_chronicles_info
  }
print(f"My books: {my_books}")

# To add a book
my_books["Fahrenheit 451"] = ("Ray Bradbury", "Dystopian", 1953)
print(f'Fahrenheit 451 info: {my_books["Fahrenheit 451"]}')

# To check (in future) if an author is in a library
my_books_authors = set()

# To populate our set(), we need to check every book and it's author
for book in my_books:
  book_info = my_books[book]
# To find book: print(f"Book: {book} - info: {book_info}")
  author = book_info[0]
# To find author: print(f'Author: {author}')

# Add books and display the set containing authors
  my_books_authors.add(author)
print(f"Authors: {my_books_authors}")

# Now my_books_author is poplutated, let's try it out
is_my_author = "Ray Bradbury" in my_books_authors

# Lastly we display a message if author belongs to our authors
if is_my_author == True:
  print("Ray Bradbury belongs to my authors!")

''' We can play around by adding some more books and authors.
Or even display books with a publication year above 1949'''