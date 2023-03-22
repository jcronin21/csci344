import {getAccessToken} from './utilities.js';
const rootURL = 'https://photo-app-secured.herokuapp.com';

const showStories = async (token) => {
    const endpoint = `${rootURL}/api/stories`;
    const response = await fetch(endpoint, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
    })
    const data = await response.json();
    console.log('Stories:', data);
}

const showPosts = async (token) => {
    console.log('code to show posts');
}


const initPage = async () => {
    // first log in (we will build on this after Spring Break):
    const token = await getAccessToken(rootURL, 'webdev', 'password');

    // then use the access token provided to access data on the user's behalf
    showStories(token);
    showPosts(token);
}

initPage();


const likeButtons = document.querySelectorAll('.like-button');

likeButtons.forEach(button => {
  let likesCount = button.parentNode.querySelector('.likes');
  let currentLikes = parseInt(likesCount.textContent);

  button.addEventListener('click', () => {
    if (button.classList.contains('liked')) {
      currentLikes--;
      likesCount.textContent = `${currentLikes} likes`;
      button.classList.remove('liked');
    } else {
      currentLikes++;
      likesCount.textContent = `${currentLikes} likes`;
      button.classList.add('liked');
    }
  });
});


const bookmarkButtons = document.querySelectorAll('.bookmark-button');

bookmarkButtons.forEach(button => {
  button.addEventListener('click', () => {
    button.classList.toggle('filled');
  });
});


const suggestedAccounts = document.querySelectorAll('.suggested-account');

suggestedAccounts.forEach(account => {
  const followButton = account.querySelector('.follow-button');
  const suggestedUser = account.querySelector('.suggested-user');

  followButton.addEventListener('click', () => {
    if (followButton.classList.contains('following')) {
      followButton.textContent = 'Follow';
      followButton.classList.remove('following');
      console.log(`Unfollowed ${suggestedUser.textContent}.`);
    } else {
      followButton.textContent = 'Following';
      followButton.classList.add('following');
      console.log(`Followed ${suggestedUser.textContent}.`);
    }
  });
});



const commentButtons = document.querySelectorAll('.add-comment-button');

commentButtons.forEach(button => {
  button.addEventListener('click', () => {
    const section = button.parentNode;

    const form = document.createElement('form');

    form.innerHTML = `
      <input type="text" name="comment" placeholder="Add a comment">
      <button type="submit">Post</button>
    `;

    form.addEventListener('submit', (event) => {
      event.preventDefault();
      
      const commentInput = form.querySelector('input[name="comment"]');
      const commentText = commentInput.value;

      const comment = document.createElement('div');
      comment.classList.add('comment');
      comment.innerHTML = `${commentText}`;

      section.appendChild(comment);

      commentInput.value = '';
    });

    section.appendChild(form);
  });
});
