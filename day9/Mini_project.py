
class AIModel:
    def __init__(self, name):
        self.name = name
        self.__accuracy = 0

    def update_accuracy(self,value):
        if 0 <= value <= 100:
            self.__accuracy = value
        else:
            print("Accuracy must be between 0 and 100")
    
    def get_accuracy(self):
        return self.__accuracy
    
class VisionModel(AIModel):
    def __init__(self, name, camera_type):
        super().__init__(name)
        self.camera_type = camera_type
    
    def show_details(self):   # only way to see model info
        print(f"Model: {self.name}")
        print(f"camera: {self.camera_type}")
        print(f"Accuracy : {self.get_accuracy()}%")

    def improve_accurracy(self, increase): # only safe way to increase accuracy
        new_value = self.get_accuracy() +increase
        self.update_accuracy(new_value)

class NLPModel(AIModel):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def show_details(self):
        print(f"[NLP Model]")
        print(f"Name : {self.name}")
        print(f"language : {self.language}")
        print(f"Accuracy : {self.get_accuracy()}")


# ---------- RUN ----------
model = VisionModel("FaceDetector", "HD Camera")
nlp = NLPModel("ChatAnalyszer", "English")

model.update_accuracy(88)
nlp.update_accuracy(92)

model.show_details()
print()
nlp.show_details()
#model.improve_accurracy(10)
#model.show_details()





