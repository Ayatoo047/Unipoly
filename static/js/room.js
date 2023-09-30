scrollToConversationBottom()
let roomName = document.getElementById('room_name').innerText
// let username = username
let username = document.getElementById('username').innerText
const threadScroll = document.getElementById('threadscroll')
const theMessage = document.getElementsByClassName('thread__details')
 // Get the input element and the form
 const textinput = document.getElementById('textinput');
 const textForm = document.getElementById('textform');
 const inputValue = textinput;
 let ourdata = {}
 let user_id = '';

 function slugify(text) {
  return text
      .toString() // Ensure the input is a string
      .toLowerCase() // Convert to lowercase
      .trim() // Remove leading and trailing whitespace
      .replace(/\s+/g, '-') // Replace spaces with dashes
      .replace(/[^\w-]+/g, '') // Remove non-word characters except dashes
      .replace(/--+/g, '-'); // Replace consecutive dashes with a single dash
}

// Example usage:
const inputText = roomName;
const slug = slugify(inputText);
// console.log(slug);

//  console.log(roomName)
 const socket = new WebSocket(`ws://${window.location.host}/ws/chat/${slug}/`)

 textForm.addEventListener('submit', (event) => {
  // if (socket.CLOSED){
  //   socket = new WebSocket(`ws://${window.location.host}/ws/chat/${slug}/`)
  // }
    // console.log('message')
    event.preventDefault()
    const textInput = textinput.value
    socket.send(JSON.stringify({
        'message': textInput,
        'sender': username
      }));
    // console.log(message,sender)
 })

 function scrollToConversationBottom() {
    const conversationDiv = document.getElementById('threadscroll');
    conversationDiv.scrollTop = conversationDiv.scrollHeight - 5;
}

 function appendThreadToThreadscroll(username, messageText, imageUrl) {
    console.log('working on it')
    // Create a new thread element
    const newThread = document.createElement('div');
    newThread.classList.add('thread');

    // Create the thread__top section
    const threadTop = document.createElement('div');
    threadTop.classList.add('thread__top');

    // Create the thread__author section
    const threadAuthor = document.createElement('div');
    threadAuthor.classList.add('thread__author');

    // Create a link to the user profile
    const userLink = document.createElement('a');
    userLink.href = username; // You can replace 'username' with the actual URL
    userLink.classList.add('thread__authorInfo');

    // Create the avatar
    const avatar = document.createElement('div');
    avatar.classList.add('avatar', 'avatar--small');
    const avatarImg = document.createElement('img');
    avatarImg.src = imageUrl; // You can replace 'imageUrl' with the actual image URL
    avatar.appendChild(avatarImg);

    // Create the username span
    const usernameSpan = document.createElement('span');
    usernameSpan.textContent = username; // You can replace 'username' with the actual username

    // Append avatar and username to userLink
    userLink.appendChild(avatar);
    userLink.appendChild(usernameSpan);

    // Create the thread__date span
    const dateSpan = document.createElement('span');
    dateSpan.classList.add('thread__date');
    // You can set the date content here

    // Append userLink and dateSpan to threadAuthor
    threadAuthor.appendChild(userLink);
    threadAuthor.appendChild(dateSpan);

    // Create the thread__delete link
    const deleteLink = document.createElement('a');
    deleteLink.href = 'delete-link-url'; // You can replace with the actual delete link URL
    deleteLink.classList.add('thread__delete');

    // Create the delete icon (SVG)
    const deleteIcon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    deleteIcon.setAttribute('version', '1.1');
    deleteIcon.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    deleteIcon.setAttribute('width', '32');
    deleteIcon.setAttribute('height', '32');
    deleteIcon.setAttribute('viewBox', '0 0 32 32');

    // Create the title for the delete icon
    const deleteTitle = document.createElement('title');
    deleteTitle.textContent = 'remove';

    // Create the path for the delete icon
    const deletePath = document.createElement('path');
    deletePath.setAttribute('d', 'M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z');

    // Append title and path to deleteIcon
    deleteIcon.appendChild(deleteTitle);
    deleteIcon.appendChild(deletePath);

    // Append deleteIcon to deleteLink
    deleteLink.appendChild(deleteIcon);

    // Create the thread__details div
    const threadDetails = document.createElement('div');
    threadDetails.classList.add('thread__details');
    threadDetails.textContent = messageText; // You can replace 'messageText' with the actual message content

    // Append threadAuthor, deleteLink, and threadDetails to threadTop
    threadTop.appendChild(threadAuthor);
    threadTop.appendChild(deleteLink);

    // Append threadTop and threadDetails to the newThread
    newThread.appendChild(threadTop);
    newThread.appendChild(threadDetails);

    // Append the newThread to the 'threadscroll' div
    const threadscrollDiv = document.getElementById('threadscroll');
    console.log('alomst')
    threadscrollDiv.appendChild(newThread);
    scrollToConversationBottom()
}


