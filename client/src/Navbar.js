export const Navbar = (props) => {
  return (
    <nav>
      <div className="nav-wrapper">
        <a href="#" className="brand-logo">Logo</a>
        <ul id="nav-mobile" className="right hide-on-med-and-down">
          <li><a href="sass.html">Sass</a></li>
          <li><a href="badges.html">Components</a></li>
          <li><a href="collapsible.html">Sign in</a></li>
          <li><a className="waves-effect waves-red darken-1 btn-flat">Sing up</a></li>
        </ul>
      </div>
    </nav>
  );
};
