#create super class
class Release:
    def __init__(self, name, writer, pages=None):
        self.name = name
        self.writereditor = writer
        self.pages = pages
    #make print thingy
    def printinfo(self):
        print(f"name: {self.name}")
        print(f"writer/editor: {self.writereditor}")
        if self.pages != None:
            print(f"pages: {self.pages}")
#book and comic details
class Book(Release):
    def __init__(self, name, writer, pages):
        super().__init__(name,writer,pages)
class Comic(Release):
    def __init__(self, name, writer):
        super().__init__(name,writer)

#insert the release's
book = Book("Hytti n:6", "Rosa Liksom", 200)
comic = Comic("Aku Ankka", "Aki Hyyppä")

#print info
book.printinfo()
#(to make it pretty)
print(" ")
comic.printinfo()