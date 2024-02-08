<script>
  let urlbase = 'http://127.0.0.1:5000'
  import { push } from 'svelte-spa-router'
  import { isloggedin } from "./stores";
  function logout(){
      const lo = fetch(urlbase + '/logout', {
          method:'POST',
          body: JSON.stringify({'logout': true}),
          headers: {
              'Content-Type': 'application/json'
          }
      }).then(resp => resp.json().then(res => {
          let loggedOut = res['logoutsuccessful'];
          if (loggedOut == true){
              isloggedin.set(false)
              console.log("made it to pre-re-navigation thingy")
              push('/signin')
          }
      }))
    }
</script>

<main class="container">
  <div class="navbar bg-base-100">
    <div class="navbar-start">
      <div class="dropdown">
        <label tabindex="0" class="btn btn-ghost lg:hidden">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" /></svg>
        </label>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-70">
          <li><a>Item 1</a></li>
          <li>
            <a>Parent</a>
            <ul class="p-2">
              <li><a>Submenu 1</a></li>
              <li><a>Submenu 2</a></li>
            </ul>
          </li>
          <li><a>Item 3</a></li>
        </ul>
      </div>
      <h1 class="font-black">Tino Conf</h1>
    </div>
    <div class="navbar-center hidden lg:flex">
      <ul class="menu menu-horizontal px-1">
        <li><a>Item 1</a></li>
        <li tabindex="0">
          <details>
            <summary>Parent</summary>
            <ul class="p-2">
              <li><a>Submenu 1</a></li>
              <li><a>Submenu 2</a></li>
            </ul>
          </details>
        </li>
        <li><a>Item 3</a></li>
      </ul>
    </div>
    <div class="navbar-end">
      <button class="btn btn-error" on:click={() => {logout()}}>Log Out</button>
    </div>
  </div>
    <!---->
    
  </main>

  <style>
    nav{
      margin-bottom:20px;
      margin-top:0px;
    }
    ul{
      margin-top:0px;
    }
  </style>