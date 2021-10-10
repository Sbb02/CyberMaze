from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

cyberBot = ChatBot(name='Cyber Bot', read_only=True, logic_adapters=['chatterbot.logic.BestMatch'])

cyberBot.storage.drop()

trainer = ListTrainer(cyberBot)

trainerCorpus = ChatterBotCorpusTrainer(cyberBot)

trainerCorpus.train("chatterbot.corpus.english.greetings")

#add some more questions to chat
chat = [['Hello Cyber Bot!',
    'Hello, how are you?'],
    ['I am fine. How are you?',
    'I am fine.'],
    ['How can I help you?',
    'I am doing good'],
    ['How can I help you?',
    'How can I help you?'],
    ['I am fine. How can I help you today?',
    'How can I help you?'],
    ['How are you?'
    'I am fine.'],
    ['What can I call you?',
    'I am Cyber Bot. How can I help you today?'],
    ['Who are you?',
    'I am Cyber Bot. How can I help you today?'],
    ['What is your name?',
    'I am Cyber Bot. How can I help you today?'],
    ['What is cybersecurity',
    'Cybersecurity is the practice of protecting critical systems and sensitive information from digital attacks. Also known as information technology (IT) security, cybersecurity measures are designed to combat threats against networked systems and applications, whether those threats originate from inside or outside of an organization.'
    ],
    ['Tell me something about yourself',
    'I am Cyber Bot, a chatbot designed to answer some questions about cybersecurity or the maze.'],
    ['Who created you?',
    'Fireboys created me'],
    ['What can you do',
    'I can help you with']
    ['0',
    'Thank you.']
    ]

for i in chat:
    trainer.train(i)
print('Hello! I am Cyber Bot, a chatbot designed to answer questions which you might have about the game.')
print('To quit, type 0')
string = input()
while (string!='0'):
    print(cyberBot.get_response(string))
    string = input()
print(cyberBot.get_response('0'))
