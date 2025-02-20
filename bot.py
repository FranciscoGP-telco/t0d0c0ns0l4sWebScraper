#Class with the logic about the telegram Bot
class telegramBot():
    def __init__(self, token, chatId):
        self.token = token
        self.chatId = chatId
    
    def getMessages(self):
        url = f'https://api.telegram.org/bot{self.token}/getUpdates'
        results = requests.get(url).json()
        for result in results['result']:
            username = result['message']['from']['username']
            message = result['message']['text']
            print(f'Username: {username}; Message: {message}\n')
                
    def sendMessage(self, message):
        print(message)
        url = f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chatId}&text={message}'
        print(requests.get(url).json())
