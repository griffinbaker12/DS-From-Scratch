from collections import Counter, defaultdict

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendship_pairs = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]

friendships = {user["id"]: [] for user in users}


for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)


def number_of_friends(user):
    user_id = user["id"]
    return len(friendships[user_id])


total_connections = sum(number_of_friends(user) for user in users)

assert total_connections == 24

num_users = len(users)
avg_connections = total_connections / num_users

assert num_users == 10
assert avg_connections == 2.4

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id.sort(key=lambda friend_tuple: friend_tuple[1], reverse=True)


def foaf_ids_bad(user):
    return [
        foaf_id
        for friend_id in friendships[user["id"]]
        for foaf_id in friendships[friend_id]
    ]


print(foaf_ids_bad(users[0]))  # [0,2,3,0,1,3]
# Bad because it includes the users and the same users multiple times without counting
# Also returns users the person already knows


def friends_of_friends(user):
    return Counter(
        foaf_id
        for friend_id in friendships[user["id"]]
        for foaf_id in friendships[friend_id]
        if foaf_id != user["id"] and foaf_id not in friendships[user["id"]]
    )


print(friends_of_friends(users[3]))  # Counter({0: 2, 5: 1})

assert friends_of_friends(users[3]) == Counter({0: 2, 5: 1})

# And this could be based on the tags of the articles they read and how long they read them or something like that
interests = [
    (0, "Hadoop"),
    (0, "Big Data"),
    (0, "HBase"),
    (0, "Java"),
    (0, "Spark"),
    (0, "Storm"),
    (0, "Cassandra"),
    (1, "NoSQL"),
    (1, "MongoDB"),
    (1, "Cassandra"),
    (1, "HBase"),
    (1, "Postgres"),
    (2, "Python"),
    (2, "scikit-learn"),
    (2, "scipy"),
    (2, "numpy"),
    (2, "statsmodels"),
    (2, "pandas"),
    (3, "R"),
    (3, "Python"),
    (3, "statistics"),
    (3, "regression"),
    (3, "probability"),
    (4, "machine learning"),
    (4, "regression"),
    (4, "decision trees"),
    (4, "libsvm"),
    (5, "Python"),
    (5, "R"),
    (5, "Java"),
    (5, "C++"),
    (5, "Haskell"),
    (5, "programming languages"),
    (6, "statistics"),
    (6, "probability"),
    (6, "mathematics"),
    (6, "theory"),
    (7, "machine learning"),
    (7, "scikit-learn"),
    (7, "Mahout"),
    (7, "neural networks"),
    (8, "neural networks"),
    (8, "deep learning"),
    (8, "Big Data"),
    (8, "artificial intelligence"),
    (9, "Hadoop"),
    (9, "Java"),
    (9, "MapReduce"),
    (9, "Big Data"),
]

# function name with parameters should read like english


def data_scientists_who_like(target_interest):
    return [user_id for user_id, interest in interests if interest == target_interest]


# If we are needing to search a lot, then going through a list will not be very efficient
# Can make use of defaultdict to speed this up
user_ids_by_interest = defaultdict(list)
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    interests_by_user_id[user_id].append(interest)


# Can be used to build a richer feature based on combination of mutual friends and mutual interests
def most_common_interests_with(user):
    return [
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    ]


salaries_and_tenures = [
    (83000, 8.7),
    (88000, 8.1),
    (48000, 0.7),
    (76000, 6),
    (69000, 6.5),
    (76000, 7.5),
    (60000, 2.5),
    (83000, 10),
    (48000, 1.9),
    (63000, 4.2),
]

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print(average_salary_by_tenure)

assert average_salary_by_tenure == {
    0.7: 48000.0,
    1.9: 48000.0,
    2.5: 60000.0,
    4.2: 63000.0,
    6: 76000.0,
    6.5: 69000.0,
    7.5: 76000.0,
    8.1: 88000.0,
    8.7: 83000.0,
    10: 83000.0,
}


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    return "more than five"


salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure_bucket[tenure_bucket(tenure)].append(salary)

average_salary_by_bucket = {
    bucket: sum(salaries) / len(salaries)
    for bucket, salaries in salary_by_tenure_bucket.items()
}

# What we would really like to do is see how much a unit of tenure earns you in salary
assert average_salary_by_bucket == {
    "between two and five": 61500.0,
    "less than two": 48000.0,
    "more than five": 79166.66666666667,
}
