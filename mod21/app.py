import csv
import datetime

from sqlalchemy import Column, Integer, Text, create_engine, Float, Boolean, DateTime, Date, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy

from flask import Flask, jsonify, request

engine = create_engine('sqlite:///sqlite_python.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Authors(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey(f"{Authors.__tablename__}.id"), nullable=False)

    author = relationship(Authors.__name__, backref=backref(__tablename__,
                                    cascade="all, delete-orphan",lazy="joined"))

    receiving_books = relationship("ReceivingBooks", back_populates='book',
                                    cascade="all, delete-orphan",lazy="joined")

    students = association_proxy("receiving_books", "student")

    def __init__(self, name:str, count:int,release_date:datetime, author_id):
        self.name = name
        self.count = count
        self.release_date = release_date
        self.author_id = author_id
    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.colums}





class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    receiving_books =  relationship("ReceivingBooks", back_populates='student',
                                    cascade="all, delete-orphan",lazy="joined")

    books = association_proxy('receiving_books', 'book')

    def __init__(self, id:int, name:str, surname:str, phone:str, email:str, average_score:float, scholarship:bool):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.average_score = average_score
        self.scholarship = scholarship

    @classmethod
    def get_students_with_scholarship(cls):
        return session.query(Students).filter(Students.scholarship is True)

    @classmethod
    def get_student_with_grater_score(cls, score):
        return session.query(Students).filter(Students.average_score > score)


class ReceivingBooks(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey(f"{Books.__tablename__}.id"),nullable=False)
    student_id = Column(Integer, ForeignKey(f"{Students.__tablename__}.id"),nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    book = relationship(Books.__name__, back_populates='receiving_books')
    student = relationship(Students.__name__, back_populates='receiving_books')

    def __init__(self, id:int, book_id:int, student_id:int, date_of_issue:datetime,date_of_return:datetime):
        self.id = id
        self.book_id = book_id
        self.student_id = student_id
        self.date_of_issue = date_of_issue
        self.date_of_return = date_of_return


    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.colums}

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return is None:
            return (datetime.datetime.now() - self.date_of_issue).days
        return (self.date_of_return - self.date_of_issue).day


app = Flask(__name__)


@app.before_request
def before_request():
    Base.metadata.create_all(engine)


@app.route("/books", methods=["GET"])
def get_all_books():
    books = session.query(Books).all()
    books_list = []
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list=books_list), 200


@app.route("/borrowers", methods=["GET"])
def get_borrowers():
    borrowers = session.query(ReceivingBooks).filter(ReceivingBooks.date_of_return == None)
    borrowers_list = []
    for borrower in borrowers:
        if borrower.count_date_with_book > 14:
            borrowers_list.append(borrower)
    return jsonify(borrowers_list=borrowers_list), 200


@app.route("/give_book", methods=["POST"])
def give_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    temp = ReceivingBooks(book_id=book_id,
                          student_id=student_id,
                          date_of_issue=datetime.datetime.now())
    session.add(temp)
    session.commit()

    return 'Книга успешно выдана', 201


@app.route("/return_book", methods=["POST"])
def return_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    session.query(ReceivingBooks) \
        .filter(ReceivingBooks.student_id == student_id and ReceivingBooks.book_id == book_id) \
        .update({ReceivingBooks.date_of_return: datetime.datetime.now()})

    session.commit()

    return 'Книга успешно возвращена', 200


@app.route("/get_book", methods=["POST"])
def get_book():
    to_find = request.form.get('to_find')
    finds = session.query(Books).filter(Books.name.like(to_find))
    finds_list = []
    for find in finds:
        finds_list.append(find.to_json())

    return finds_list

@app.route("/get_author_books_count", methods=["GET"])
def get_author_books_count():
    author_id = int(request.form.get('author_id'))
    books = session.query(Books.count).filter(Books.author_id == author_id)
    count = 0
    for book in books:
        count += book[0]
    return f"books with author_id {author_id} = {count}", 200

@app.route("/get_books_list_student_not_read", methods=["GET"])
def get_books_list_student_not_read():
    student_id = int(request.form.get('student_id'))
    student: Students = session.query(Students).filter(Students.id == student_id).scalar()
    books = map(lambda book: book.id, student.books)
    authors = session.query(Authors).subquery()
    books_list = session.query(Books).join(authors, Books.author_id == authors.columns.id)\
        .group_by(authors.columns.id).filter(Books.id.not_in(books)).all()

    return books_list, 200

@app.route("/get_avg_books_in_cur_month",methods=["GET"])
def get_avg_books_in_cur_month():
    books_count = session.query(func.count(ReceivingBooks.book_id)) \
        .group_by(ReceivingBooks.student_id) \
        .filter(func.extract('month', ReceivingBooks.date_of_issue) == datetime.datetime.now().month).subquery()
    books_count_average: float = session.query(func.avg(books_count)).scalar()
    return str(books_count_average), 200


@app.route("/get_most_popular_book_within_gpa_grater_4",methods=["GET"])
def get_most_popular_book_within_gpa_grater_4():
    books_count = session.query(Books.name.label("book"), func.count(ReceivingBooks.student_id).label("count")) \
        .group_by(ReceivingBooks.book_id) \
        .filter(Books.id == ReceivingBooks.book_id, Students.id == ReceivingBooks.student_id, Students.average_score > 4.0) \
        .subquery()
    most_popular_book: str = session.query(books_count.columns.book, func.max(books_count.columns.count)).scalar()
    if most_popular_book is None:
        most_popular_book = 'None'
    return most_popular_book, 200

@app.route('/get_top_10_students_bu_books_read',methods=["GET"])
def get_top_10_students_bu_books_read():
    top_students = session.query(Students.name) \
        .group_by(ReceivingBooks.student_id) \
        .filter(Students.id == ReceivingBooks.student_id) \
        .order_by(func.count(ReceivingBooks.book_id).desc()) \
        .limit(10) \
        .all()
    result = ''
    for i, val in enumerate(top_students, start=1):
        result += f'{i} - {val[0]}\n'
    return result, 200

@app.route("/set_students_data_from_csv", methods=["POST"])
def set_students_data_from_csv():
    students_data = request.files["students_data"]
    with open(students_data.filename, mode='r') as file:
        reader = csv.DictReader(file, delimiter=";")
        students: [Students] = [{
            "name": row["name"],
            "surname": row["surname"],
            "phone": row["phone"],
            "email": row["email"],
            "average_score": float(row["average_score"]),
            "scholarship": bool(row["scholarship"])
            } for row in reader]

        session.bulk_insert_mappings(Students, students)
        session.commit()
    return "Done", 200





if __name__ == "__main__":
    app.run(debug=True)
