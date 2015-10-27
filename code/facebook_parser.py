import json
from lxml import html


class FacebookParser(object):
    """
    Parse the horrible Facebook data messages.htm into something more useful.
    Produces tab-delimited conversation logs in parsed_convos.
    """
    def __init__(self, path):
        self.lower_size_limit = 500

        with open(path) as fb_html:
            html_string = fb_html.read()

        tree = html.fromstring(html_string)
        convos = self.get_conversations(tree)

        conv_lists = [self.parse_convo(convo) for convo in convos]

        self.conv_dict = self.reduce_convos_by_authors(conv_lists)

        self.save_all_convos_to_files()

    def parse_convo(self, convo):
        parsed_convo = zip(self.get_msg_author(convo), self.get_msg_txt(convo))
        return [(self.delist(msg), self.delist(txt))
                for [msg, txt] in parsed_convo]

    def reduce_convos_by_authors(self, conv_lists):
        convo_dict = {}
        for i in range(len(conv_lists)):
            convo = list(reversed(conv_lists[i]))
            author_str = self.get_convo_authors(convo)
            if author_str in convo_dict.keys():
                convo_dict[author_str] = convo_dict[author_str] + convo
            else:
                convo_dict[author_str] = convo
        return convo_dict

    def save_all_convos_to_files(self):
        for filename, convo in self.conv_dict.iteritems():
            if len(convo) > self.lower_size_limit:
                filepath = 'parsed_convos/' + filename + '.json'
                self.save_convo_to_file(convo, filepath)

    @staticmethod
    def save_convo_to_file(parsed_convo, filepath):
        with open(filepath, 'w') as outfile:
            json.dump(parsed_convo, outfile,  indent=4)

    @staticmethod
    def get_conversations(tree):
        return tree.xpath('//div[@class="thread"]')

    @staticmethod
    def get_msg_author(convo):
        msgs = convo.xpath('div[@class="message"]' +
                           '/div[@class="message_header"]')
        return [msg.xpath('span[@class="user"]/text()') for msg in msgs]

    @staticmethod
    def get_convo_authors(convo):
        authors = [author for (author, msg) in convo]
        authors = [auth.replace(' ', '')
                   for auth in set(authors) if "@" not in auth]
        return '-'.join(sorted(authors))

    @staticmethod
    def get_msg_txt(convo):
        ps = convo.xpath('p')
        return [p.xpath('text()') for p in ps]

    @staticmethod
    def delist(xml_entry):
        if xml_entry == []:
            return ''
        return xml_entry[0]
