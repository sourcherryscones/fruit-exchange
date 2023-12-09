import Home from './Home.svelte'
import Register from './Register.svelte'
import Day from './Day.svelte'
import Slot from './Slot.svelte'
import Week from './Week.svelte'
import ShowModal from './ShowModal.svelte'
import LoginPage from './LoginPage.svelte'
import Error from './Error.svelte'
import { wrap } from 'svelte-spa-router/wrap'
import { first_name } from './stores.js'

export const routes = {
    "/": Home,
    "/register": Register,
    "/today": Day,
    "/slot": Slot,
    "/week": wrap({
        component: Week,
        userData: {first_name: first_name}
    }),
    "/modaltest": ShowModal,
    "/signin": LoginPage,
    "/error": Error
}