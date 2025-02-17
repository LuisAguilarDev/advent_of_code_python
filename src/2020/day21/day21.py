import os
from collections import defaultdict
import heapq

# --- Day 21: Allergen Assessment ---
file_path = os.path.join(os.path.dirname(__file__), "day21.txt")

with open(file_path, "r") as file:
    contents = file.read().splitlines()

# sprint(contents)
text = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
          trh fvjkl sbzzf mxmxvkd (contains dairy)
          sqjhc fvjkl (contains soy)
          sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()

# cuales ingredientes no contienen alergenos
# cuantas veces aparecen
def getData(lists):
    recipes = []
    allergens = []
    for recipe in lists:
        [raw_ing,raw_allergens] = recipe.split("(")
        l = []
        for ingredient in raw_ing.split(" "):
            if ingredient.strip() != "":
                l.append(ingredient.strip())
        recipes.append(l)
        a = []
        for allergen in raw_allergens.replace(",","").split(" "):
            at = allergen.strip(") ")
            if at != "" and at != "contains":
                a.append(at)
        allergens.append(a)
    return recipes,allergens

def countIngredients(recipes,allergen_list):
    recipes_by_allergen = dict() # allergen: recipes[]
    for ing, allergens in zip(recipes, allergen_list):
        for allergen in allergens:
            recipes_by_allergen.setdefault(allergen, []).append(set(ing))
    allergens = set()
    for allergen,allergen_recipes  in recipes_by_allergen.items():
        new_allergens = set.intersection(*allergen_recipes)
        allergens.update(new_allergens)
    count = defaultdict(int)
    for recipe in recipes:
        for ingredient in recipe:
            if ingredient not in allergens:
                count[ingredient] += 1
    return sum(count.values())
    
value = countIngredients(*getData(contents))
assert(value == 2374)

#Part 2
def allergensSorted(recipes,allergen_list):
    recipes_by_allergen = dict() # allergen: recipes[]
    for ing, allergens in zip(recipes, allergen_list):
        for allergen in allergens:
            recipes_by_allergen.setdefault(allergen, []).append(set(ing))
    allergens = set()
    name_allergens = dict()
    for allergen,allergen_recipes  in recipes_by_allergen.items():
        new_allergens = set.intersection(*allergen_recipes)
        name_allergens[allergen] = new_allergens
        allergens.update(new_allergens)
    pq = []
    for name,posibles in name_allergens.items():
        heapq.heappush(pq, (len(posibles),posibles,name))
    names = dict()
    while pq:
        _,posibles,name = heapq.heappop(pq)
        if len(posibles) == 1:
            names[name] = posibles.pop()
            continue
        posibles.difference_update(names.values())
        if len(posibles) == 1:
            names[name] = posibles.pop()
        else: heapq.heappush(pq, (_+1,posibles,name))
    res = []
    for name in sorted(names.keys()):
        res.append(names[name])
    return ",".join(res)

        

value = allergensSorted(*getData(contents))
assert(value == "fbtqkzc,jbbsjh,cpttmnv,ccrbr,tdmqcl,vnjxjg,nlph,mzqjxq")