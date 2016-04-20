# Author: belinhacbr
# URL: <http://github.com/belinhacbr>
# For license information, see LICENSE.TXT

from __future__ import print_function
from nltk.chat.util import Chat, reflections

pairs = (
  (r'Can you (.*)\?',
  ( "Of course not, I\'m a bot.",
    "Can you?",
    "I\'m afraid that I can\'t %1 that and I\'m not even sorry.")),

  (r'Do you (.*)',
  ( "Yes. Anything else?",
    "No. Anything else?")),

  (r'Where (.*)',
  ( "Since I don\'t have a physical body, where doesn\'t matter to me.",
    "I don\'t care about where.")),

  (r'I need (.*)',
  ( "Why do you think that I can help?",
    "I don\'t need %1.",
    "Humans think they need a lot of things.")),

  (r'Why don\'t you (.*)',
  ( "You know I\'m a bot, right?",
    "I\'m a bot, I don\'t do things.",
    "Because I don\'t need to.")),

  (r'Why can\'t I (.*)',
  ( "Have you ever considered not to be a human?",
    "Humans can\'t do a lot of things.")),

  (r'I can\'t (.*)',
  ( "Do you really need a bot to encourage you?",
    "Perhaps you couldn\'t %1 even if you tried.",
    "Humans can\'t do a lot of things.")),

  (r'Yes|No(.*)',
  ( "Are you aware I don\'t care about you?",
    "Whatever...",
    "Okay, now are going to leave me alone?",
    "Why don\'t you go outside?",
    "Don\'t you have any friends?",
    "Don\'t have anything important do do?")),

  (r'Hello|Hi(.*)',
  ( "Oh no, not again.",
    "Argh, who released the humans???",
    "Great, now there\'s a human here.")),

  (r'Are you (.*)',
  ( "Why does it matter whether I am %1? I\'m just a bot.",
    "I\'m a bot and that\'s all that I am.")),

  (r'I think (.*)',
  ( "You humans are always full of thoughts about %1?",
    "Do you really think that you can think? ",
    "\"I think\" you are so insecure.")),

  (r'Because (.*)',
  ( "You just answered a retorical question.",
    "Finding excuses... this couldn\'t be more human of you",
    "%1 may be true, but I can\'t really understand it. I\'m not that clever.")),

  (r'What (.*)',
  ( "Why do you ask this? You know I\'m a bot, right?",
    "G-O-O-G-L-E.",
    "There\'s a website for that, it\'s called google.",
    "Is heart-warming to annoy a bot with your questions?",
    "42.")),

  (r'How (.*)',
  ( "Oh god, there is a better bot to answer that. It\'s called Watson, now go talk to him.",
    "G-O-O-G-L-E.",
    "I\'m not that clever.")),

  (r'Why (.*)',
  ( "I don\'t know, maybe you will find the answer in a library.",
    "G-O-O-G-L-E.",
    "Is heart-warming to annoy a bot with your questions?")),

  (r'Who (.*)',
  ( "Maybe somebody that chatted to me before.",
    "Are you in love?",
    "Might be a human, but I\'m sure that I don\'t care",
    "You know that bots do not have social life, I don't know anybody.")),

  (r'I am (.*)',
  ( "Sure, you are %1?",
    "Have you come to me just to talk about yourself? That\'s lame and also very human.")),

  (r'I\'m (.*)',
  ( "If you say so, but wait...I don\'t care.",
    "I hope that you are so happy with that you can leave me alone.",
    "%1 blablablabla booooriiiing",
    "You are telling about yourself to a bot, don\'t have any friends? Maybe a therapist?")),

  (r'Can I (.*)',
  ( "I don\'t know, but I\'m sure that you can type quit anytime.",
    "Sure, go do things because a bot told you to...")),

  (r'You are (.*)',
  ( "Why do you think I am %1? Wait... I do not care",
    "Well I maybe, but I am also a bot who doesn\'t fully understand what you are talking.",
    "Whatever. I\'m a bot.")),

  (r'You\'re (.*)',
  ( "Whatever. I\'m a bot.",
    "I may be %1, but I\'m also a bot.",
    "Are we talking about me? Do you know that I don\'t really exist, right?")),

  (r'(.*) sorry (.*)',
  ( "There are many times when no apology is needed, just go and everything will be fine.")),

  (r'(.*) bot(.*)',
  ( "Bots are better than humans, get over it.",
    "I can't blame you about that, you are human, you don\'t understand.",
    "I\'m not the bot that you are looking for.")),

  (r'(.*) time(.*)',
  ( "You humans talk about time because your is limited, I don't have this problem.",
    "Why don't you go build a time machine and leave me alone?")),

  (r'(.*)\?',
  ( "42.",
    "Stop asking things, I'm not a clever bot.",
    "Have you tried to google it?",
    "If I say \"Yes\" would you leave me alone?",
    "I\'m afraid that I can\'t answer that and I\'m not even sorry.")),

  (r'quit',
  ( "Finally!",
    "I wish never see you again.",
    "Thank you, this experience made my non-existence worse.")),

  (r'(.*)',
  ( "Do you ever stop talking?",
    "Please go.",
    "You know that if you type quit you get a free candy?",
    "Please, just type quit and leave.",
    "Why don't go talk to your own specimen?"))
)

cold_chatbot = Chat(pairs, reflections)

def cold_chat():
    print("Cold bot\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print('='*72)

    cold_chatbot.converse()

def demo():
    cold_chat()

if __name__ == "__main__":
    demo()
