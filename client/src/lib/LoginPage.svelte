<script>
    import { push } from "svelte-spa-router";
    import { isloggedin } from "./stores";
    import { first_name } from "./stores.js"

let username="Hugo Steemers"
let password="ghijkl"

function testfunc(){
    console.log("HI KIDS")
}

function userLogin(){
    console.log("userlogin fucntino has been called!")
        const user = fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            body: JSON.stringify({'username': username, 'password': password}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let userFound = res['success'];
            if (userFound === true){
                username='';
                password='';
                isloggedin.set(true)
                first_name.set(res["firstname"])
                push('/week');
            } else{
                if (res['error'] == 'USER NOT FOUND'){
                    push('/error')
                }
                //showHint=true;
            }
        }));
    }
</script>
<div>    <input name="username" type="text" placeholder="Type here" bind:value={username} class="input input-bordered input-primary w-full max-w-xs" />
    <input name="passwd" type="password" placeholder="Type here" bind:value={password} class="input input-bordered input-primary w-full max-w-xs" />
    <input type="submit" value="Log In" class="btn btn-neutral" on:click={() => {userLogin()}} />
</div>