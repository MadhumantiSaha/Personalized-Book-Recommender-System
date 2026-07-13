# 📚 Personalized Book Recommender System

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-19.0-61DAFB?logo=react&logoColor=black)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A semantic book recommendation system powered by Large Language Models (LLMs). This project uses vector search, zero-shot classification, and sentiment analysis to provide personalized book suggestions based on natural language queries, accessible via a responsive React frontend dashboard and a FastAPI backend.

## ✨ Features

- **Semantic Search**: Find books using natural language queries (e.g., "a book about a person seeking revenge")
- **Genre Classification**: Zero-shot LLM classification to categorize books as fiction or non-fiction
- **Emotion Analysis**: Sentiment analysis to sort books by tone (suspenseful, joyful, sad, etc.)
- **Interactive Web App**: Modern dashboard built with React and powered by a FastAPI REST API

## 🏗️ Project Structure

```
Personalized-Book-Recommender-System/
├── Backend/                 # FastAPI Web Server
│   ├── app/                 # Application logic & routes
│   │   ├── main.py          # FastAPI server entry point
│   │   ├── recommender.py   # Vector search and recommendation logic
│   │   ├── schemas.py       # Pydantic schemas
│   │   └── utils.py         # Helper functions
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables (OpenAI API keys, etc.)
├── Frontend/                # React Dashboard (Vite)
│   ├── src/                 # React source code
│   │   ├── App.jsx          # Main dashboard view
│   │   └── main.jsx         # React application root
│   ├── package.json         # Node.js dependencies & scripts
│   └── vite.config.js       # Vite configuration
├── notebooks/               # Jupyter notebooks for data processing
│   ├── data-exploration.ipynb
│   ├── vector-search.ipynb
│   ├── text-classification.ipynb
│   └── sentiment-analysis.ipynb
├── .gitignore
├── requirements.txt         # Core project/notebook dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Node.js (v18 or higher) and npm/pnpm
- OpenAI API Key (configured in Backend environment variables)

---

### Backend Setup (FastAPI)

1. **Navigate to the Backend directory**
   ```bash
   cd Backend
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the `Backend` directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Start the FastAPI server**
   ```bash
   uvicorn app.main:app --reload
   ```
   The backend will run on [http://localhost:8000](http://localhost:8000). You can view the interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

---

### Frontend Setup (React & Vite)

1. **Navigate to the Frontend directory**
   ```bash
   cd Frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```
   The dashboard will run on [http://localhost:5173](http://localhost:5173).

---

## 📖 Usage

### Running the Notebooks

Before starting the web application, you can execute the notebooks in the `notebooks/` directory sequentially to understand or re-build the recommendation database:

1. `data-exploration.ipynb` - Clean and prepare the book data
2. `vector-search.ipynb` - Build the vector database for semantic search
3. `text-classification.ipynb` - Classify books by genre
4. `sentiment-analysis.ipynb` - Analyze book emotions and tone

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Frontend** | React, Vite, Axios, TailwindCSS/CSS |
| **Backend** | FastAPI, Uvicorn, Pydantic |
| **Data Processing** | Pandas, Numpy, Matplotlib, Seaborn |
| **ML/AI & Embeddings** | LangChain, Transformers, OpenAI, PyTorch |
| **Vector Search** | LangChain-Chroma, ChromaDB |

## 🎓 Acknowledgments

This project was created following the freeCodeCamp course: **"Build a Semantic Book Recommender with LLMs – Full Course"**

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ for book lovers
</p>
