fun main() {
 var story=Story("Short story","Children should respect elders","5 to 15")
//    println(story.recordStory("The child that was beaten"))
    var storyTeller=StoryTeller("Long story","WE should work hard","15 to 35")
    println(storyTeller.tellStory("The man that got rich"))

    var ethiopian=EthiopianRecipe("Wheat flour, yoghurt,salt","2 hrs","fermentation","adds minerals")
    println(ethiopian.displayFood("Injera"))
    var moroccan=MoroccanRecipe("tomatoes, cucumber and onions","30 mins","mixed","Gives vitamins")
    println(moroccan.displayFood("Salad"))
    var nigerian=NigerianFood("Flour, water","45 minures","Boiling and stirring","Carbohydrates")
    println(nigerian.displayFood("Fufu"))
}

// #Pseudocode
// #Input- stories length, moral lessons, and the age group
// #Output- A display of the recorded stories and the story being told in another language.
// #Process - Create a class Story with attriutes in the constructor then create methods record and translate
// # story
 open class Story(var storyLength:String,var moralLesson:String, var ageGroup:String){
//    fun recordStory(storyTitle:String):String{
//        var stories=()
//        stories.add(storyTitle)
//        return stories
//
//    }

}
class StoryTeller(storyLength: String,moralLesson:String, ageGroup:String):Story(storyLength,moralLesson,ageGroup){
 fun tellStory(storyTitles:String):String{
     return "The story being told is ${storyTitles}"
 }
}


// #Pseudocode
// # Input - ingredients,preparation time, cooking method and nutritional information
// #Output- Detail aout a specific African food
// #Process - Create a class `Recipe` class, with attriutes in the constructor,
// #  then subclasses that inherit attributes from  Recipe class  then create methods
// # display food cooked for each African recipe from the subclasses

open class Recipe(var ingredients:String, var preparationTime:String, var cookingMethod:String, var nutritionalInfo:String ){
fun displayFood(foodName:String):String{
    return "The food being cooked is ${foodName}"
}
}
class MoroccanRecipe(ingredients:String, preparationTime:String, cookingMethod:String, nutritionalInfo:String ):Recipe(ingredients,preparationTime,cookingMethod,nutritionalInfo){
//    fun displayFood(foodName:String):String{
//        return "The food being cooked is ${foodName}"
//    }
}
class EthiopianRecipe(ingredients:String, preparationTime:String, cookingMethod:String, nutritionalInfo:String ):Recipe(ingredients,preparationTime,cookingMethod,nutritionalInfo){
//    fun displayFood(foodName:String):String{
//        return "The food being cooked is ${foodName}"
//    }
}
class NigerianFood(ingredients:String, preparationTime:String, cookingMethod:String, nutritionalInfo:String ):Recipe(ingredients,preparationTime,cookingMethod,nutritionalInfo){
//    fun displayFood(foodName:String):String{
//        return "The food being cooked is ${foodName}"
//    }
}