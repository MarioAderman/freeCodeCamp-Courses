import { useState, useRef, useEffect } from 'react'
import IngredientsList from './IngredientsList'
import ClaudeRecipe from './ClaudeRecipe'
import { getRecipeFromChefClaude } from '../ai'

export default function Main() {
    const [ingredients, setIngredients] = useState([])
    const [recipe, setRecipe] = useState("")
    const recipeSection = useRef(null)

    useEffect(() => {
        if (recipe !== "" && recipeSection.current !== null) {
            recipeSection.current.scrollIntoView({ behavior: "smooth" })
        }
    }, [recipe])

    function addIngredient(formData) {
        const newIngredient = formData.get("ingredient")
        setIngredients(prevIngredients => [...prevIngredients, newIngredient])
    }

    async function getRecipe() {
        const recipeMarkdown = await getRecipeFromChefClaude(ingredients)
        console.log(recipeMarkdown)
        setRecipe(recipeMarkdown)
    }

    return (
        <main>
            <form className="add-ingredient-form" action={addIngredient}>
                <input
                    type="text"
                    placeholder="e.g. oregano" 
                    aria-label="Add ingredient"
                    name="ingredient"
                />
                <button>Add ingredient</button>
            </form>
            {ingredients.length > 0 ? 
                <IngredientsList ref={recipeSection} ingredients={ingredients} getRecipe={getRecipe} /> 
                : null}
            {/* {recipe === true ? <ClaudeRecipe recipe={recipe} /> : null} */}
            {recipe && <ClaudeRecipe recipe={recipe} />}
        </main>
    )
}