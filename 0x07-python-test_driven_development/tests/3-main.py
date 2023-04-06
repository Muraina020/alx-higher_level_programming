#!/usr/bin/python3
says_my_name = __import__('3-say_my_name').says_my_name

says_my_name("John", "Smith")
says_my_name("Walter", "White")
says_my_name("Bob")
try:
    says_my_name(12, "White")
except Exception as e:
    print(e)
