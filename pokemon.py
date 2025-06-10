class Pokemon:
    def __init__(self, entry, name, type, description, is_caught):
        self.entry = entry
        self.name = name
        self.type = type  # back to a simple string
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(f"{self.name}! {self.name}!")

    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")  
        print(f"Description: {self.description}")
        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet.")

# Create the Pikachu object
Pikachu = Pokemon(
    25,
    "Pikachu",
    "Electric",
    "It has small electric sacs on both its cheeks. If threatened, it releases electric charges.",
    True
)

Pikachu.speak()
Pikachu.display_details()
