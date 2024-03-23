"""Task 1: Data Structures Implementation (lists and data frames for managing books and 
members)    Each member dictionary includes an empty list for borrowed_books to track the IDs of books each member has borrowed.
Sequence hint: initialize two variables as lists, then create two functions as per the above requires. An 
example of the appending part of the question is as follows:
books.append({
 "book_id": book_id,
 "title": title,
 "author": author
 })
You must use the same procedure for all append"""

#Initialize two data structures to keep track of books and members both represented as lists
books = []
members = []

#The system features two functions (You must create these functions): add_book and add_member.
#The add_bookfunction takes three parameters (book_id, title, author, status) and appends a new book dictionary to the books list.

def add_book (book_id, title, author, status):
    books.append ({
        'book_id': book_id,
        'title': title,
        'author': author,
        'status': status,

     })
#Each member dictionary includes an empty list for borrowed_books to track the IDs of books each member has borrowed.
#The add_member function, on the other hand, requires two parameters (member_id, name) and appends a new member dictionary to the members list.
    
def add_members (member_id, name):
    members.append ({
        'members.id': member_id,
        'name': name,
        'borrowed_book': [],
    })

"""Task 1 A:
Suppose you use the system to add a book titled "Python Programming" written by Jacob Zuma with a 
book_id of 2024001, and a member named Anelisa Maleka with a member_id of 1. How would these 
additions reflect in the books and members lists, and what would the output look like if you printed 
both lists immediately after these additions?"""


#Hint: call the functions 
add_book (2024001,  "Python Programming", "Jacob Zuma", "Available")
add_members(1, "Anelisa Maleke")

#write a print statement for them
print ("Books")
for book in books:
    print(book)

print("\nMembers")
for members in members:
    print(members)
    
