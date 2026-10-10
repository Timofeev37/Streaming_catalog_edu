import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson",
                                                    "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def main():
    print("Hello from streaming-catalog-edu!")


def average_rating(movies):
    sum_rating = 0
    for movie in movies:
        sum_rating += movie["rating"]
    average_rating = round(sum_rating / len(movies),1)
    return average_rating

def catalog_age_stats(movies, current_year=2026):
    years_sum = 0
    year_max = movies[0]["year"]
    year_min = movies[0]["year"]
    for movie in movies:
        if movie["year"] <= year_min:
            year_min = movie["year"]
        elif movie["year"] >= year_max:
            year_max = movie["year"]
        years_sum += current_year - movie["year"]
    years_avg = math.ceil(years_sum / len(movies))

    return (current_year - year_max, current_year - year_min, years_avg)

def duration_in_hours(minutes):
    hours = minutes // 60
    remainder = minutes % 60

    return f'{hours}ч {remainder}м'

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating>5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 < year < 2021:
            return "недавние"
        case _:
            return "старые"



# print(average_rating(movies))
# print(catalog_age_stats(movies))
# print(duration_in_hours(movies[0]["duration_min"]))
# print(rating_tier(6))
# print(decade_label(2018))

# for movie in movies:
#     if "comedy" not in movie["genres"]:
#         print(movie["title"])

# i = 0
# while i < len(movies):
#     i += 1
#     if movies[i]["rating"] > 9:
#         print(movies[i]["title"])
#         break
#     if i == len(movies)-1:
#         print("Шедевров не найдено")
#         break

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

# print(count_long_movies(movies))


def normalize_title(title):
    words = title.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    return " ".join(capitalized_words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    length = duration_in_hours(movie["duration_min"])
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f'{length}, жанры: {genres}'
    )

# print(normalize_title(movies[2]["title"]))

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            films = filmography.get(actor, [])
            films.append(movie["title"])
            filmography[actor] = films
    return filmography



# avg = average_rating(movies)
# print ({movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avg})

# print(actor_filmography(movies))
# print(count_by_genre(movies))

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])

    return genres

def common_actors(movie1, movie2):
    movie1_actors = set(actors for actors in movie1["actors"])
    movie2_actors = set(actors for actors in movie2["actors"])
    common_actors = movie1_actors&movie2_actors
    return common_actors

def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    genres_b = set()
    for movie in movies_a:
        genres_a.update(movie["genres"])
    for movie in movies_b:
        genres_b.update(movie["genres"])

    only_in_movie_a_genres = genres_a - genres_b

    return only_in_movie_a_genres

# print(genres_only_in_one(movies[0:2], movies[5:6]))
#
# print(all_genres(movies))
#
# print(common_actors(movies[0], movies[3]))


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


# for movie in iter_high_rated(movies):
#     print(format_report_line(movie))

# print(sum(movie["duration_min"] for movie in movies if movie["rating"] > 7))

def build_report(movies):
    print('ОТЧЕТ ПО КАТАЛОГУ')
    print('Средний рейтинг: ',average_rating(movies))
    print('Средний возраст фильмов: ', catalog_age_stats(movies)[2])
    print()
    print('ТОП-3 фильма:')
    top = top_n_by_rating(movies)
    for movie in top:
            for flick in movies:
                if flick["title"] == movie[0]:

                    print(format_report_line(flick))
    print('')
    print('Фильмов по жанрам:')
    genres_calc = {}
    for genre in all_genres(movies):
        for movie in movies:
            if genre in movie["genres"]:
                genres_calc[genre] = genres_calc.get(genre, 0) + 1
    genres_top = sorted(genres_calc.items(), key=lambda item: item[1], reverse=True)
    for genre in genres_top:
        print(f'    {genre[0]} - {genre[1]}')
    print('')
    print('Все жанры каталога:', ", ".join(list(all_genres(movies))))


if __name__ == "__main__":
    main()
    build_report(movies)