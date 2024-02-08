<script>
    import Nav from './Nav.svelte'
    import Slot from './Slot.svelte'
    import AdminSlot from './AdminSlot.svelte';
    export let slots;
    export let admin;
    let weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
</script>
<main>
    <div class="card bg-orange-100 w-96 bg-base-100 shadow-xl">
        <figure class="px-10 pt-10">
          <img src="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg" alt="Shoes" class="rounded-xl" />
        </figure>
        <div class="card-body items-center text-center">
          <h2 class="card-title">Shoes!</h2>
          <p>If a dog chews shoes whose shoes does he choose?</p>
          <div class="card-actions">
            <button class="btn btn-primary">Buy Now</button>
          </div>
        </div>
      </div>
</main>