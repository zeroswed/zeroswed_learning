fav_movies = ['batman','monkey','superman']

for movie in fav_movies[:]:
        print(movie.capitalize())
        if movie == 'monkey':
            fav_movies.remove(movie)
print("\nUpdated favorite movies list:")
for movie in fav_movies:
    print(movie.capitalize())    
    
for movie in fav_movies:
    if "He-man" not in fav_movies:
        fav_movies.append("He-man")
print("\nFinal favorite movies list:")
for movie in fav_movies:
    print(movie.capitalize())

numbers = [1, 2, 3, 4, 5]
list = ("apple", "banana", "cherry")
numbers.extend(list)
print(numbers)