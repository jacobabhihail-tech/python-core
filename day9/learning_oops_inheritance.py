# Base Class

class BaseAIService:
    def service_info(self):
        print("This is a base AI serivce")

    def process(self, data):
        return data
    
#Child Class(Inherits BaseAiServices)
class ChatbotSerivce(BaseAIService):
    def respond(self, message):
        processed_message = self.process(message)
        return f"Bot reply: {processed_message}"
    
#object creation

bot = ChatbotSerivce()

#output
bot.service_info()
reply = bot.respond("Hello AI")
print(reply)
