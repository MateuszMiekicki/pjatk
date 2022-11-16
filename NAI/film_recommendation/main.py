import json
import numpy as np

def euclidean_score(dataset, user1, user2):
    '''
     Function checking similarity of users movies using euclidean distance
    :param dataset: json
    :type dataset:
    :param user1: first user
    :type user1:
    :param user2: second user to compare
    :type user2:
    :return: euclidean distance
    '''
    if user1 not in dataset:
        raise TypeError('Cannot find ' + user1 + ' in the dataset')

    if user2 not in dataset:
        raise TypeError('Cannot find ' + user2 + ' in the dataset')

    common_movies = {}
    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1

    if len(common_movies) == 0:
        return 0

    squared_diff = []

    for item in dataset[user1]:
        if item in dataset[user2]:
            squared_diff.append(
                np.square(dataset[user1][item] - dataset[user2][item]))

    return 1 / (1 + np.sqrt(np.sum(squared_diff)))


def pearson_score(dataset, user1, user2):
    '''
    Function checking similarity of users movies using pearson correlation
    :param dataset: data in json file
    :type dataset:
    :param user1: first user
    :type user1:
    :param user2: second user to compare
    :type user2:
    :return: pearson correlation
    '''
    if user1 not in dataset:
        raise TypeError('Cannot find ' + user1 + ' in the dataset')

    if user2 not in dataset:
        raise TypeError('Cannot find ' + user2 + ' in the dataset')

    common_movies = {}
    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1

    num_ratings = len(common_movies)
    if num_ratings == 0:
        return 0
    user1_sum = np.sum([dataset[user1][item] for item in common_movies])
    user2_sum = np.sum([dataset[user2][item] for item in common_movies])

    user1_squared_sum = np.sum(
        [np.square(dataset[user1][item]) for item in common_movies])
    user2_squared_sum = np.sum(
        [np.square(dataset[user2][item]) for item in common_movies])

    sum_of_products = np.sum(
        [dataset[user1][item] * dataset[user2][item] for item in common_movies])

    Sxy = sum_of_products - (user1_sum * user2_sum / num_ratings)
    Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
    Syy = user2_squared_sum - np.square(user2_sum) / num_ratings

    if Sxx * Syy == 0:
        return 0

    return Sxy / np.sqrt(Sxx * Syy)


class RecommendationSystem:
    def __init__(self, data, user):
        self.users_and_scores = {}
        self.most_compatible_users = []
        self.data = data
        self.user = user

    def get_nearest_user(self, user_to_compare):
        '''
        Function getting the most similar user to compared one.
        :param user_to_compare:
        :type user_to_compare:
        :return: nearest_user
        '''
        user_list = list(self.data.keys())
        user_list.remove(user_to_compare)
        highest_score = 0
        for u in user_list:
            score = euclidean_score(data, user_to_compare, u)
            # pearson_score(data, user_to_compare, u) 
            self.users_and_scores[u] = score
            if score >= highest_score:
                highest_score = score
                nearest_user = u
        return nearest_user

    def get_nearest_users_list(self, user_to_compare):
        '''
        Function getting list of most similar users to compared one.
        :param user_to_compare:
        :type user_to_compare:
        :return: nearest_users_list
        '''
        nearest = self.get_nearest_user(user_to_compare)
        sorted_nearest_users_dict = {k: v for k, v in sorted(
            self.users_and_scores.items(), key=lambda item: item[1])}
        for v in list(sorted_nearest_users_dict.values()):
            if v == 'orange':
                del sorted_nearest_users_dict[v]
        nearest_users_list = list(sorted_nearest_users_dict.keys())
        nearest_users_list.reverse()
        return nearest_users_list

    def get_common_movies(self, user_to_compare, nearest_user):
        '''
        Function getting movies common for compared users
        :param user_to_compare:
        :type user_to_compare:
        :param nearest_user:
        :type nearest_user:
        :return: common_movies
        '''
        common_movies = []
        i = 0
        for item in self.data[user_to_compare]:
            i += 1

            if item in self.data[nearest_user]:

                common_movies.append(item)
        return common_movies

    def recommended_movies(self):
        '''
        Function getting 5 movies worth to recommend
        :return: recommended_movies
        '''
        iterator = 0
        recommended_movies = []
        nearest_list = self.get_nearest_users_list(self.user)
        while len(recommended_movies) < 5:
            nearest = nearest_list[iterator]
            if nearest not in self.most_compatible_users:
                self.most_compatible_users.append(nearest)
            common = self.get_common_movies(self.user, nearest)
            for key, value in data[nearest].items():
                if key not in common and value > 8 and key not in recommended_movies:
                    recommended_movies.append(key)
            iterator += 1
        return recommended_movies[:5]

    def not_recommended_movies(self):
        '''
         Function getting 5 movies not worth to recommend
        :return: not_recommended_movies
        '''
        iterator = 0
        not_recomended_movies = []
        nearestList = self.get_nearest_users_list(self.user)
        while len(not_recomended_movies) < 5:
            nearest = nearestList[iterator]
            if nearest not in self.most_compatible_users:
                self.most_compatible_users.append(nearest)
            common = self.get_common_movies(self.user, nearest)
            for key, value in self.data[nearest].items():
                if key not in common and value < 3:
                    not_recomended_movies.append(key)
            iterator += 1
        return not_recomended_movies[:5]

    def get_most_compatible_users(self):
        '''
        Function getting most compatible users.
        :return:most_compatible_users
        '''
        return self.most_compatible_users

def toString(dataList):
    i = 1
    for item in dataList:
        print(i, ". ", item)
        i += 1


with open('ratings.json', 'r', encoding="utf-8") as f:
    data = json.loads(f.read())

# user = input(
#     "Podaj imie i nazwisko użytkownika, któremu chcesz rekomendować filmy:")
user ="Paweł Czapiewski"
while user not in data.keys():
    print("Użytkownika nie ma w naszej bazie, podaj jednego z:")
    for i in data.keys():
        print("", i, ", ", end="")
    # user = input()
    user ="Paweł Czapiewski"
rSystem = RecommendationSystem(data, user)

print("Filmy, które podobały się osobom, mającym zbliżony gust do wskazanego użytkownika: ")
toString(rSystem.recommended_movies())
print("Filmy, które nie podobały się osobom, mającym zbliżony gust do wskazanego użytkownika: ")
toString(rSystem.not_recommended_movies())
print("Osoby o podobnym guście do wskazanego użytkownika:")
toString(rSystem.get_most_compatible_users())
