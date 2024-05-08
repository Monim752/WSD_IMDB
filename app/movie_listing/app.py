from app.movie_listing.model import User


class MovieListingApp:
    def __init__(self):
        self.movies = []
        self.users = []
        self.current_user = None

    def main(self):
        while True:
            if self.current_user is None:
                self.handle_login_screen()
            else:
                self.handle_user_menu()

    def handle_login_screen(self):
        print("\nWelcome to Movie Listing Application ")
        print("\nAvailable Choices \n ")
        print("1. Register with your email")
        print("2. Login with your email")
        print("3. Exit the application")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            email_to_register = input("Enter your email to register: ")
            self.register_user(email_to_register)
        elif choice == 2:
            email_to_login = input("Enter email to login: ")
            self.login_user(email_to_login)
            if self.current_user is not None:
                print("Successfully Logged in!")
        elif choice == 3:
            print("Exit the application.")
            return
        else:
            print("Invalid choice. Please try again.")

    def handle_user_menu(self):
        print("\nYour available choices \n ")
        print("1. Search movies")
        print("2. Add Movie to your favorite list")
        print("3. Remove movie from your favorite list")
        print("4. View personal details")
        print("5. Search movies from your favorite list")
        print("6. Logout")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            keyword = input("Enter keyword for search: ")
            search_result = self.search_movies(keyword)
            if not search_result:
                print("No movies found for the given keyword.")
            else:
                print("Search results:")
                for movie in search_result:
                    print(movie)
        elif choice == 2:
            title_to_add = input("Enter movie title to add to your favorites: ")
            movies_to_add = self.search_movies_by_title(title_to_add)
            if not movies_to_add:
                print("Movie not found.")
            else:
                print("Select a movie to add to your favorites:")
                for i, movie in enumerate(movies_to_add, 1):
                    print(f"{i}. {movie.get_title()}")
                movie_choice = int(input("Enter your choice: "))
                if 1 <= movie_choice <= len(movies_to_add):
                    self.add_to_favorites(self.current_user, movies_to_add[movie_choice - 1])
                else:
                    print("Invalid choice.")
        elif choice == 3:
            self.remove_from_favorites()
        elif choice == 4:
            self.view_user_profile()
        elif choice == 5:
            self.search_favorites()
        elif choice == 6:
            self.logout_user()
            print("Logged out Successfully!.")
        elif choice == 7:
            print("Exit the application!")
            return
        else:
            print("Invalid choice. Please try again.")

    def add_movie(self, movie):
        if movie not in self.movies:
            self.movies.append(movie)
        else:
            print("Movie already exists. Please try a different one!")

    def register_user(self, email):
        for user in self.users:
            if user.get_email() == email:
                print("User already exists. Please log in!")
                return
        user = User(email)
        self.users.append(user)
        print("User registered Successfully!")

    def login_user(self, email):
        for user in self.users:
            if user.get_email() == email:
                self.current_user = user
                return
        print("User not found. Please register!")

    def logout_user(self):
        self.current_user = None

    def search_movies(self, keyword):
        result = []
        for movie in self.movies:
            if keyword.lower() in movie.get_title().lower() or \
                    keyword.lower() in movie.get_cast().lower() or \
                    keyword.lower() in movie.get_category().lower():
                result.append(movie)
        result.sort(key=lambda x: x.get_title())
        return result

    def search_movies_by_title(self, title):
        result = []
        for movie in self.movies:
            if title.lower() in movie.get_title().lower():
                result.append(movie)
        return result

    def add_to_favorites(self, user, movie):
        user.add_favorite(movie)
        print("Movie added to your favorites.")

    def remove_from_favorites(self):
        if not self.current_user.get_favorites():
            print("No movies in favorites to remove.")
            return
        print("Favorite Movies:")
        for i, movie in enumerate(self.current_user.get_favorites(), 1):
            print(f"{i}. {movie.get_title()}")
        index_to_remove = int(input("Enter index number of movie to remove from your favorites: "))
        if 1 <= index_to_remove <= len(self.current_user.get_favorites()):
            movie_to_remove = self.current_user.get_favorites()[index_to_remove - 1]
            self.current_user.remove_favorite(movie_to_remove)
            print("Movie Successfully removed from your favorite list4.")
        else:
            print("Invalid index number. Please try again")

    def view_user_profile(self):
        print(self.current_user)
        print("Favorite Movies are:")
        for movie in self.current_user.get_favorites():
            print(movie)

    def search_favorites(self):
        if not self.current_user.get_favorites():
            print("No movies in your favorite list to search.")
            return
        keyword_for_favorites = input("Enter search keyword for favorites: ")
        result = []
        for movie in self.current_user.get_favorites():
            if keyword_for_favorites.lower() in movie.get_title().lower() or \
                    keyword_for_favorites.lower() in movie.get_cast().lower() or \
                    keyword_for_favorites.lower() in movie.get_category().lower():
                result.append(movie)
        print("Search result in favorite movies for '" + keyword_for_favorites + "':")
        for movie in result:
            print(movie)
