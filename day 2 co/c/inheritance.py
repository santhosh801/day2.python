class admin():
    def balance (self):
        print("35000912019k")

class memo(admin):
    def inb (self):
        print("120k")

class meme(memo):
    def inbb(self):
        print("110k")

class memd(meme,admin):
    def ib(self):
        print("100k")

ah=memd()
ah.ib()
ah.inbb()
ah.balance()



ak=meme()
ak.inbb()
ak.inb()

ai=memo()
ai.inb()
ai.balance()

ol=admin()
ol.balance()

    