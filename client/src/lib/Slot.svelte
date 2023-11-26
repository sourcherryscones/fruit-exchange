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

    import Modal from './Modal.svelte';
    import BookSlot from './BookSlot.svelte';

	let showModal = false;
</script>

<main>
    <button role="link" class="card-compact rounded w-60 h-auto bg-base-100 text-primary-content my-1 py-3" on:click={() => (showModal = true)}>
        <div class="card-body bg-{slot_data["bookable"]? "base-100" : "neutral"} rounded">
            <h1 class="font-black">{periods[slot_data["slot_id"].slice(-1)]}</h1>
        </div>
    </button>
    <BookSlot bind:showModal>
        <h2 slot="header">
            modal
            <small><em>adjective</em> mod·al \ˈmō-dəl\</small>
        </h2>
    
        <ol class="definition-list">
            <li>of or relating to modality in logic</li>
            <li>
                containing provisions as to the mode of procedure or the manner of taking effect —used of a
                contract or legacy
            </li>
            <li>of or relating to a musical mode</li>
            <li>of or relating to structure as opposed to substance</li>
            <li>
                of, relating to, or constituting a grammatical form or category characteristically indicating
                predication
            </li>
            <li>of or relating to a statistical mode</li>
        </ol>
    
        <a href="https://www.merriam-webster.com/dictionary/modal">merriam-webster.com</a>
    </BookSlot>
    <!--<a href="/#/register">
            <button role="link" class="card-compact rounded w-60 h-auto bg-base-100 text-primary-content my-1 py-3">
                <div class="card-body bg-{slot_data["bookable"]? "base-100" : "neutral"} rounded">
                <h1 class="font-black">{periods[slot_data["slot_id"].slice(-1)]}</h1>
                </div>
            </button>
        </a>-->
</main>