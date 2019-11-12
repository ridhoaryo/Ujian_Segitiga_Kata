words = input('Input words: ').replace(' ', '')

def word_triangle(sentences):  
    sen_list = list(sentences)
    rules = []
    for a in range(len(sen_list)):
        x = int((a*(a+1))/2)
        rules.append(x)

    n=0
    if len(sen_list) not in rules:
        print ('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
    else:
        n= rules.index(len(sen_list)) 
    y = 0
    for i in range(0, n): 
        for j in range(0, i+1): 
            print(sen_list[y], end=" ")  
            y += 1
        print("\r")   
    z = 0
    for i in range(n, 0, -1): 
        for j in range(1, i+1): 
            print(sen_list[z], end=" ")  
            z += 1
        print("\r") 

word_triangle(words)