document.addEventListener("DOMContentLoaded", () => {
    async function fetchUsers() {
        try {
            const response = await fetch("https://reqres.in/api/users/");
            const json = await response.json();
            Users(json.data);
        } catch (err) {
            console.error(err);
        }
    }

    function Users(users) {
        users.forEach((user) => {
            const userDiv = document.createElement("div");
            userDiv.classList.add("bg-white","hover" ,"text-dark", "p-3", "m-2", "col-auto", "rounded");

            const userName = document.createElement("h3");
            userName.innerHTML = user.first_name;
            userName.classList.add("my-2", "text-truncate");
            userDiv.appendChild(userName);

            const userEmail = document.createElement("p");
            userEmail.innerHTML = user.email;
            userDiv.appendChild(userEmail);

            const userimg = document.createElement("img");
            userimg.classList.add("img-fluid", "rounded-circle");
            userimg.src = user.avatar;
            userDiv.appendChild(userimg);

            document.getElementById("users").appendChild(userDiv);
        });
    }


    fetchUsers();
});
