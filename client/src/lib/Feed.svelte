<script>
    //export let postdict = [];
    let booklist = [];
    import Nav from './Nav.svelte'
    import {link, push} from 'svelte-spa-router';
    import { onMount } from 'svelte';
    import Card from './Card.svelte';
    import { isloggedin } from './stores';
    let showLogout = true;
    let modal;

    let dialog;

    onMount(async () => {
        const res = await fetch('./allposts');
        const resp = await res.json();
        booklist = resp.reverse();
    });

    function logout(){
        const lo = fetch('./logout', {
            method:'POST',
            body: JSON.stringify({'logout': true}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let loggedOut = res['logoutsuccessful'];
            if (loggedOut == true){
                showLogout = false;
                isloggedin.set(false)
                push('/login')
            }
        }))
    }

</script>


<main>
    <head>
    </head>
    <Nav/>
    <div class="container">
        <h1>Feed</h1>
        <a class="rtalign" role="button" href="/#/post">Create new post</a>
        <div class="grid">
            {#each booklist as book}
                <Card book={book} />
            {/each}
        </div>
    </div>
</main>

<style>
    @media only screen and (max-width:595px){ .grid{ grid-template-columns:repeat(1, 1fr); } }
    @media only screen and (min-width:600px){ .grid{ grid-template-columns:repeat(1, 1fr); } }
    @media only screen and (min-width:785px){ .grid{ grid-template-columns:repeat(2, 1fr); } }
    @media only screen and (min-width:890px){ .grid{ grid-template-columns:repeat(3, 1fr); } }
</style>
