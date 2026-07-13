import { useEffect, useState } from "react";
import { fetchMeta, getRecommendations } from "./api";
import "./App.css";

function App() {
  const [categories, setCategories] = useState(["All"]);
  const [tones, setTones] = useState(["All"]);
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("All");
  const [tone, setTone] = useState("All");
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchMeta()
      .then((meta) => {
        setCategories(meta.categories);
        setTones(meta.tones);
      })
      .catch(() => setError("Could not reach the backend."));
  }, []);

  async function handleSubmit(e) {
    e.preventDefault();
    if (!query.trim()) return;
    setLoading(true);
    setError(null);
    try {
      const results = await getRecommendations({ query, category, tone });
      setBooks(results);
    } catch {
      setError("Something went wrong fetching recommendations.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <h1>Semantic book recommender</h1>

      <form onSubmit={handleSubmit} className="search-row">
        <input
          type="text"
          placeholder="e.g., A story about forgiveness"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <select value={category} onChange={(e) => setCategory(e.target.value)}>
          {categories.map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>
        <select value={tone} onChange={(e) => setTone(e.target.value)}>
          {tones.map((t) => (
            <option key={t} value={t}>{t}</option>
          ))}
        </select>
        <button type="submit" disabled={loading}>
          {loading ? "Searching..." : "Find recommendations"}
        </button>
      </form>

      {error && <p className="error">{error}</p>}

      <h2>Recommendations</h2>
      <div className="gallery">
        {books.map((book) => (
          <div className="book-card" key={book.isbn13}>
            <img
              src={book.thumbnail}
              alt={book.title}
              onError={(e) => { e.target.src = "/cover-not-found.jpg"; }}
            />
            <p className="caption">
              <strong>{book.title}</strong> by {book.authors}: {book.description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;