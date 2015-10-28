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
Costello   The pitcher's name? 
Abbott     Yes! 
Costello   If I mentioned the third baseman's name, who did I say is playing third? 
Abbott     What? 
Costello   Who's wife? 
Abbott     Who 
Costello   I throw it to I Don't Know. I Don't Know. I Don't Know. I Don't Know throws it to who? 
Abbott     Naturally 
Costello   I'm only asking you, who's the guy runs to second. Who picks up the first baseman, how does he sign his name?
Abbott & Costello Together   Third base! 
```
