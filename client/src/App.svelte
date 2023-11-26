<script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Nav from './lib/Nav.svelte'
  import Home from './lib/Home.svelte'

  import Router, { link } from "svelte-spa-router";
  import { routes } from "./lib/routes.js";
</script>

  <!--<Counter />-->
<main>
    <Router {routes}/>
</main>

<!--<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style>
-->