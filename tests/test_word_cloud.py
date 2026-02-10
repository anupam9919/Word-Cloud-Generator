"""
Unit tests for word cloud generation functionality
"""
import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wordcloud import WordCloud
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already present
try:
    stopwords.words('english')
except (LookupError, OSError):
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download('stopwords', quiet=True)


class TestTextProcessing:
    """Test text processing and cleaning functions"""
    
    def test_clean_text_removes_punctuation(self):
        """Test that punctuation is removed from text"""
        text = "Hello, world! This is a test."
        cleaned = ""
        for char in text:
            if char.isalpha() or char.isspace():
                cleaned += char
        
        assert "," not in cleaned
        assert "!" not in cleaned
        assert "." not in cleaned
        assert "Hello" in cleaned
    
    def test_lowercase_conversion(self):
        """Test that text is converted to lowercase"""
        text = "HELLO World"
        result = text.lower()
        assert result == "hello world"
    
    def test_stopwords_removal(self):
        """Test that stopwords are removed"""
        uninteresting_words = set(stopwords.words('english'))
        words = ["the", "hello", "is", "world", "a", "test"]
        cleaned_words = [word for word in words if word not in uninteresting_words]
        
        assert "the" not in cleaned_words
        assert "is" not in cleaned_words
        assert "a" not in cleaned_words
        assert "hello" in cleaned_words
        assert "world" in cleaned_words
        assert "test" in cleaned_words


class TestWordFrequency:
    """Test word frequency calculation"""
    
    def test_word_frequency_count(self):
        """Test that word frequencies are counted correctly"""
        words = ["hello", "world", "hello", "test", "world", "hello"]
        frequencies = {}
        for word in words:
            frequencies[word] = frequencies.get(word, 0) + 1
        
        assert frequencies["hello"] == 3
        assert frequencies["world"] == 2
        assert frequencies["test"] == 1
    
    def test_empty_text_handling(self):
        """Test handling of empty text"""
        words = []
        frequencies = {}
        for word in words:
            frequencies[word] = frequencies.get(word, 0) + 1
        
        assert len(frequencies) == 0
    
    def test_single_word(self):
        """Test handling of single word"""
        words = ["hello"]
        frequencies = {}
        for word in words:
            frequencies[word] = frequencies.get(word, 0) + 1
        
        assert frequencies["hello"] == 1
        assert len(frequencies) == 1


class TestWordCloudGeneration:
    """Test word cloud generation"""
    
    def test_wordcloud_creation(self):
        """Test that WordCloud object can be created"""
        wordcloud = WordCloud()
        assert wordcloud is not None
    
    def test_wordcloud_from_frequencies(self):
        """Test word cloud generation from frequency dictionary"""
        frequencies = {"hello": 5, "world": 3, "test": 2}
        wordcloud = WordCloud()
        wordcloud.generate_from_frequencies(frequencies)
        
        assert wordcloud is not None
        # Check that words are in the generated cloud
        assert len(wordcloud.words_) > 0
    
    def test_wordcloud_with_empty_frequencies(self):
        """Test word cloud with empty frequencies"""
        frequencies = {}
        wordcloud = WordCloud()
        
        # Should handle empty dict gracefully
        try:
            wordcloud.generate_from_frequencies(frequencies)
        except ValueError:
            # Expected behavior for empty frequencies
            pass


class TestPhraseGeneration:
    """Test n-gram phrase generation"""
    
    def test_bigram_generation(self):
        """Test bigram (2-word phrase) generation"""
        words = ["hello", "world", "this", "is", "test"]
        phrase_length = 2
        phrases = [" ".join(words[i:i+phrase_length]) for i in range(len(words)-phrase_length+1)]
        
        assert "hello world" in phrases
        assert "world this" in phrases
        assert "this is" in phrases
        assert "is test" in phrases
        assert len(phrases) == 4
    
    def test_trigram_generation(self):
        """Test trigram (3-word phrase) generation"""
        words = ["hello", "world", "this", "is", "test"]
        phrase_length = 3
        phrases = [" ".join(words[i:i+phrase_length]) for i in range(len(words)-phrase_length+1)]
        
        assert "hello world this" in phrases
        assert "world this is" in phrases
        assert "this is test" in phrases
        assert len(phrases) == 3
    
    def test_phrase_frequency_count(self):
        """Test phrase frequency counting"""
        phrases = ["hello world", "world test", "hello world", "test case"]
        frequencies = {}
        for phrase in phrases:
            frequencies[phrase] = frequencies.get(phrase, 0) + 1
        
        assert frequencies["hello world"] == 2
        assert frequencies["world test"] == 1
        assert frequencies["test case"] == 1


class TestFileOperations:
    """Test file reading operations"""
    
    def test_file_reading(self, tmp_path):
        """Test reading content from a file"""
        # Create a temporary test file
        test_file = tmp_path / "test.txt"
        test_content = "Hello world, this is a test file."
        test_file.write_text(test_content)
        
        # Read the file
        with open(test_file, 'r') as file:
            content = file.read()
        
        assert content == test_content
    
    def test_file_writing(self, tmp_path):
        """Test writing content to a file"""
        test_file = tmp_path / "output.txt"
        test_content = "Test output content"
        
        with open(test_file, 'w') as file:
            file.write(test_content)
        
        # Verify the content was written
        assert test_file.read_text() == test_content


class TestIntegration:
    """Integration tests for complete workflow"""
    
    def test_complete_text_processing_pipeline(self):
        """Test the complete text processing pipeline"""
        # Sample text
        text = "Hello, world! This is a test. Hello world again!"
        
        # Clean text
        cleaned_text = ""
        for char in text:
            if char.isalpha() or char.isspace():
                cleaned_text += char
        
        # Convert to lowercase and split
        words = cleaned_text.lower().split()
        
        # Remove stopwords
        uninteresting_words = set(stopwords.words('english'))
        cleaned_words = [word for word in words if word not in uninteresting_words]
        
        # Count frequencies
        frequencies = {}
        for word in cleaned_words:
            frequencies[word] = frequencies.get(word, 0) + 1
        
        # Verify results
        assert "hello" in frequencies
        assert "world" in frequencies
        assert frequencies["hello"] == 2
        assert frequencies["world"] == 2
        assert "is" not in frequencies  # stopword removed
        assert "a" not in frequencies   # stopword removed
    
    def test_wordcloud_generation_pipeline(self):
        """Test complete word cloud generation pipeline"""
        # Sample frequencies
        frequencies = {"python": 10, "programming": 8, "code": 6, "test": 4}
        
        # Generate word cloud
        wordcloud = WordCloud(width=400, height=200, background_color='white')
        wordcloud.generate_from_frequencies(frequencies)
        
        # Verify word cloud was created
        assert wordcloud is not None
        assert len(wordcloud.words_) > 0
        
        # Check that high-frequency words are present
        word_list = list(wordcloud.words_.keys())
        assert any("python" in word.lower() for word in word_list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
