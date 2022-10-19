import string
import collections

def caesar(rotate_string, number_to_rotate_by):
       return rotate_string.translate(str.maketrans(string.ascii_lower, "{}{}".format(str.ascii_lower[number_to_rotate_by:],str.ascii_lower[:number_to_rotate_by])))

caesar(ABCDEFGHIJKLMNOPQRSTUVWXYZ,13)