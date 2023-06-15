// #Pseudocode
// #Input- stories length, moral lessons, and the age group 
// #Output- A display of the recorded stories and the story being told in another language.
// #Process - Create a class Story with attriutes in the constructor then create methods record and translate
// # story

class Story{
constructor (storyLength,moralLesson,ageGroup){
this.storyLength=storyLength
this.moralLesson=moralLesson
this.ageGroup=ageGroup
}
record(storyTitle){
    let stories=[]
    return stories.push(storyTitle)
}

}
class StoryTeller extends Story{
    tellStory(storyTitle){
        return `The story being told is ${storyTitle}`

    }   
    
}
let story=new Story("Short story","Children must respect elders","5-15")
console.log(story.record("The child that was beaten"));
let storyTeller=new StoryTeller("Long story","We should work hard","15-35")
console.log(storyTeller.tellStory("The Man that became rich"));


// #Pseudocode
// # Input - ingredients,preparation time, cooking method and nutritional information 
// #Output- Detail aout a specific African food 
// #Process - Create a class `Recipe` class, with attriutes in the constructor,
// #  then subclasses that inherit attributes from  Recipe class  then create methods 
// # display food cooked for each African recipe from the subclasses

class Recipe{
    constructor(ingredients,preparationTime, cookingMethod,nutritionalInformation ){
     this.ingredients=ingredients
     this.preparationTime=preparationTime
     this.cookingMethod=cookingMethod
     this.nutritionalInformation=nutritionalInformation
    }
   displayFood(foodName){
    return `The food being cooked is ${foodName}`
   }
}
class MoroccanRecipe extends Recipe{
    displayFood(foodName){
        return `The food being cooked is ${foodName}`
       }

}
class EthiopianRecipe extends Recipe{

displayFood(foodName){
    return `The food being cooked is ${foodName}`
   }
}

class NigerianRecipe extends Recipe{
   displayFood(foodName){
    return `The food being cooked is ${foodName}`
   }
}

let moroccan =new MoroccanRecipe("tomatoes, cucumber and onions","30 mins","mixed","Gives vitamins")
console.log(moroccan.displayFood("Salad"));
let nigerian=new NigerianRecipe("Flour, water","45 minures","Boiling and stirring","Carbohydrates")
console.log(nigerian.displayFood("Fufu"));
let ethiopian=new EthiopianRecipe("Wheat flour, yoghurt,salt","2 hrs","fermentation","adds minerals")
console.log(ethiopian.displayFood("Injera"));


// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.

//pseudocode

//// # Input - diet, typical lifespan, migration
// patterns
// #Output- Information about animals
// #Process - Create a class Species class, with attriutes in the constructor,
// #  then subclasses Predator`, `Prey that inherit attributes from  class Species then create methods 
// # 

class Species{
    constructor(diet,lifespan, migration){

    }
}