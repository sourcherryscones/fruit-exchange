<script>
	export let showModal; // boolean
	export let slot_name;
	export let sdata;
	import { push } from 'svelte-spa-router'
	let weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


	let reasonforreq = '';
	let descrip = '';

	let dialog; // HTMLDialogElement
	let urlbase = 'http://127.0.0.1:5000';

	let stuff;

	function bookRoom(){
		console.log("bookroom function called")
        const bookroom = fetch(urlbase + '/book', {
            method: 'POST',
            body: JSON.stringify({'title': reasonforreq, 'description': descrip, 'slot_id': sdata["slot_id"], 'date': sdata["date"]}),
			headers: {
				'Content-Type': 'application/json'
			}
        }).then(resp => resp.json().then(res => {
            let id = res['id'];
            if (id){
                reasonforreq='';
                descrip='';
				dialog.close()
                push('/week');
            } else{
                push('/error')
            }
        }));
    }

	$: if (dialog && showModal) dialog.showModal();
</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-noninteractive-element-interactions -->
<dialog
	bind:this={dialog}
	on:close={() => (showModal = false)}
	on:click|self={() => dialog.close()}
>
    <div on:click|stopPropagation role="button" tabindex="0">
        <div>
            <div class="card-body cursor-auto">
					<div class="space-y-12">
					  <div class="border-b border-gray-900/10 pb-12">
						<h2 class="text-base font-semibold leading-7 text-gray-900">Book a room during <span class="text-red-500 font-bold">{slot_name}</span> on {weekdays[sdata["day"]]}<span class="text-red-500 font-bold"></span></h2>
						<p>Current number of requests: {sdata["freq"]}</p>
						<p class="mt-1 text-sm leading-6 text-gray-600">This information will help our librarians prioritize your request accordingly!</p>
				  
						  <div class="sm:col-span-4">
							<div class="mt-2">
							  <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
								<input type="text" name="title" autocomplete="username" class="mx-2 block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6" placeholder="Reason for request" bind:value={reasonforreq}>
							  </div>
							</div>
							<div class="mt-2">
								<textarea name="description" rows="3" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="More details, if you'd like to share :)" bind:value={descrip}></textarea>
							  </div>
						  </div>
					  </div>
					</div>
					<input hidden name="date" value={sdata["date"]}>
					<input hidden name="slot_id" value={sdata["slot_id"]}>
					<div class="card-actions justify-end">
						<button class="btn btn-error btn-outline" on:click={() => dialog.close()}>Cancel</button>
						<button class="btn btn-warning" on:click={() => bookRoom()}>Book</button>
		
					</div>
            
            </div>
        </div>
    </div>
	<!-- svelte-ignore a11y-no-static-element-interactions
	<div on:click|stopPropagation>
		<slot name="header" />
		<hr />
		<slot />
		<hr />
		svelte-ignore a11y-autofocus
		<button autofocus on:click={() => dialog.close()}>close modal</button>
	</div>-->
</dialog>

<style>
	dialog {
		max-width: 32em;
		border-radius: 0.2em;
		border: none;
		padding: 0;
	}
	dialog::backdrop {
		background: rgba(0, 0, 0, 0.3);
	}
	dialog > div {
		padding: 1em;
	}
	dialog[open] {
		animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
	}
	@keyframes zoom {
		from {
			transform: scale(0.95);
		}
		to {
			transform: scale(1);
		}
	}
	dialog[open]::backdrop {
		animation: fade 0.2s ease-out;
	}
	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}
	button {
		display: block;
	}
</style>
