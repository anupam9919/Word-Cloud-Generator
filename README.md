# 🌟 Word Cloud Generator

A versatile Python application that creates beautiful word cloud visualizations from text data. This tool offers multiple input methods and advanced phrase analysis capabilities, making it perfect for text analysis, content visualization, and data exploration.

## ✨ Features

- **📝 Text Input Mode**: Generate word clouds directly from text entered via command line
- **📁 File Upload Mode**: Process text files to create visualizations
- **🔤 N-gram Analysis**: Create word clouds from multi-word phrases (bigrams, trigrams, etc.)
- **🎨 Interactive GUI**: User-friendly interface with themed styling for phrase selection
- **🧹 Smart Text Processing**: Automatic removal of stopwords and punctuation
- **💾 Export Capability**: Save generated word clouds as PNG images

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/anupam9919/word_cloud.git
   cd word_cloud
   ```

2. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK stopwords (required for text processing):**

   ```python
   python -c "import nltk; nltk.download('stopwords')"
   ```

## 📖 Usage

The project includes three different scripts for different use cases:

### 1. 📝 Text Input Mode (`input_as_text.py`)

Generate a word cloud from direct text input:

```bash
python input_as_text.py
```

- Enter your text when prompted
- The script will clean the text, remove stopwords, and display the word cloud
- Text is automatically saved to `input.txt`

### 2. 📁 File Upload Mode (`input_as_file_upload.py`)

Create a word cloud from a text file:

```bash
python input_as_file_upload.py
```

- A file dialog will open for you to select a `.txt` file
- The word cloud will be generated and displayed automatically

### 3. 🔤 Phrase Selection Mode (`input_phrase_select.py`)

Generate word clouds with n-gram analysis:

```bash
python input_phrase_select.py
```

- Select a text file when prompted
- Choose phrase length from the dropdown:
  - **Bigram (2)**: Pairs of consecutive words
  - **Trigram (3)**: Three consecutive words
  - **Four-gram (4)**: Four consecutive words
  - **Five-gram (5)**: Five consecutive words
- Click "Generate Word Cloud" to create the visualization

## 🛠️ Technical Details

### Text Processing Pipeline

1. **Input Acquisition**: Text from user input, file, or file dialog
2. **Cleaning**: Removal of punctuation and special characters
3. **Normalization**: Conversion to lowercase
4. **Filtering**: Removal of English stopwords using NLTK
5. **Frequency Analysis**: Word/phrase counting
6. **Visualization**: Word cloud generation using matplotlib

### Dependencies

- **wordcloud**: Core word cloud generation
- **matplotlib**: Visualization and display
- **nltk**: Natural language processing and stopwords
- **tkinter**: GUI components (included with Python)
- **ttkthemes**: Enhanced GUI styling

See `requirements.txt` for complete dependency list.

## 📂 Project Structure

```
word_cloud/
├── input_as_text.py           # CLI text input mode
├── input_as_file_upload.py    # File upload mode
├── input_phrase_select.py     # N-gram analysis with GUI
├── requirements.txt           # Python dependencies
├── sample.txt                 # Sample text file for testing
├── input.txt                  # Auto-generated from text input
├── README.md                  # This file
└── LICENSE                    # MIT License
```

## 🎯 Use Cases

- **Content Analysis**: Visualize key themes in documents, articles, or reports
- **Social Media Analytics**: Analyze trending topics from text data
- **Academic Research**: Identify frequent terms in research papers or surveys
- **Creative Projects**: Generate artistic word-based visualizations
- **SEO & Marketing**: Analyze keyword frequency in content

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [wordcloud](https://github.com/amueller/word_cloud) library
- Uses [NLTK](https://www.nltk.org/) for natural language processing
- Themed GUI powered by [ttkthemes](https://github.com/TkinterEP/ttkthemes)

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ for text visualization enthusiasts**
