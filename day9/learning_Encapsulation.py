# learning encapsulation

class AIModel:
    def __init__(self, name, accuracy):
        self.name = name                #public
        self._version = 1.0             #protected
        self.___accuracy = accuracy     #private

    def get_accuracy(self):
        return self.___accuracy
    
    def update_accuracy(self, new_accuracy):
        if 0 <= new_accuracy <= 100:
            self.___accuracy = new_accuracy
        else:
            print("Invalid accuracy value")

#Object

model = AIModel("ChatGpt-core", 92)

print("Model: ", model.name)
print("accuracy: ", model.get_accuracy())

model.update_accuracy(95)
print("Updated Accuracy: ", model.get_accuracy())

print(model.__accuracy)