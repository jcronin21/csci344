import React, { useEffect, useState } from 'react';
import Suggestion from './Suggestion';

export default function Suggestions() {
  const [suggestions, setSuggestions] = useState([]);

  useEffect(() => {
    fetch('/api/suggestions')
      .then((response) => response.json())
      .then((data) => setSuggestions(data));
  }, []);

    // return some JSX
    return (
        <div className="suggestions">
          <h2>Suggestions</h2>
          <div>
            {suggestions.map((suggestion) => (
              <Suggestion key={suggestion.id} suggestion={suggestion} />
            ))}
          </div>
        </div>
      );
    }