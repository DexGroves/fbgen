import random


class MarkovGenerator(object):
    """Vanilla Markov generator."""

    def __init__(self):
        pass

    def _generate_database(self):
        """Generate the database of words keyed by prior words."""
        cache = {}
        for w1, w2, w3 in self._triples(self.words):
            key = (w1, w2)
            if key in cache:
                cache[key].append(w3)
            else:
                cache[key] = [w3]
        return cache

    @staticmethod
    def _triples(input_words):
        """
        Generates triples from the given data string.
        So if our string were "What a lovely day", we'd generate:
            (What, a, lovely) and then (a, lovely, day).
        """
        if len(input_words) < 3:
            return
        for i in range(len(input_words) - 2):
            yield (input_words[i], input_words[i+1], input_words[i+2])


class AuthorGenerator(MarkovGenerator):
    """Generate a sequence of authors."""

    def __init__(self, msg_sequence):
        self.words = [author for (author, msg) in msg_sequence]
        self.cache = self._generate_database()
        self.author_set = set(self.words)

    def generate_authors(self, num_authors):
        seed = random.choice(range(len(self.words) - 3))
        seed_word, next_word = self.words[seed], self.words[seed + 1]
        w1, w2 = seed_word, next_word

        gen_words = []
        for i in xrange(num_authors):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])

        return gen_words


class MessageGenerator(MarkovGenerator):
    """Generate a message given author data."""

    def __init__(self, msg_data):
        self.msg_data = [self._add_padding(msg)
                         for (author, msg) in msg_data]

        msg_sublists = [msg.split(" ") for msg in self.msg_data]
        self.words = [item for sublist in msg_sublists
                      for item in sublist]

        self.msg_length = len(self.words)

        self.cache = self._generate_database()

    def generate_message(self):
        msgstart_is = [i for i in range(self.msg_length - 3)
                       if '\000msgstart' in self.words[i]]

        seed = random.choice(msgstart_is)
        seed_word, next_word = self.words[seed], self.words[seed + 1]
        w1, w2 = seed_word, next_word

        gen_words = []
        while (True):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
            if '\000msgend' in w2:
                break
        gen_words.append(w1)
        gen_words.append(w2)

        return self._remove_padding(' '.join(gen_words))

    @staticmethod
    def _add_padding(msg):
        """Track the start and end of messages."""
        return '\000msgstart ' + msg + ' \000msgend'

    @staticmethod
    def _remove_padding(mkstring):
        """Untrack the start and end of messages."""
        mkstring = mkstring.replace("\000msgstart", "")
        return mkstring.replace("\000msgend", "")
