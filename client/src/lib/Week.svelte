<script>
    import Day from './Day.svelte';
    import { onMount } from 'svelte';
    import Nav from './Nav.svelte'

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
    });
</script>

<main class="w-fit m-0 place-content-center">
    <Nav />
    <div class="flex gap-4 w-fit">
        {#each week as day}
                <Day slots={day} weekday={wd}/>
        {/each}
    </div>
</main>
