export default function Entry() {
    return (
        <article className="journal-entry">
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
        <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet"/>
            <div className="main-image-container">
                <img src="https://scrimba.com/links/travel-journal-japan-image-url" className="main-image" alt="mount fuji" />
            </div>
            <div>
                <img src="marker.png" className="marker" alt="map marker icon" />
                <span>Japan</span>
                <a href="https://maps.app.goo.gl/C9yndcNEs9Vw2YUN8">View on Google Maps</a>
                <h2>Mount Fuji</h2>
                <p>12 Jan, 2021 -24 Jan, 2021</p>
                <p>Mount Fuji is the tallest mountain in Japan, standing at 3,776 meters (12,380 feet). Mount Fuji is the
                    single most popular tourist site in Japan, for both Japanese and foreign tourists.
                </p>
            </div>
        </article>
    )
}