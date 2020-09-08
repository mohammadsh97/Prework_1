# Prework_1
General
The purpose of this exercise is to make sure you understand all the basic syntax of Python.
The task should be written in Python 3.7.
Use PyCharm Community IDE and GIT as specified in the auxiliary requirements you got.
Before heading to the task (described in the next page), read the guidelines written below.
It is also recommended to overview the suggested links at the end of this file for some background.
Guidelines
1. Use Python 3.7.x.
2. Suggested IDE is PyCharm Community.
3. Read the exercise to the end and make sure you understand it well.
4. Start implementing according to the exercise chronology.
5. Create the modules and the packages when first needed (and not in advance).
6. Use the same classes and functions names that are used in the exercise.
7. Use helper functions.
8. Use meaningful names.
9. Document your code where and whenever necessary.
10. Prefer to use the “re” module in places you need to manipulate strings (like with emails and
phones in the Person module).
11. Remember that Python interpreter will not warn on code errors which were not used or
reached yet.
12. Remember to convert int to str in case you want to concatenate it with strings.
13. Remember the functions len, type, and how to properly handle exceptions.
14. Prefer list comprehensions over regular for loop.
15. In terms of efficiency, remember that some of the pythonic types are immutable (such as
strings and tuples).
16. Test your code frequently, make sure any recent addition functions properly.
 
Packages
There will be two packages:
• workers in which the foundational modules for workers are defined
• hwltd in which the application of HelloWorld ltd. is written Package workers
This package defines two modules:
• person defines personal details
• structure defines positions and roles Package hwltd
This package defines two modules:
• organization defines organizational structures
• reports defines reports Phase I
Module person
• Class Person –
o Each object initializes the following variables: first and last name, year of birth,
email, phone(s), address [use __init__()]
o Firstandlastnamemustnotbeempty
o ID number is automatic – the first Person gets the ID 1, the next gets 2, etc. [use
class variable, @classmethod]
o Email must not be empty, and must include a name (alpha-numeric chars), followed by the ‘@’ symbol, then one or more subdomains separated by dots, and finally, another dot and the domain name – which must be ‘hwltd.com’ (e.g., jake@japan.asia.hr.hwltd.com or laura@mng.hwltd.com) [for that purpose, use a @staticmethod, in which you use regular expression].
o A list of phones
o Anaddress
o All the details should be entered when initializing the object.
o The name, ID and email should never be changed (possible to enforce in python?). o Phones might be added or removed later.
o Addressmightbechanged.
• Class Phone
o Definesaphonenumber
o Might start with a ‘+’ sign or a digit
o Might include (excluding the ‘+’ prefix) only digits and hyphens • Class Address
o Holds country and city
o Bothmustnotbeempty
o Provide a method that returns the address as a nicely formatted string. The string
will be constructed from the country, the city and the results of a ‘protected’
  
method that returns the other details of the address [use the single underscore to
identify it as ‘protected’. Throw NotImplementedError to make it ‘abstract’].
• Class StreetAddress
o InheritsAddress
o Holds in addition the street name and house number [use super() for initializer]
o Overridetheabstractmethodofaddressdetailstoreturnthestreetandnumber • Class PobAddrees
o InheritsAddress
o Holds post office box number [use super() for initializer]
o Overridetheabstractmethodofaddressdetailstoreturnthepostofficebox
Module structure
• Class Group
o Defines a group in the organization.
o A group has a name, a description, and its parent group (might be None).
o A group might have either a list of subgroups or a list of workers
o A group should provide a method get_workers() that returns a list of its workers; if it
has subgroups, then this list includes all the workers in those subgroups
▪ If you did not already do it that way, this is a good opportunity to use list
comprehension
▪ If you did not already do it – it might be even better to return a generator
expression instead
▪ ➔If you are new to “list comprehension” and “generator expression”, do it
first your own way and once you finish the first version of the exercise, get
back and refactor your code after learning those mechanisms.
▪ In case needed, consider using the chain() method from itertools module.
o A group should provide a method get_parents() that returns a list containing the parent group, and then the grand-parent group, and so on, until there are no more parents.
▪ A better way: let the function yield the values instead of returning them as list. If you do not know what ‘yield’ is, finish the first version of the exercise first and then get back here and refactor your code.
• Worker
o Holds a variable of type Person
o Holds a salary variable
o Provides a method get_salary() that returns the salary
• Engineer
o InheritsWorker
o Holds a bonus variable
o Overrides get_salary() so that it returns salary + bonus • SalesPerson
o InheritsWorker
o Holds commission (as a fraction)
o Holds “deals” – a list with the amounts of all the deals they have made
o Overrides get_salary() so that it returns the salary + commission * (sum of deals)

