#**Ancestral Stories:** In many African cultures, the art of storytelling is passed
#down from generation to generation. Imagine you're creating an application that
#records these oral stories and translates them into different languages. The
#stories vary by length, moral lessons, and the age group they are intended for.
#Think about how you would model `Story`, `StoryTeller`, and `Translator`
#objects, and how inheritance might come into play if there are different types of
#stories or storytellers.


#Pseudocode
#Input- stories length, moral lessons, and the age group 
#Output- A display of the recorded stories and the story being told in another language.
#Process - Create a class Story with attriutes in the constructor then create methods record and translate
# story

class Story:
    def __init__(self,story_length,moral_lesson,age_group):
        self.story_length=story_length
        self.moral_lesson=moral_lesson
        self.age_group=age_group
    def record(self,story_title):
        stories=()
        # stories.__add__(story_title)
        return stories
class StoryTeller (Story):
    def __init__(self, story_length, moral_lesson, age_group):
        super().__init__(story_length, moral_lesson, age_group)
    def tell_story(self,story_title):
        return f"The story being told right now is {story_title} "
   # def translate(self):


story=Story("Short story","Children must respect elders","5-15")
# print(story.record("The child that was beaten"))
story_teller=StoryTeller("Long story","We should work hard","15-35")
print(story_teller.tell_story("The Man that became rich"))

#**African Cuisine:** You're creating a recipe app specifically for African cuisine.
#The app needs to handle recipes from different African countries, each with its
#unique ingredients, preparation time, cooking method, and nutritional
#information. Consider creating a `Recipe` class, and think about how you might
#create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
#`EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
#methods.

#Pseudocode
# Input - ingredients,preparation time, cooking method and nutritional information 
#Output- Detail aout a specific African food 
#Process - Create a class `Recipe` class, with attriutes in the constructor,
#  then subclasses that inherit attributes from  Recipe class  then create methods 
# display food cooked for each African recipe

class Recipe:
    def __init__(self,ingredients,preparation_time, cooking_method,nutritional_information ):
        self.ingredients=ingredients
        self.preparation_time=preparation_time
        self. cooking_method=cooking_method
        self.nutritional_information=nutritional_information
    def display_food(self, food_name):
        return f"The food cooked is {food_name} "
class MoroccanRecipe (Recipe):
    def __init__(self, ingredients, preparation_time, cooking_method, nutritional_information):
        super().__init__(ingredients, preparation_time, cooking_method, nutritional_information)
    def display_food(self, food_name):
        return super().display_food(food_name)
class EthiopianRecipe (Recipe):
    def __init__(self, ingredients, preparation_time, cooking_method, nutritional_information):
        super().__init__(ingredients, preparation_time, cooking_method, nutritional_information)
    def display_food(self, food_name):
        return super().display_food(food_name)
class NigerianRecipe(Recipe):
    def __init__(self, ingredients, preparation_time, cooking_method, nutritional_information):
        super().__init__(ingredients, preparation_time, cooking_method, nutritional_information)
    def display_food(self, food_name):
        return super().display_food(food_name)
    
moroccan =MoroccanRecipe("tomatoes, cucumber and onions","30 mins","mixed","Gives vitamins")
print(moroccan.display_food("Salad"))
ethopian=EthiopianRecipe("Wheat flour, yoghurt,salt","2 hrs","fermentation","adds minerals")
print(ethopian.display_food("Injera"))
nigerian=NigerianRecipe("Flour, water","45 minures","Boiling and stirring","Carbohydrates")
print(nigerian.display_food("Fufu"))