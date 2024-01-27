# DATABASE SCANNING

"""
Here, your task is to write some code that
filters through a database of employee info 
and find specific employees. Then, you will 
also have to update the database to automate 
some changes.

If there are any questions about this
assignment, feel free to ask questions!
"""

# The following includes our database list. 
# It is a big list containing inner lists. 
# Each inner list follows the same order:
# [ name, title, salary ]
# (Note: name, title, and salary are strings.)
database = [n.strip().split(",") for n in open("database.txt").readlines()]

# PART 1: Print the information of every 
# employee in the database on separate lines. 
# (Do not print the database list, but print 
# every list inside.)


  
# PART 2: Print out the NAME of every worker 
# that has a salary under $30,000.
# (The expected output should be Pete, Gavin, 
# Lucas, Chris, and Lucy.)



# PART 3: If any employee that is a WORKER in 
# the database has a salary over $30,000, change 
# their title from WORKER to OFFICER. Print the 
# list to make sure your changes are correct.
# (Bob, Mildew, Ashley, Eric, Ariel, and 
# Catherine should now appear as "Officer".)

