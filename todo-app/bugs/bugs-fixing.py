# This line of code is missing the close brakets!
answers = ['Yes', 'No', 'Yes', 'No', 'No'
# ---------------------------------------------------------------------------------------------------
# This line of code is missing the commas after 'YES' and 'NO'      
my_answer = input("What is your answer?")
answers = ['Yes', 'No', 'Yes' 'No' my_answer]   
# ---------------------------------------------------------------------------------------------------

#This line of code id missing the "." on the input variable
my_answer = input(What is your answer?)
answers = ['Yes', 'No', 'Yes', 'No', my_answer]

# ---------------------------------------------------------------------------------------------------

This line of code contains the wrong brakets for the string passing the input variable
my_answer = input["What is your answer?"]
answers = ['Yes', 'No', 'Yes', 'No', my_answer]

# ---------------------------------------------------------------------------------------------------
This code is missing the : after True and indent after print
while True
print("Hello")

The programmer here is trying to convert the string "hello" to "HELLO" by using the upper() method:

The argument should be outside of the parentheses ex: print(greetin.upper())
greeting = "hello"
print(upper(greeting))

# ---------------------------------------------------------------------------------------------------
However, the program returns an error. Can you help fix the code, so it prints out HELLO?

A programmer wrote the following program:

countries = []
 
while True:
    country = input("Enter the country: ")
    countries.append(country)
print(countries)     #  --> This print function should be indented

The expected output is as follows:
    Enter the country: Cambodia
    ["Cambodia"]
    Enter the country: Triomindia
    ["Cambodia", "Triomindia"]
    Enter the country

However, the code returns an error instead of the expected output. Fix the code, so it produces the expected output.
# ---------------------------------------------------------------------------------------------------

The programmer is trying to loop over the buttons list and print out each item with the first letter capitalized. However, the programmer has done something wrong. Try to find and fix the issue.

for i in buttons:
    print(i.capitalize())
 
buttons = ["cancel", "reply", "submit"] # This function declaration should be define before the for loop!!!

# ---------------------------------------------------------------------------------------------------

The programmer is again missing something in the code. Try to find what it is and fix it.
buttons = ["cancel", "reply", "submit"]
 
for i in buttons:
print(i.capitalize()) ### Identation require after the for loop!!!

# ---------------------------------------------------------------------------------------------------

#### The code below is supposed to print out the items of the list with the first character of each item capitalized. However, the code contains two errors. Try to find and fix the errors.
for item in ["sandals", "glasses", "trousers"): 
    print(item.capitalize)
    
    #### Two Errors ###
## Wrong brackets are used for the list of items
## The print function is passing the capitalize method without parenthesis i.e: print(item.capitalize())

# ---------------------------------------------------------------------------------------------------
### The programmer is trying to extract and print out 'b' using list indexing, but there is an error. Try to fix it.

elements = ['a', 'b', 'c']
print(elements(1))  ### list objects should be called with [] list not () toples

# ---------------------------------------------------------------------------------------------------

The code below aims to replace 'b' with 'x' in the list elements.

However, the output of the code is still ['a', 'b', 'c'].

Try to fix the code so 'b' is replaced with 'x'.

elements = ['a', 'b', 'c']
new = 'x'
new = elements[1] #### The "new" variable should be defined by "element[1]". i.e = elements[1] = new
print(elements)

# ---------------------------------------------------------------------------------------------------
### Supposedly, the following program should:

 1. Prompt the user to input an index (e.g., 0, 1, or 2).

 2. Print out the item with that index.

However, there is a bug with the program which you should try to fix.

menu = ["pasta", "pizza", "salad"]
 
user_choice = input("Enter the index of the item: ") # argument has an error: int(input("Enter....."))
 
message = f"You chose {menu[user_choice]}."
print(message)
# ---------------------------------------------------------------------------------------------------
### Here is another piece of buggy code:

menu = ["pasta", "pizza", "salad"]
 
for i, j in enumerate[menu]: # enumerate is a function, we need to use round parenthesis, not square brackets.
    print(f"{i}.{j}")

Fix the code, so it prints out the output below:

0.pasta
1.pizza
2.salad

# ---------------------------------------------------------------------------------------------------

Here is another piece of code that contains a bug:

menu = ["pasta", "pizza", "salad"]
 
for i, j in enumerate(menu):
    print("f{i}.{j}") # f should be before the quotes, not after them.
The expected output is this:

0.pasta
1.pizza
2.salad
Fix the bug so the program prints out the above output.

# ---------------------------------------------------------------------------------------------------