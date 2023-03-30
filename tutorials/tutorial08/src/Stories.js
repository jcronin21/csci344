import React, { useEffect, useState } from 'react';

export default function Stories() {
    // logic here
    const[stories, setStories] = useState([]);

    useEffect(()=>{
        fetch('/api/stories')
        .then(response => response.json())
        .then(data => setStories(data.stories))
    
    }, []);


    // return some JSX
    return (
        <div className="stories">
          {stories.map(story => (
            <div key={story.id} className="story">
              <img src={story.image} alt="Story thumbnail" />
              <div className="story-details">
                <h3>{story.title}</h3>
                <p>{story.content}</p>
              </div>
            </div>
          ))}
        </div>
      );
    }