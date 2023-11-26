<script>
    import Nav from './Nav.svelte'
    import Slot from './Slot.svelte'
    export let slots;
    export let weekday;
    let weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
</script>
<main>
    <div class="card bg-gradient-to-r from-orange-100 to-orange-200">
    <h1 class="font-black text-base">{weekdays[weekday]} | {slots[0]["date"]}</h1>
    {#each slots as s}
        <div>
            <Slot slot_data={s} />
        </div>
    {/each}
    </div>
</main>