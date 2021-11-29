# Quire - A Chatbot that's built to point out your mistakes. Gramatically.

## Steps for Installation
1. Clone this repo into a folder of your choosing.
2. Make sure you have **Python** (`brew install python`), **Rasa** (`pip install rasa[full]`), and **Keras Tensorflow** installed (`pip install tensorflow`)
3. Alternatively, you can also use the requirements folder in the repo to install everything you need.
4. Navigate (`cd`) to the cloned repository.
5. Start the action server with `rasa run actions` and leave this running in a terminal window.
6. Open a new terminal window and run `rasa shell`

## Suggested Conversation Flows

### Ask Quire to tell you to use a word in a sentence.
  You: Hi \
  **Quire**: Hi! How can I help you? \
  **You**: Use the word angry in a sentence \
  **Quire**: They were angry because their plans had been discovered \
  **Quire**: Was that helpful? \
  **You**: No \
  **Quire**: She gave her companion an angry glance. \
  **Quire**: Was that helpful? \
  **You**: Yes \
  **Quire**: Great!

### Ask Quire to tell you the meaning of a word.
  **You**: What does umbrella mean? \
  **Quire**: Umbrella(noun): a device consisting of a circular canopy of cloth on a folding metal frame supported by a central rod, used as protection against rain or sometimes sun. \
  **Quire**: Was that helpful? \
  **You**: Yes \
  **Quire**: Great!

### Ask Quire to tell you to rhyming words for a word.
  **You**: Give me rhyming words for old. \
  **Quire**: old rhymes with cold, fourfold, and sheepfold
######  _(They're a little odd for rhymes, but that's got more to do with the API it is pulling from than Quire itself.)_

### Ask Quire to tell you to opposite words for a word.
  **You**: What is the opposite of brother? \
  **Quire**: brother x sister 

### BONUS: Ask Quire to tell you a joke. Or tell it your name, it will remember. 
