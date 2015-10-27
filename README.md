# fbgen
Markov-generated Facebook chat

Tools for processing the heap of HTML Facebook's request data feature provides to JSON, and subsequently into Markov-generated madness flavoured to your favourite friends. Interface coming soon™.

Thanks to agiliq for boosting me with this gist: https://gist.github.com/agiliq/131679#file-gistfile1-py

## Example
```python
from code.conversation_reader import ConversationReader
from code.conversation_generator import ConversationGenerator

conv_data = ConversationReader.read_json_to_list("example/whos_on_first.json")
cg = ConversationGenerator(conv_data)

cg.generate_conversation(10)
```
```
Abbott     Because 
Costello   Funny names? 
Abbott     Yes 
Costello   I throw the ball me being a good outfield? 
Abbott     Yes 
Costello   When you pay off the first baseman every month, who gets the money? 
Abbott     I'm telling you. Who's on first, What's on second, I Don't Know is on first 
Costello   So who gets it? 
Abbott     Oh, that's our shortstop! 
Costello   I'm not asking you who's on second 
```
