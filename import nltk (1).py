import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

def process_text(file_path, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for token in stemmed_tokens:
            output_file.write(token + '\n')

input_file_path = 'example.txt'
output_file_path = 'processed_text.txt'

process_text(input_file_path, output_file_path)
print(f"Processed text written to {output_file_path}")