//  // Add a keydown event listener to the input element
//  textform.addEventListener('keydown', function (event) {
//    // Check if the Enter key (key code 13) is pressed
//    if (event.key === 13) {
//      // Prevent the default form submission
//     //  event.preventDefault();
//      console.log('entered')

//      // Get the input value
//      const inputValue = textinput.value;

//      // Do something with the input value (e.g., display it, send it to the server)
//      console.log('Input Value:', inputValue);

//      // You can also reset the input field if needed
//      textInput.value = '';
//    }
//  });
 
// const socket = new WebSocket(`ws://${window.location.host}/ws/chat/yy/`)
// socket.onopen = (function(e) {
//     socket.send(JSON.stringify({
//     'message': textinput,
//     'sender': username
//   }));})

socket.onmessage = function(e) {
    // console.log('Server: ' + e.data);
    const {sender, message, create, user_url} = JSON.parse(e.data)
    // appendThreadToThreadscroll(sender, message, 'https://randomuser.me/api/portraits/men/37.jpg');
    // console.log(message)


    // async function fetchData() {
    //     const url = `/lastmessage/${roomName}`; // Replace with your API URL
      
    //     try {
    //       const response = await fetch(url, {
    //         method: 'GET', // Using the GET method
    //         headers: {
    //           'Content-Type': 'application/json', // Set the content type based on your API requirements
    //           // You can add other headers if needed
    //         },
    //       });
      
    //       if (!response.ok) {
    //         throw new Error('Network response was not ok');
    //       }
      
    //       const data = await response.json()
    //       .then(data =>
    //         {
    //           // return data;
    //           user_id = data.user_id;
    //          let created = data.created
    //           console.log(user_id);

            if(username == sender){
              threadScroll.innerHTML += ` <div class="thread">
              <div class="thread__top">
                <div class="thread__author">
                  <a href="${user_url}" class="thread__authorInfo">
                    <div class="avatar avatar--small">
                      <img src="https://randomuser.me/api/portraits/men/37.jpg" />
                    </div>
                    <span>@${sender}</span>
                  </a>
                  <span class="thread__date">${create}</span>
                </div>
                
                <a href="{% url 'deletemessage' message.id %}">
                <div class="thread__delete">
                  <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                    <title>remove</title>
                    <path
                      d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"
                    ></path>
                  </svg>
                </div>
                </a>
          
              </div>
              <div class="thread__details">
                ${message}
              </div>
            </div>`
            }
            else{
              threadScroll.innerHTML += ` <div class="thread">
              <div class="thread__top">
                <div class="thread__author">
                  <a href="/user-profile/${user_id}" class="thread__authorInfo">
                    <div class="avatar avatar--small">
                      <img src="https://randomuser.me/api/portraits/men/37.jpg" />
                    </div>
                    <span>@${sender}</span>
                  </a>
                  <span class="thread__date">${created}</span>
                </div>
              </div>
              <div class="thread__details">
                ${message}
              </div>
            </div>`
            }
            scrollToConversationBottom()
            textinput.value = ''
        }
      //     );
      //     // Handle the response data here
      //     // console.log(data);
      //     // user_id = data.user_id;
      //     // created = data.created;
      //   } catch (error) {
      //     // Handle any errors that occurred during the fetch
      //     console.error('There was a problem with the fetch operation:', error);
      //   }
      // }
      // fetchData()
      // console.log(user_id)
      // function data() {fetchData().then(data => {
      //   ourdata = fetchData()
      //   // return data
      // })}
      // data()
      // console.log(ourdata)
  //   threadScroll.innerHTML += ` <div class="thread">
  //   <div class="thread__top">
  //     <div class="thread__author">
  //       <a href="/user-profile/${fetchData.user_id}" class="thread__authorInfo">
  //         <div class="avatar avatar--small">
  //           <img src="https://randomuser.me/api/portraits/men/37.jpg" />
  //         </div>
  //         <span>@${sender}</span>
  //       </a>
  //       <span class="thread__date">${fetchData.created}</span>
  //     </div>
      
  //     {% if request.user == message.user %}
  //     <a href="{% url 'deletemessage' message.id %}">
  //     <div class="thread__delete">
  //       <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
  //         <title>remove</title>
  //         <path
  //           d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"
  //         ></path>
  //       </svg>
  //     </div>
  //     </a>
  //     {%endif%}

  //   </div>
  //   <div class="thread__details">
  //     ${message}
  //   </div>
  // </div>`

  // console.log('done')
    // $(document).ready(function() {
    //   // Get the number of li tags in the ul tag with id 'transaction'
    //   var liCount = $("#transaction li").length;
    
    //   // If the li tags are more than 10, only show the last 10
    //   if (liCount > 10) {
    //     $("#transaction li:lt(10)").show();
    //     $("#transaction li:gt(9)").hide();
    //   }
    // });
//     checker()
//     updatedrawChart()

// };

// const executeCode = () => {
//     console.log('clicked');
//     socket.send(JSON.stringify({
//       'message': generateRandomNumber(),
//       'sender': username
//     }));
//   };