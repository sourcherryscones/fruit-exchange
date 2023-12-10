<script>
    export let slot_data;
    let periods = {
        "1": "Period 1",
        "2": "Period 2",
        "3": "Period 3",
        "4": "Period 4",
        "5": "Period 5",
        "L": "Lunch", 
        "6": "Period 6",
        "7": "Period 7"
    }

    let slotname = periods[slot_data["slot_id"].slice(-1)]

    import BookSlot from './BookSlot.svelte';

	let showModal = false;
</script>

<main>
    <button role="link" disabled={!slot_data["bookable"]} class="card-compact rounded w-60 h-auto {(slot_data["bookable"]) ? "bg-base-100" : "bg-red-400"} text-primary-content my-1 py-3" on:click={() => (showModal = true)}>
        <div class="card-body rounded">
            <h1 class="font-black">{slotname}</h1>
        </div>
    </button>
    <BookSlot bind:showModal slot_name={slotname} sdata={slot_data}/>
        <!--<a href="/#/register">
            <button role="link" class="card-compact rounded w-60 h-auto bg-base-100 text-primary-content my-1 py-3">
                <div class="card-body bg-{slot_data["bookable"]? "base-100" : "neutral"} rounded">
                <h1 class="font-black">{periods[slot_data["slot_id"].slice(-1)]}</h1>
                </div>
            </button>
        </a>-->
</main>