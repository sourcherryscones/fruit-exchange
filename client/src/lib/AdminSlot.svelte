<script>
    import { push } from 'svelte-spa-router';
    let urlbase = 'http://127.0.0.1:5000';

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

    let slotid = slot_data["slot_id"]

    function reserveSlot(){
        console.log("bookroom function called")
        const bookroom = fetch(urlbase + '/approve', {
            method: 'PATCH',
            body: JSON.stringify({"slot_id": slotid, "date": slot_data["date"], "uid": 1}),
			headers: {
				'Content-Type': 'application/json'
			}
        }).then(resp => resp.json().then(res => {
            push('/admin')
        }));
    }

    let slotname = periods[slot_data["slot_id"].slice(-1)]

    import BookSlot from './BookSlot.svelte';

	let showModal = false;
</script>

<main>
    <div class="drawer drawer-end">
        <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
        <div class="drawer-content">
          <!-- Page content here -->
          <label for="my-drawer-4" class="btn rounded w-60 h-auto {(slot_data["bookable"]) ? "bg-base-100" : "bg-red-400"} text-primary-content my-1 py-3">{slotname}</label>
        </div> 
        <div class="drawer-side z-40">
          <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
          <ul class="menu p-4 w-80 min-h-full bg-base-200 text-base-content">
            <!-- Sidebar content here -->
            <li><a>Hugo Steemers<input type="checkbox" class="checkbox" id="my-checkbox" on:change={reserveSlot()}/></a></li>
          </ul>
        </div>
      </div>
</main>

<style>
    label{
        background-color: white;
        
    }
</style>