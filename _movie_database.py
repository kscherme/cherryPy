class _movie_database:

    def __init__(self):
      self.movies = dict()
      self.users  = dict()
      self.ratings= dict()

    def load_movies(self, movie_file):
        self.movies.clear()
        myfile = open(movie_file, encoding= "latin-1")
        for line in myfile:
            lines = line.split("::")
            self.movies[int(lines[0])] = [lines[1], lines[2].rstrip()]

    def get_movie(self, mid):
        return self.movies.get(mid)

    def get_movies(self):
        id_list = []
        for key in self.movies:
            id_list.append(key)
        return id_list
    
    def set_movie(self, mid, mylist):
        self.movies[mid] = mylist

    def delete_movie(self, mid):
        self.movies.pop(mid, None)

    def load_users(self, users_file):
        self.users.clear()
        myfile = open(users_file)
        for line in myfile:
            lines = line.split("::")
            self.users[int(lines[0])] = [lines[1], int(lines[2]), int(lines[3]), lines[4].rstrip()]

    def get_user(self, uid):
        return self.users.get(uid)

    def get_users(self):
        id_list = []
        for key in self.users:
            id_list.append(key)
        return id_list

    def set_user(self, uid, mylist):
        self.users[uid] = mylist

    def delete_user(self, uid):
        self.users.pop(uid, None)

    def load_ratings(self, ratings_file):
        self.ratings.clear()
        myfile = open(ratings_file)
        for line in myfile:
            lines = line.split("::")
            self.set_user_movie_rating(int(lines[0]), int(lines[1]), int(lines[2]))
        

    def get_rating(self, mid):
        if mid in self.ratings:
            total = 0
            sum_ratings = 0
            for key, value in self.ratings[mid].items():
                sum_ratings += float(value)
                total += 1
            return float(sum_ratings/total)
        else:
            return 0

    def get_highest_rated_movie(self):
        if len(self.ratings) == 0:
            return None
        max_rating = 0.0
        max_rating_id = 10000
        for key, value in self.ratings.items():
            rating = self.get_rating(key)
            if rating > max_rating:
                max_rating = rating
                max_rating_id = key
            elif rating == max_rating and key < max_rating_id:
                max_rating_id = key
        return max_rating_id

    def set_user_movie_rating(self, uid, mid, rating):
        try:
            self.ratings[mid].update({uid: rating})
        except KeyError:
            self.ratings[mid] = {}
            self.ratings[mid].update({uid:rating})
    
    def get_user_movie_rating(self, uid, mid):
        return self.ratings[mid].get(uid)

    def delete_all_ratings(self):
        self.ratings.clear()

    def print_sorted_movies(self):
        #for movie in sorted(self.movies, key=str.lower):
            #print movie
        for key in sorted(self.movies):
            print (key)



if __name__ == "__main__":
       mdb = _movie_database()

       #### MOVIES ########
       mdb.load_movies('ml-1m/movies.dat')
       #mdb.print_sorted_movies()
       mdb.load_ratings('ml-1m/ratings.dat')
       print (mdb.get_rating(1))
       print (mdb.get_movie(1))
       
       #print mdb.get_rating(787)
