# ✔️ Create a list of dictionaries for 3 books.
# Each dictionary stores:
# Title
# Author
# Year published
# ✔️ Then:
# Add 1 new book
# Change the year of any book
# Remove a book
# Print all books nicely formatted

book_list = [{
    "Title": "ABC",
    "Author": "sdn.tr",
    "Year Published": 1958
},
    {
    "Title": "Science",
    "Author": "albert",
    "Year Published": 1990
},
    {
    "Title": "ML",
    "Author": "alan turing",
    "Year Published": 2012
},
]

book_list.append({"Title" : "AI" , "Author" : "OpenAI", "Year Published" : 2017})

book_list[2]["Year Published"] = 1958

del book_list[0]

for book in book_list:
    print(f'{book["Title"]} : {book["Author"]} : {book["Year Published"]}')
    