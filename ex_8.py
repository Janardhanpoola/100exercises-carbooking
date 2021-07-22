class dictionary:
    def ep(self):
        d = dict(weather = "clima", earth = "terra", rain = "chuva")
        word=input("enter a word to know its portugese meaning    ")
        word=word.lower()
        for k in d:
            if word in d:
                print('portuguese mean is {}'.format(d[word]))
                break
        else:
            print("cant find it")

d=dictionary()

d.ep()