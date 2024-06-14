# guess we're assuming each row is a user's interests
from collections import Counter
from typing import List, Tuple

users_interests = [
    ["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"],
    ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
    ["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
    ["R", "Python", "statistics", "regression", "probability"],
    ["machine learning", "regression", "decision trees", "libsvm"],
    ["Python", "R", "Java", "C++", "Haskell", "programming languages"],
    ["statistics", "probability", "mathematics", "theory"],
    ["machine learning", "scikit-learn", "Mahout", "neural networks"],
    ["neural networks", "deep learning", "Big Data", "artificial intelligence"],
    ["Hadoop", "Java", "MapReduce", "Big Data"],
    ["statistics", "R", "statsmodels"],
    ["C++", "deep learning", "artificial intelligence", "probability"],
    ["pandas", "R", "Python"],
    ["databases", "HBase", "Postgres", "MySQL", "MongoDB"],
    ["libsvm", "regression", "support vector machines"],
]

# Count the number of users interested in each topic
popular_interests = Counter(
    [interest for user_interests in users_interests for interest in user_interests]
)
# print(popular_interests.most_common())

# Suggest most popular interests user is not already interested in


def most_popular_new_interests(
    user_interests: List[str], max_results: int = 5
) -> List[Tuple[str, int]]:
    return [
        (suggestion, frequency)
        for suggestion, frequency in popular_interests.most_common()
        if suggestion not in user_interests
    ][:max_results]


print(most_popular_new_interests(users_interests[0]))

unique_interests = sorted(
    {interest for user_interests in users_interests for interest in user_interests}
)

assert unique_interests[:6] == [
    "Big Data",
    "C++",
    "Cassandra",
    "HBase",
    "Hadoop",
    "Haskell",
]


def make_user_interest_vector(users_interests: List[str]) -> List[int]:
    return [1 if interest in users_interests else 0 for interest in unique_interests]


print(make_user_interest_vector(users_interests[0]))
