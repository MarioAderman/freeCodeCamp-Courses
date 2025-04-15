export default function Entry(props) {
    return(
        <article className="journal-entry">
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
        <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet"/>
            <div className="main-image-container">
                <img src={props.entryObject.img} className="main-image" alt="main-img" />
            </div>
            <div>
                <img src="marker.png" className="marker" alt="map marker icon" />
                <span className="country">{props.entryObject.country}</span>
                <a href={props.entryObject.googleMapLink}>View on Google Maps</a>
                <h2>{props.entryObject.name}</h2>
                <p>{props.entryObject.date}</p>
                <p>{props.entryObject.description}</p>
            </div>
        </article>
    )
}