Phase II
Module organization
• Defines the organizational structure of Hello World ltd.: o HelloWorld
▪ Engineering Department • SW Group
o InfrastructureTeam o AppTeam
o DriversTeam
o QA Team
• HW Group
o ChipTeam
o BoardTeam
o PowerTeam
• CTO Group
• System Group
o DesignTeam
o PocTeam ▪ HR Department
• Recruitment Group o Tech Team o Staff Team
• Culture Group ▪ Finance Department
• Salaries Group
• Budget Group
o IncomeTeam o OutcomeTeam
• Define a class Employees, that holds a dict of all employees (names), using their email as the key (remember that dictionary is not hashable).
• Define a class HelloWorld, that holds the organizational structure, and gets a path to a file at initialization. It reads from the file all the workers in the company and adds them to an Employees object.
o If you did not already do so, open the file using with. If you are not familiar with that keyword, do it first the way you know, and after finishing the first version of the exercise, get back here and refine your code.
• In the file, each worker is defined in a separate row as follows (rows starting with a hash tag (‘#’) should be ignored):
<last_name>, <first_name>, <year_of_birth>, <email>, <phones>, <address>, <team>, <role>, <data>
Where –
o phonesmightincludezeroormorephones,separatedwithasemicolon(‘;’)

o addresscanbeeitherintheformof<country;city;street;number>or <country;city;pots_office_box_number>
o rolemustbeoneof:‘staff’,‘engineer’,‘sales’
o team is one of the teams defined in the organization structure o <data> is role-specific, as follows:
▪ for ‘staff’: the salary
▪ for ‘engineer’: <salary;bonus>
▪ for ‘sales’: <salary;commission;deal_1;deal_2;...;deal_n>
o For the string manipulations, consider using the following functions: ▪ split(), strip() and other functions from the re module
Module reports
• get_num_employees(department, depth)
o Provides the number of employees in a department in a dict form
o Department: The department to analyze
o Depth: levels of report
o The report will print the number of workers in the department or the sub
departments, according to the depth level – for example: ▪ report_num_employees(hr, 1) -
HR, 24 workers
▪ report_num_employees(engineering, 3) -
Engineering – 157 workers SW – 82 workers
Infrastructure – 30 workers App – 13 workers
Drivers – 16 workers
QA – 23 workers
HW – 41 workers Chip – 12 workers Board – 17 workers Power – 12 workers
CTO – 7 workers System – 27 workers
Design – 8 workers
Poc – 19 workers • get_average_salary(group)
o Return the average salary of the workers in that group. • get_relational_salary(worker)
o For a given worker, return a dictionary that its keys are the worker’s teammates (excluding the worker itself) and the value is the ratio between the worker’s salary and the teammate salary (e.g., if the workers’ salary is 1200 and the teammate’s salary is 1800, the ratio is 1.5)
 
 Download Python 3.7.x:
https://www.python.org/downloads/
Download PyCharm (IDE for python):
http://www.jetbrains.com/pycharm/download/#section=windows
How to Get Started with Python:
      https://www.programiz.com/python-programming/first-program#what
List of keywords in Python with examples:
https://www.programiz.com/python-programming/keyword-list
Exception handling:
https://www.programiz.com/python-programming/exception-handling
File operations:
https://www.programiz.com/python-programming/file-operation
https://stackoverflow.com/questions/1466000/python-open-built-in-function-difference- between-modes-a-a-w-w-and-r
String manipulations:
https://www.learnpython.org/en/Basic_String_Operations
            Check Types:
https://codeyarns.com/2010/01/28/python-checking-type-of-variable/
Tuple structure:
https://www.tutorialspoint.com/python/python_tuples.htm
Good summery of basic types:
https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
      
 A bit about classes:
https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define- objects-in-python-3
class(object) syntax:
https://stackoverflow.com/questions/10044321/class-classnameobject-what-sort-of-word-is- object-in-python
http://radek.io/2011/07/21/private-protected-and-public-in-python/
        Main function in Python:
https://stackoverflow.com/questions/419163/what-does-if-name-main-do
When to use what (list, dict, set):
https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set
Hashable types:
https://www.quora.com/What-are-hashable-types-in-Python
Generators:
https://www.learnpython.org/en/Generators
Sorting:
https://docs.python.org/3/howto/sorting.html
           Slicing:
https://stackoverflow.com/questions/39241529/what-is-the-meaning-of-in-python
__init__:
https://stackoverflow.com/questions/3782827/why-arent-pythons-superclass-init-methods- automatically-invoked
packages:
https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python- module-and-a-python-package
        
super():
https://rhettinger.wordpress.com/2011/05/26/super-considered-super/ https://www.programiz.com/python-programming/methods/built-in/super
https://www.reddit.com/r/learnpython/comments/zzkp6/pray_help_me_understand_super_ini t_args_and_kwargs/
Exceptions:
https://stackoverflow.com/questions/4990718/python-about-catching-any-exception
       
regex python:
https://www.debuggex.com/cheatsheet/regex/python
https://stackoverflow.com/questions/3075130/what-is-the-difference-between-and-regular- expressions
https://stackoverflow.com/questions/2241600/python-regex-r-prefix https://www.tutorialspoint.com/python/python_reg_expressions.htm
https://stackoverflow.com/questions/500864/case-insensitive-python-regular-expression- without-re-compile
https://stackoverflow.com/questions/1576789/in-regex-what-does-w-mean
