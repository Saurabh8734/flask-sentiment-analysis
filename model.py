from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample training data (for a quick start)
training_data = [
    ("I love this product", "positive"),
    ("This is an amazing experience", "positive"),
    ("I am not happy with this", "negative"),
    ("This is disappointing", "negative"),
    ("Such a great day!", "positive"),
    ("I hate this item", "negative"),
    ("I'm feeling fantastic", "positive"),
    ("This is awful", "negative")
]


# preparing data
texts, labels = zip(*training_data)
vectorizer =CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train a simple model
model = MultinomialNB()
model.fit(X, labels)


# Save model and vectorizer
with open("sentiment_model.pkl", "wb") as model_file:
    pickle.dump((vectorizer, model), model_file)