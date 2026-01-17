it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
---> 7

it_companies.add('twitter')
print(it_companies)
---> {'twitter', 'IBM', 'Microsoft', 'Amazon', 'Facebook', 'Oracle', 'Apple', 'Google'}

it_2 = {'Techstar','Richards','FinWorlds'}
it_companies.update(it_2)
print(it_companies)
---> {'Oracle', 'Techstar', 'Richards', 'IBM', 'Apple', 'Google', 'FinWorlds', 'Amazon', 'Microsoft', 'Facebook'}

it_companies.remove('IBM')
print(it_companies)
---> {'Microsoft', 'Amazon', 'Facebook', 'Google', 'Oracle', 'Apple'}

# Element exists in the set
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set) # Output: {1, 3}
# Element does not exist
my_set.remove(4) # Raises KeyError: 4 

# Element exists in the set
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set) # Output: {1, 3}
# Element does not exist
my_set.discard(4) # No error, set remains unchanged
print(my_set) # Output: {1, 3}

# Exercises: Level 2

A.update(B)
print(A)
---> {19, 20, 22, 24, 25, 26, 27, 28}

print(A.intersection(B))
---> {19, 20, 22, 24, 25, 26}

print(A.issubset(B))
---> True

print(A.isdisjoint(B))
---> False

A.update(B) and B.update(A)
print(A)
print(B)
---> {19, 20, 22, 24, 25, 26, 27, 28}
{19, 20, 22, 24, 25, 26, 27, 28}

print(A.symmetric_difference(B))
---> {27, 28}

del(A,B)
print(A)
print(B)
--->     print(A)
          ^
NameError: name 'A' is not defined

# Exercises: Level 3

ages = set(age)
print(ages)
len_set=len(ages)
len_lst=len(age)
print(len_set)
print(len_lst)
if len_lst > len_set:
    print('lenght of list is greater than lenght of set')
else:
    print('lenght of set is greater than lenght of list')
 --->{19, 22, 24, 25, 26}
5
8
lenght of list is greater than lenght of set

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
diff_words = set(words)
print(diff_words)
len_of_diff_words = len(diff_words)
print(f'{len_of_diff_words} Different Words have been used in the Sentence ')
---> {'teach', 'I', 'and', 'love', 'a', 'teacher', 'people', 'to', 'inspire', 'am'}
10 Different Words have been used in the Sentence 


Questions : 

#Exercises: Level 1
1.Find the length of the set it_companies
2.Add 'Twitter' to it_companies
3.Insert multiple IT companies at once to the set it_companies
4.Remove one of the companies from the set it_companies
5.What is the difference between remove and discard

#Exercises: Level 2
1.Join A and B
2.Find A intersection B
3.Is A subset of B
4.Are A and B disjoint sets
5.Join A with B and B with A
6.What is the symmetric difference between A and B
7.Delete the sets completely

#Exercises: Level 3
1.Convert the ages to a set and compare the length of the list and the set, which one is bigger?
2.I am a teacher and I love to inspire and teach people.
How many unique words have been used in the sentence? 
Use the split methods and set to get the unique words.









