import React, { useEffect, useState } from 'react';

export default function Profile({profile}) {
    // some logic here:
   const[profile, setProfile] = useState(null);
   console.log("Profile!!");
   useEffect(()=>{
    async function fetchProfile(){
        const response = await fetch('/api/profile',{
            headers:getHeaders(token)
        });
        const data = await response.json();
        setProfile(data)

    }
    fetchProfile();
},[token]);
if (!profile) {
    return '';
}
   
 
    
    


    // return some JSX
    // if (!profile) {
    //     return <div>''</div>;
    // }
    
    return (
        <header>
            <img src={profile.thumb_url} alt= "Profile thumbnail" />
            <h3>{profile.username}</h3>
        
        </header>
    )
}
