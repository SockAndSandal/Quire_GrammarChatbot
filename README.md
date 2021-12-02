# Quire - A Chatbot that's built to point out your mistakes. Gramatically.

##### _This chatbot is made on Rasa 3.0, so please make sure you have Rasa 3.0 installed on the env for proper functioning of this chatbot._

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
  **Quire**: Umbrella(noun): a device consisting of a circular canopy of cloth on a folding metal frame supported by a central rod, used as protection against rain or sometimes sun. 

### Ask Quire to tell you to rhyming words for a word.
  **You**: Give me rhyming words for old. \
  **Quire**: old rhymes with cold, fourfold, and sheepfold
######  _(They're a little odd for rhymes, but that's got more to do with the API it is pulling from than Quire itself.)_

### Ask Quire to tell you to opposite words for a word.
  **You**: What is the opposite of brother? \
  **Quire**: brother x sister 

### BONUS: Ask Quire to tell you a joke. Or tell it your name, it will remember. You could also ask Quire why it is named that and it will tell you.


### Current Issues:

1. Quire doesn't take very well to typos in the words themselves. It might understand when you say "what is the oposite of brother" but is much less likely to understand or give you the right response if you spell "brother" wrong. This has got to do with the fact that the words are the literal queries that feed as input to our API and the API doesn't take very well to typos.
2. While Quire is good at slot mapping for a large variety of words, whether that is for meanings of words or using in sentences, it can fail at mapping the correct word to the slots when it encounters words that are very different from what it's been trained for. While it is easy to mitigate this issue using a form format where I turn this into a multi-turn conversation and ask to input the word in a different sentence, I don't think that is a natural way to interact with a chatbot in the real world. 
