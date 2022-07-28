import random

class randomacc:

    def __init__(self, ac, pw) -> None:
        self.ac = ac
        self.pw = pw
    
#random username
    def randomusernamea(self):
        a = random.randint(1000,10000)
        b = random.sample('zyxwvutsrqponmlkjihgfedcba',5)
        c = ("")

        for i in b:

            c = c + str(i)

        rendomusername = (str(self.ac)+str(a)+str(c))
        return rendomusername

 #random passwd   
    def randompasswda(self):
        a = random.randint(1000,10000)
        b = random.sample('zyxwvutsrqponmlkjihgfedcba@!#',5)
        c = ("")

        for i in b:

            c = c + str(i)

        rendompasswd = (str(self.pw)+str(a)+str(c))
        return rendompasswd

#accinfo = randomacc("actest", "pdtest")




