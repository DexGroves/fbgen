from code.markov_generator import AuthorGenerator
from code.markov_generator import MessageGenerator


class ConversationGenerator(object):
    """Use an AuthorGenerator and a MessageGenerator to make a chat."""

    def __init__(self, msg_data):
        self.authgen = AuthorGenerator(msg_data)

        self.msg_generators = {}
        for cur_author in self.authgen.author_set:
            author_data = [(author, msg) for (author, msg) in msg_data
                           if author == cur_author]
            self.msg_generators[cur_author] = MessageGenerator(author_data)

    def generate_conversation(self, length):
        for talker in self.authgen.generate_authors(length):
            fb_msg = self.msg_generators[talker].generate_message()
            print talker + '\t' + fb_msg
