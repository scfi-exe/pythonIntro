# classes are blueprints
# objects are the actual things you build
# variables are called attributes (propeties)
# functions are called methods


class Movie:
    def __init__(self, title, year, imdb_score, have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

    def nice_print(self):
        print(
            f"Movie Name: {self.title}\nYear of Production: {self.year}\nIMDB Score: {self.imdb_score}\nHave Seen?: {self.have_seen}\n"
        )


film1 = Movie("Life of Scott", 1997, 8.5, True)
film2 = Movie("Life of Jay", 2003, 8.5, True)

film1.nice_print()
Movie.nice_print(film2)

films = [film1, film2]
print(films[1].title, films[0].title)
