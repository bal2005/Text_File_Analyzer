# Text File Analyzer

This is a Flask-based web application that allows users to upload text files and analyze their content. The application provides various text analysis features, including basic text statistics, readability scores, keyword frequency, most common words, and sentiment analysis.

## Features

- Basic text analysis (character count, word count, sentence count)
- Readability scores (Flesch-Kincaid, Gunning Fog)
- Keyword frequency analysis
- Most common words analysis
- Sentiment analysis (polarity, subjectivity)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/text-file-analyzer.git
   cd text-file-analyzer
   ```

2. Create a virtual environment and activate it:

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Download NLTK data:
   ```sh
   python -m nltk.downloader punkt
   ```

## Usage

1. Run the Flask application:

   ```sh
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Upload a text file and optionally enter keywords for frequency analysis.

4. View the analysis results on the results page.

## Dependencies

- Flask
- NLTK
- TextBlob
- TextStat

## License

This project is licensed under the MIT License. See the LICENSE file for details.
