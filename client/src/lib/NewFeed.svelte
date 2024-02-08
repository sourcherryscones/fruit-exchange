<script>
    import Day from './Day.svelte';
    import { onMount } from 'svelte';
    import Nav from './Nav.svelte'
    import { first_name } from './stores';

    let nameVal = ', '

    first_name.subscribe((val) => {
        nameVal += val;
    })

    let urlbase = 'http://127.0.0.1:5000';
    
    let week = []

    let wd = 0;
    onMount(async () => {
        const res = await fetch(urlbase + '/getschedule');
        console.log("RES IS")
        console.log(res)
        const resp = await res.json();
        console.log(resp)
        week = resp;
        console.log("VALUE OF FIRST NAME STORE VAR")
        console.log(first_name)
    });
</script>

<main class="place-content-center">
    <Nav />
    <h1 class="prose-xl font-bold">hi kids!</h1>
    <div class="flex gap-4 w-fit m-0 place-content-center">
        {#each week as day}
                <Day slots={day} admin={false}/>
        {/each}
    </div>
</main>
