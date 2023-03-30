import React, { useEffect, useState } from 'react';
import { getHeaders } from './utils';

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
// return the stories:
return (
  stories.map(stories => {
    return (
        <Stories model={stories} key={'stories-' + stories.id} />
    )
    }))}
