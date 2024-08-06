import nltk
from nltk.stem import PorterStemmer
from collections import Counter
import pandas as pd

# Load NLTK stopwords
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('english'))

# Initialize Porter Stemmer
stemmer = PorterStemmer()

# Function to preprocess text
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())  # Convert text to lowercase
    # Remove stopwords and non-alphabetic tokens
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return tokens

# Function to find duplicate words in a list
def find_duplicates(words):
    word_count = {}
    duplicates = []
    for word in words:
        word_lower = word.lower()  # Convert word to lowercase
        if word_lower in word_count:
            word_count[word_lower] += 1
            if word_count[word_lower] == 2:
                duplicates.append(word_lower)  # Append only when count becomes 2 (first duplicate)
        else:
            word_count[word_lower] = 1
    return duplicates, word_count

# Load data from Excel
df = pd.read_excel('JiraProject.xlsx', sheet_name='IssueType Utility')

# Create lists to store results
projects = []
issue_types_all = []
issue_types_preprocessed_all = []
duplicates_all = []
word_counts_all = []

# Iterate through each project
for project in df['Project Name'].unique():
    project_data = df[df['Project Name'] == project]
    issue_types = project_data['IssueTypes Names'].str.split(',').sum()  # Split and flatten the IssueTypes
    issue_types_preprocessed = preprocess_text(' '.join(issue_types))  # Preprocess the text
    
    # Apply stemming
    stemmed_issue_types = [stemmer.stem(word) for word in issue_types_preprocessed]
    
    # Count occurrences of each word
    duplicates, word_count = find_duplicates(stemmed_issue_types)
    
    # Append results to lists
    projects.append(project)
    issue_types_all.append(issue_types)
    issue_types_preprocessed_all.append(issue_types_preprocessed)
    duplicates_all.append(duplicates)
    word_counts_all.append(word_count)

# Create DataFrame from results
output_df = pd.DataFrame({
    'Project Name': projects,
    'IssueTypes': issue_types_all,
    'IssueTypes Preprocessed': issue_types_preprocessed_all,
    'Duplicate IssueTypes': duplicates_all,
    'Word Counts': word_counts_all
})

# Save DataFrame to CSV
output_df.to_csv('output.csv', index=False)
