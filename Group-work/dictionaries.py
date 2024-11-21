# NO. 1
# Create a dictionary with three key-value pairs representing a
# student's information: name, age, and grade. Print each key-value pair on a new line.
student_information = {
    "name": "Patricia",
    "age": 21,
    "grade":  'A'
}
for key, value in student_information.items():
     print(f"{key}:{value}")


# NO. 2
#  Write a function that takes a dictionary of people's names and 
# their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, 
# and returns a list of names of people who are 21 or older.

def people_data():
  information = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
  adult_names = []
  
  for name, age in information.items():
       if age >= 21:
            adult_names.append(name)
    
  return adult_names

result = people_data()
print(result)

# NO.3
# Given a dictionary representing items in a store with their prices,
# {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought,
# ['apple', 'orange', 'banana', 'banana'], and calculates the total cost. 
# 
def single_list():
    list1 = [1,2,3]
    list2 = [4,5,6]
    single_list = list1 + list2
    print(f"The single list is {single_list}")
single_list()

#4.Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
def word_count():
    sentence = "hello world hello"
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count)
word_count()


