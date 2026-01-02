# 📚 Personalized Book Recommender System

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green)
![Gradio](https://img.shields.io/badge/Gradio-Web%20App-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A semantic book recommendation system powered by Large Language Models (LLMs). This project uses vector search, zero-shot classification, and sentiment analysis to provide personalized book suggestions based on natural language queries.

## ✨ Features

- **Semantic Search**: Find books using natural language queries (e.g., "a book about a person seeking revenge")
- **Genre Classification**: Zero-shot LLM classification to categorize books as fiction or non-fiction
- **Emotion Analysis**: Sentiment analysis to sort books by tone (suspenseful, joyful, sad, etc.)
- **Interactive Web App**: User-friendly Gradio interface for getting recommendations

## 🏗️ Project Structure

```
Book Recommender/
├── data-exploration.ipynb     # Text data cleaning and preprocessing
├── vector-search.ipynb        # Semantic search & vector database setup
├── text-classification.ipynb  # Zero-shot genre classification
├── sentiment-analysis.ipynb   # Emotion extraction from book descriptions
├── gradio-dashboard.py        # Web application for recommendations
├── requirements.txt           # Project dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/personalized-book-suggestions.git
   cd personalized-book-suggestions
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Add your API keys to the .env file
   ```

## 📖 Usage

### Running the Notebooks

Execute the notebooks in order to build the recommendation system:

1. `data-exploration.ipynb` - Clean and prepare the book data
2. `vector-search.ipynb` - Build the vector database for semantic search
3. `text-classification.ipynb` - Classify books by genre
4. `sentiment-analysis.ipynb` - Analyze book emotions and tone

### Launching the Web App

```bash
python gradio-dashboard.py
```

Then open your browser and navigate to `http://localhost:7860`

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Data Processing** | Pandas, Matplotlib, Seaborn |
| **ML/AI** | LangChain, Transformers, ChromaDB |
| **Vector Search** | LangChain-Chroma, OpenCV embeddings |
| **Web Interface** | Gradio |
| **Data Source** | Kaggle Hub |

## 📦 Dependencies

- [kagglehub](https://pypi.org/project/kagglehub/) - Dataset access
- [pandas](https://pypi.org/project/pandas/) - Data manipulation
- [matplotlib](https://pypi.org/project/matplotlib/) & [seaborn](https://pypi.org/project/seaborn/) - Visualization
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment management
- [langchain-community](https://pypi.org/project/langchain-community/) - LLM integrations
- [langchain-chroma](https://pypi.org/project/langchain-chroma/) - Vector database
- [transformers](https://pypi.org/project/transformers/) - ML models
- [gradio](https://pypi.org/project/gradio/) - Web interface

## 🎓 Acknowledgments

This project was created following the freeCodeCamp course: **"Build a Semantic Book Recommender with LLMs – Full Course"**

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ for book lovers
</p>



