#Rewrite the entire Task 1 C using Data frames instead of lists
import pandas as pd

bookDetails = ({
        'book_id':[int(input("Enter the book ID: "))],
        'title':  [input("Enter the book tittle: ")],
        'author': [input("Enter the book author: ")],
        'status': ["Available"],

     })

dfB = pd.DataFrame(bookDetails)

print("dataFrame for books: ",dfB)



memberD = ({
        'members.id': [232],
        'name': ["Thokozani"],
        'borrowed_book': [[]],
    })

dfm = pd.DataFrame(memberD)

print ("dataFrame for the member: ", dfm)

