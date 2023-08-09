from flask import Flask, jsonify, request

app = Flask(__name__)
 
#Mock
books = [
    {
        'id': 1,
        'title': 'Fox',
        'author': 'Toninho 1' 
    },
    {
        'id': 2,
        'title': 'Prince',
        'author': 'Toninho 2' 
    },
    {
        'id': 3,
        'title': 'Rose',
        'author': 'Toninho 3' 
    }
]

#Endpoints
#Get
@app.route('/getBooks', methods=['GET'])
def getBooks():
    return jsonify(books)

@app.route('/getBookById/<int:id>', methods=['GET'])
def getBookById(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

#Put
@app.route('/updateBook/<int:id>', methods=['PUT'])
def updateBook(id):
    bookReceived = request.get_json()
    for idReceived,book in enumerate(books):
        if book.get('id') == id:
            books[idReceived].update(bookReceived)
            return jsonify(books)
        
#Post
@app.route('/addBook', methods=['POST'])
def addBook():
    newBook = request.get_json()
    books.append(newBook)
    return jsonify(books)

#Delete
@app.route('/deleteBook/<int:id>', methods=['DELETE'])
def deleteBook(id):
    for idReceived, book in enumerate(books):
        if book.get('id') == id:
            del books[idReceived]
            return jsonify(books)

app.run(port=8080, host='localhost', debug=True);