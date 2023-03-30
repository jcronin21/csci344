import React, { useEffect, useState } from 'react';

export default function Stories({token}) {  
  const [stories, setStories] = useState(null);
 
  useEffect(() => {
      async function fetchStories() {
          const response = await fetch('/api/stories', {
              headers: getHeaders(token)
          });
          const data = await response.json();
          setStories(data)
      }
      fetchStories();

  }, [token]);  
 
  // return some HTML:
  if (!stories) {
      return '';
  }
  return (
      stories.map(story => {
          return (
              <Story model={story} key={'story-' + story.id} />
          )
      })
  );    
}