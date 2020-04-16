class Fruits():
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories
        
    def __str__(self):
        return f"{self.name} and {self.calories}"
    
    def __len__(self):
        return self.calories
      
      
 ## my_list = Fruits("Banana", 200)
 ## print(my_list)
 ## len(my_list
