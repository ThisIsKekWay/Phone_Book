def searching(name):
    counter = 0
    with open('results.csv', 'w') as re:
        re.close()
    with open('book.csv', 'r') as f:
        line_count = sum(1 for line in open('book.csv'))
        for i in range(line_count):
            a = f.readline()
            if a.count(name) == 1:
                counter += 1
                with open('results.csv', 'a') as r:
                    r.write(a)
        if counter > 0:
            print(f'По вашему запросу найдено записей: {counter}')
        else:
            print('По вашему запросу ничего не найдено')
