#!/usr/bin/env python
import argparse
from code.conversation_reader import ConversationReader
from code.conversation_generator import ConversationGenerator


descr = "Markov generate a conversation from a conversation JSON file."
parser = argparse.ArgumentParser(description=descr)
parser.add_argument("path", help="Path to conversation JSON.")
parser.add_argument("n", type=int, help="Number of messsages to generate.")

args = parser.parse_args()

conv_data = ConversationReader.read_json_to_list(args.path)
cg = ConversationGenerator(conv_data)

cg.generate_conversation(args.n)
