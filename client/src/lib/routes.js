import Home from './Home.svelte'
import Register from './Register.svelte'
import Day from './Day.svelte'
import Slot from './Slot.svelte'
import Week from './Week.svelte'
import ShowModal from './ShowModal.svelte'
import { wrap } from 'svelte-spa-router/wrap'

export const routes = {
    "/": Home,
    "/register": Register,
    "/today": Day,
    "/slot": Slot,
    "/week": Week,
    "/modaltest": ShowModal
}