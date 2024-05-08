class Movie:
    def __init__(self, title, cast, category, release_date, budget):
        self.title = title
        self.cast = cast
        self.category = category
        self.release_date = release_date
        self.budget = budget

    def get_title(self):
        return self.title

    def get_cast(self):
        return self.cast

    def get_category(self):
        return self.category

    def get_release_date(self):
        return self.release_date

    def get_budget(self):
        return self.budget

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Cast: {self.cast}\n" \
               f"Category: {self.category}\n" \
               f"Release Date: {self.release_date}\n" \
               f"Budget: ${self.budget:.3f}\n"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return self.title == other.title


class User:
    def __init__(self, email):
        self.email = email
        self.favorites = []

    def get_email(self):
        return self.email

    def add_favorite(self, movie):
        if movie not in self.favorites:
            print("Movie added to your favorite list.")
            self.favorites.append(movie)
        else:
            print("Movie already exists in your favorite list.")

    def remove_favorite(self, movie):
        self.favorites.remove(movie)

    def get_favorites(self):
        return self.favorites

    def __str__(self):
        return f"Email: {self.email}\n" \
               f"Favorites: {len(self.favorites)} movies\n"
