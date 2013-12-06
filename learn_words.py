#!/usr/bin/env python
# -*- coding: utf-8 -*- from __future__ import unicode_literals
# @Author: Roman Zaytsev

# word = {original:"", translation, }
# words file format:
#   word1: translation2, translation2, ...
#   word2: translation2, translation2, ...

from sys import argv, exit
from os.path import exists
from random import randint

OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

if len(argv)>1:
    file_locaton = argv[1]
else:
    file_locaton="words.txt"

if not exists(file_locaton):
    print(WARNING+"Words file doesn't exist! Please put the file in current folder or set path to file as a script argument"+ENDC)
    exit(0)

words = []

f = open(file_locaton,"r")
for line in f:

    if line.strip() !="":
        words.append({"original": line.split(":")[0].strip(), "translation": line.split(":")[1].strip()})


passed_words_index = []
for i in xrange(0,len(words)):
    random = randint(0,len(words)-1)
    while random in passed_words_index:
        random = randint(0,len(words)-1)
    passed_words_index.append(random)
    print(words[random]['original'])
    answer = raw_input("?: ")
    correct_answers = []
    for item in words[random]['translation'].split(','): correct_answers.append( item.strip().upper() )

    if answer.upper() !='Q':
        if answer.upper() in correct_answers:
            print(OKGREEN + 'Right!' + ENDC+'\n')
        else:
            print(FAIL +'Wrong!  Answer is: ' + words[random]['translation']+ENDC+'\n')
    else:
        exit(0)
