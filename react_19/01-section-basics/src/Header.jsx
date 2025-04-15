export default function Header() {
    return (
      <header className="header">
        <img src='/React-Logo.png' className="react-logo" alt="React Logo"/>
        <nav>
          <ul className="nav-list">
            <li className="nav-list-item">Pricing</li>
            <li className="nav-list-item">About</li>
            <li className="nav-list-item">Contact</li>
          </ul>
        </nav>
       </header>
    )
  }