from sqlalchemy import func
# from datetime import datetime
from model import Book, User, Book_shelf, connect_to_db, db
from server import app 
from sys import argv


def load_books():
    """Load books from raw_books.csv into databaase"""

    
    enc = 'iso-8859-15'
    for row in open("raw_books.txt",'r', encoding=enc):
        #stackoverflow https://stackoverflow.com/questions/16528468/while-reading-file-on-python-i-got-a-unicodedecodeerror-what-can-i-do-to-resol?fbclid=IwAR2DFBQeizmZcKk7honBCgOMo60Jz4s654_9CA6PFLF8mv1Wfw3ADPeKGZ0

        row = row.rstrip()
    
        (indentifer, book_id,best_book_id,work_id,books_count,isbn,
        isbn13,authors,original_publication_year,original_title,title,
        language_code,average_rating,ratings_count,work_ratings_count,work_text_reviews_count,
        ratings_1,ratings_2,ratings_3,ratings_4,ratings_5,image_url,small_image_url) = row.split("\t")
        
        book = Book(book_id=book_id,
                    small_image_url=small_image_url,
                    author=authors,
                    title=title)

        db.session.add(book)
        db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data

    load_books()
