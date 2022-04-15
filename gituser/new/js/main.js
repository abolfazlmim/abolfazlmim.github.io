const userName = document.querySelector('#userName');
const searchBtn = document.querySelector('#searchBtn');
const api_Url = "https://api.github.com/users/";
const imgProfile = document.querySelector('#img');


const name1 = document.querySelector('#name');
const bio1 = document.querySelector('#bio');
const username = document.querySelector('#username1');
const posts = document.querySelector('#posts');
const follower1 = document.querySelector('#follower');
const following1 = document.querySelector('#following');

let profileSection = document.getElementsByClassName("content")[1];
let error = document.getElementById("error");

searchBtn.addEventListener('click',function(){
    let userSearch = userName.value;
    if (!userSearch) {
        profileSection.style.visibility = "hidden";
        error.className = "show";
        error.innerHTML='please enter username :D';
        setTimeout(function(){ error.className = error.className.replace("show", ""); }, 3000);
            return;
        }
    fetch(api_Url+userSearch).then(function(response){
        if (response.ok) {
            profileSection.style.visibility = "visible";
            profileSection.style.opacity = 1;
            return response.json();       
        }
        if (!response.ok) { 
            profileSection.style.visibility = "hidden";
            if (response.status == 404){     
                error.className = "show";
                error.innerHTML='⁦ಠ_ಠ⁩ user not found';
                setTimeout(function(){ error.className = error.className.replace("show", ""); }, 3000);
                return;
            }
            return ; 
      }
     return response;
        
    }).then(function(data){
        render(data);
    })
    .catch(function(error){
        console.log(error)
    });

})

function render(data) {
    const { avatar_url,name,login,bio,public_repos,followers,following} = data;
    imgProfile.src = avatar_url;

    if (name) {
        name1.innerHTML = `${name}`;
    }
    else if (!name) {
        name1.innerHTML = `${login}`;;
    }
	
	if (bio) {
        bio1.innerHTML = `${bio}`;
    }
    else if (!bio) {
        bio1.innerHTML = '';
    }
	
	if (login) {
        username.innerHTML = `@${login}`;
    }
    else if (!login) {
        username.innerHTML = '';
    }
	
	if (public_repos) {
        posts.innerHTML = `${public_repos}`;
    }
    else if (!public_repos) {
        posts.innerHTML = '0';
    }
	
	if (followers) {
        follower1.innerHTML = `${followers}`;
    }
    else if (!followers) {
        follower1.innerHTML = '0';
    }
	
		if (following) {
        following1.innerHTML = `${following}`;
    }
    else if (!following) {
        following1.innerHTML = '0';
    }
}