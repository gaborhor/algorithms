
# HashTable ADT with chaining implementation
# This hashtable accepts only strings and hashes based on their
# ASCII value of the first char
# The constructor takes in the size of the table

## Example hashtable
# class MyHashtable(object):
#     def __init__(self, size): # Creates an empty hashtable
#         self.size = size
#         # Create the list (of size) of empty lists (chaining)
#         self.table = []
#         for i in range(self.size):
#             self.table.append([])
#     def str (self): # for print
#         return str(self.table)
#     def insert(self, elem): # Adds an element into the hashtable
#         hash = ord(elem[0]) % self.size
#         self.table[hash].append(elem)
#     def member(self, elem): # Returns if element exists in hashtable
#         hash = ord(elem[0]) % self.size
#         return elem in self.table[hash]
#     def delete(self, elem): # Removes an element from the hashtable
#         hash = ord(elem[0]) % self.size
#         self.table[hash].remove(elem)


# Testing code for 'MyHashtable'
# s = MyHashtable(10)
# s.insert("amy") #97
# print(s.str())
# s.insert("chase") #99
# print(s.str())
# s.insert("chris") #99
# print(s.str())
#
# print(s.member("amy"))
# print(s.member("chris"))
# print(s.member("alyssa"))
# s.delete("chase")
# print(s.member("chris"))
# print(s.str())
# Use print(s) at any time to see the contents of the table for debugging



# 'NewHashtable' ADT for Open Addressing w/ Linear Probing
# - Each location in table holds only one value, storing 'None' on __init__
# - Second table will hold the status of each index: 'Empty', 'Filled', or 'Deleted'
# - When insert/delete/find member, use method from 'MyHashtable', ASCII value of first char of str
# - Goal is to insert new member at "next available" spot, searching until finding one that isn't 'Filled'
# - Needs to wrap to start of table w/ a mod when probing.
# - Once spot that isn't 'Filled' encountered, assign new member to it and mark as 'Filled'
# - ASSUME THAT HASHTABLE WILL NEVER FILL UP, DO NOT ACCOUNT FOR THIS
#
# find/delete member are similar:
# - Jump to hashed location, if member there is not desired member, probe down table to find it
# - Search should end if you find desired member, but also if you encounter 'Empty' spot because
# this indicates that desired member DOES NOT EXIST
# - For NewHashtable.member(): simply return T/F
# - For NewHashtable.delete(): if desired member found, set MemberTable value to 'None' and
# StatusTable value to 'Deleted', do not do anything if desired member does not exist
# - Test 'NewHashtable' with the same cases provided for 'MyHashtable'

class NewHashtable(object):
    def __init__(self,size):
        self.size = size
        self.members = [None for i in range(size)]
        self.status = ['Empty' for i in range(size)]
    def memstr (self): # for print
        return str(self.members)
    def valstr (self): # for print
        return str(self.status)
    def insert(self, elem): # Adds an element into the hashtable
        # MUST CHECK STATUS TABLE BEFORE APPLYING MEMBER TABLE CHANGES
        hash = ord(elem[0]) % self.size

        counter = hash # indexing variable for both .members and .status
        counter_start = counter
        while True:
            if counter == self.size:
                counter = 0

            if self.status[counter] != 'Filled':
                self.members[counter] = elem
                self.status[counter] = 'Filled'
                break

            counter += 1
            if counter == counter_start:
                raise Warning(f"{self} object has no fillable spots: .insert() attempt terminated")
                break

    def member(self, elem): # Returns if element exists in hashtable
        hash = ord(elem[0]) % self.size

        counter = hash
        counter_start = counter
        while True:
            if counter == self.size:
                counter = 0

            if self.members[counter] == elem:
                return True
            elif self.status[counter] == 'Empty':
                return False

            counter += 1
            if counter == counter_start:
                return False

    def delete(self, elem): # Removes an element from the hashtable
        hash = ord(elem[0]) % self.size

        counter = hash
        counter_start = counter
        while True:
            if counter == self.size:
                counter = 0

            if self.members[counter] == elem:
                self.members[counter] = None
                self.status[counter] = 'Deleted'
                break

            counter += 1
            if counter == counter_start:
                raise Warning(f"{self} object has no member {elem}: .delete() attempt terminated")
                break


# Testing code 'NewHashtable'
# Specified both .memstr() and .valstr() prints to check Member and Status tables at each step
n = NewHashtable(10)
print(n.memstr())
print(n.valstr())
print("\n")
n.insert("amy") #97
print(n.memstr())
print(n.valstr())
print("\n")
n.insert("chase") #99
print(n.memstr())
print(n.valstr())
print("\n")
n.insert("chris") #99
print(n.memstr())
print(n.valstr())
print("\n")
# Checks for membership
print(n.member("amy"))
print(n.member("chris"))
print(n.member("alyssa"))
n.delete("chase")
print(n.memstr())
print(n.valstr())
print("\n")
print(n.member("chris"))
print(n.memstr())
print(n.valstr())
print("\n")
