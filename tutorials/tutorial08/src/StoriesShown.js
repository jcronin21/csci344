import React, { useEffect, useState } from 'react';
import { getHeaders } from './utils';

export default function StoriesShown({token}) {  
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
    if (!stories) {
        return '';
    }
    return (
        stories.map(story => {
            return (
                <Story model={story} key={'story-' + story.id} token ={token} />
            )
        })
    );     
}

function Story({model}){
    return <div>{model.text}</div>;
}