export default function IngredientsList(props) {

    const items = props.ingredients.map((ingredient) => {
        return <li>{ingredient}</li>
    })

    /* 
     Previous way to do it in React
        function handleSubmit(event){
        event.preventDefault()
        console.log('Form submitted!')
        const formData = new FormData(event.currentTarget)
        const newIngredient = formData.get("ingredient")
        setIngredients([...ingredients, newIngredient])
        event.currentTarget.reset()
    } */

    return (
        <section>
            <h2>Ingredients on hand:</h2>
            <ul className="ingredients-list" aria-live="polite">{items}</ul>
            {props.ingredients.length > 3 ? 
                <div className="get-recipe-container">
                    <div ref={props.recipeSection}>
                        <h3>Ready for a recipe?</h3>
                        <p>Generate a recipe from your list of ingredients.</p>
                    </div> 
                    <button onClick={props.getRecipe}>Get a recipe</button>
                </div> : null}
        </section>
    )
}