import nltk
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
nltk.download('punkt')
# Sample dataset with labeled examples
dataset = [
    ("I walk to the store", "present"),
    ("I walked to the store", "past"),
    ("I will walk to the store", "future"),
    ("I am walking to the store", "present_continuous"),
    ("I was walking to the store", "past_continuous"),
    ("I will be walking to the store", "future_continuous"),
]

# Function to extract features from sentences
def extract_features(sentence):
    words = nltk.word_tokenize(sentence.lower())
   # nltk.word_tokenize()
    return {word: True for word in words}

# Extracting features and labels
featuresets = [(extract_features(sentence), tense) for sentence, tense in dataset]

# Splitting data into train and test sets
train_set, test_set = train_test_split(featuresets, test_size=0.2, random_state=42)

# Training the classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Testing the classifier
predictions = [classifier.classify(features) for features, label in test_set]

true_labels = [label for features, label in test_set]

# Calculating accuracy
accuracy = accuracy_score(true_labels, predictions)
print("Accuracy:", accuracy)

# Example usage
#example_sentence = "I can go to the market"
#predicted_tense = classifier.classify(extract_features(example_sentence))
#print("Predicted tense for '{}' is '{}'".format(example_sentence, predicted_tense))

def predict_tense_by_given_text(input_text) :
    return classifier.classify(extract_features(input_text))

print(predict_tense_by_given_text("I will go to the market"))