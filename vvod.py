def writing_phone_book(data):
    with open('book.csv', 'a') as f:
        f.write(data)
        f.write('\n')
