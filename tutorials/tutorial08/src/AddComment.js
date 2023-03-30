import React from 'react';
import {getHeaders} from './utils';
import { useState } from "react";

export default function AddComment({postId, requeryPost, token}) {  
    const [value, setValue] = useState('');


    function handleChange(ev) {
        setValue(ev.target.value)
    }
   
    async function handleSubmit(ev) {
        ev.preventDefault();
        const postData = {
            "post_id": postId,
            "text": value
        };
       
        const response = await fetch('/api/comments', {
                method: "POST",
                headers: getHeaders(token),
                body: JSON.stringify(postData)
            });
        await response.json();
        requeryPost();
        setValue('');
    }

    return (
        <form onSubmit={handleSubmit} className="add-comment">
            <div className="input-holder">
                <input className="comment-textbox"
                    aria-label="Add a comment"
                    autoFocus
                    placeholder="Add a comment..."
                    value={value}
                    onChange={handleChange} />
            </div>
            <button className="link">Post</button>
        </form>
    )
}