shelf_array=input().split('&')

def add(user_input):
    global shelf_array
    if user_input not in shelf_array:
        shelf_array.insert(0,user_input)
def take(user_input):
    global shelf_array
    if user_input in shelf_array:
        shelf_array.remove(user_input)

def swap(user_input):
    book1, book2=user_input.split(' | ')
    if book1 in shelf_array and book2 in shelf_array:
        index1=shelf_array.index(book1)
        index2=shelf_array.index(book2)
        shelf_array[index1], shelf_array[index2] = shelf_array[index2], shelf_array[index1]
def insert (user_input):
    if user_input not in shelf_array:
        shelf_array.append(user_input)
def check(user_input):
    user_input=int(user_input)
    if user_input>=0 and user_input<len(shelf_array):
        print(shelf_array[user_input])
action={"Add Book":add,"Take Book":take, "Swap Books":swap, "Insert Book":insert, "Check Book":check}
while True:
    initial_input=input()
    if initial_input=='Done':
        break
    user_input=initial_input.split(' | ')
    command=user_input[0]
    user_input.pop(0)
    altered=' | '.join(user_input)
    action[command](altered)

print(', '.join(shelf_array))

