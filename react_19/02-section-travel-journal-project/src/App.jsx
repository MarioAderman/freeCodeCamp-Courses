import Header from './Header'
import contentEntries from './Content'
import Entry from './Entry'
import './App.css'

function App() {

  const entryElements = contentEntries.map((entry) => {
    return <Entry
      key={entry.id} 
      /* img={entry.img}
      country={entry.country}
      googleMapLink={entry.googleMapLink}
      name={entry.name}
      date={entry.date}
      description={entry.description} */
      entryObject={entry}
      // {...entry} This is the same as the above commented out code
      />
  })

  return (
    <>
      <Header />
      {entryElements}
    </>
  )
}

export default App
