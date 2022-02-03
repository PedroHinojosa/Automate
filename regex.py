import re

batRegex = re.compile(r'(Bat|man)')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

print(mo2.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()

print(mo2.group())
