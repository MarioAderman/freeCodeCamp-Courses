import { Fragment } from 'react' // Fragment is a built-in component that allows you to group multiple elements together
import './App.css';
import Header from './Header'
import MainContent from './MainContent'
import Footer from './Footer'

function App() {

  return (
    <Fragment> {/* It can also be written as empty angle brackets <></> */}
        <Header />
        <MainContent />
        <Footer />
      </Fragment>
  )
}

export default App
