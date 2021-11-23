s = input()
l = s.split(" ")
m = list(map(int, l))
book = []
if len(m)%2!=0:
    seperate = max(m)
    m.remove(seperate)
    while len(m)!= 0:
        books = max(m) + min(m)
        book.append(books)
        m.remove(max(m))
        m.remove(min(m))    
if len(m)%2 == 0:
    while len(m)!= 0:
        books = max(m) + min(m)
        book.append(books)
        m.remove(max(m))
        m.remove(min(m))
print(books)
    
    
    
