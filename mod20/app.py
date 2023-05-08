import datetime


from sqlalchemy import Column, Integer, Text, create_engine, Float, Boolean, DateTime, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property

from flask import Flask, jsonify ,request

engine = create_engine('sqlite:///sqlite_python.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for  c in self.__table__.colums}

class Authors(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    @classmethod
    def get_students_with_scholarship(cls):
        return session.query(Students).filter(Students.scholarship is True)

    @classmethod
    def get_student_with_grater_score(cls, score):
        return session.query(Students).filter(Students.average_score > score)

class ReceivingBooks(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    def to_json(self):
        return {c.name: getattr(self, c.name) for  c in self.__table__.colums}

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
    session.query(ReceivingBooks)\
        .filter(ReceivingBooks.student_id == student_id and ReceivingBooks.book_id == book_id)\
        .update({ReceivingBooks.date_of_return: datetime.datetime.now()})

    session.commit()

    return 'Книга успешно возвращена', 200

@app.route("/get_book",  methods=["POST"])
def get_book():
    to_find = request.form.get('to_find')
    finds = session.query(Books).filter(Books.name.like(to_find))
    finds_list = []
    for find in finds:
        finds_list.append(find.to_json())

    return finds_list


if __name__ == "__main__":
    app.run(debug=True)
