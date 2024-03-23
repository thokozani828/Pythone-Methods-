#Rewrite the entire task 1B without using functions

#Initialize two data structures to keep track of books and members both represented as lists
books = []
members = []


bookDetails = ({
        'book_id': int(input("enter book ID:")),
        'title': input("Enter a book Title:"),
        'author': input("Enter the Book Author:"),
        'status': input("Enter the status:"),

     })

books.append(bookDetails)


memberD = ({
        'members.id': 232,
        'name': "Thokozani",
        'borrowed_book': [],
    })

members.append(memberD)


#write a print statement for them
print ("Books")

for book in books:
    print(book)

print("\nMembers")

for members in members:
    print(members)
    
