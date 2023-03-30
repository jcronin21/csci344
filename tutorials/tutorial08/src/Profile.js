import React from 'react';

export default function Profile({profile}) {
    // some logic here:
    console.log(profile);
 
    
    


    // return some JSX
    if (!profile) {
        return <div>loading</div>;
    }
    
    return (
        <header>
            <img src={profile.thumb_url} alt= "Profile thumbnail" />
            <h3>{profile.username}</h3>
        
        </header>
    )
}
