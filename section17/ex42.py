# Define speak below:

def speak(animal="dog"):
    
    noises = {
        "pig": "oink",
        "duck": "quack",
        "cat": "meow",
        "dog": "woof"
    }
    
    if animal in noises:
        return noises.get(animal)    
    return "?"
    