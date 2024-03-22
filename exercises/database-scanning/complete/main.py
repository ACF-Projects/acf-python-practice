# DATABASE SCANNING

# The following includes our database list. 
# You do NOT need to modify it in any way 
# for this exercise.
# It is a giant list with more lists inside. 
# Each inner list follows the same order:
# [ name, title, salary ]
# name, title, and salary are ALL strings.
database = [n.strip().split(",") for n in open("database.txt").readlines()]

# PART 1: Print the information of every 
# employee in the database on separate lines. 
# (Do not print the database list, but print 
# every list inside.)

for worker in database:
    print(worker)
  
# PART 2: Print out the NAME of every worker 
# that has a salary under $30,000.
# (The expected output should be Pete, Gavin, 
# Lucas, Chris, and Lucy.)

for employee in database:
    salary = int(employee[2])
    if salary < 30000:
        print(employee[0])

# PART 3: If any employee that is a WORKER in 
# the database has a salary over $30,000, change 
# their title from WORKER to OFFICER. Print the 
# list to make sure your changes are correct.
# (Bob, Mildew, Ashley, Eric, Ariel, and 
# Catherine should now appear as "Officer".)

for employee in database:
    role = employee[1]
    salary = int(employee[2])
    if role == "Worker" and salary > 30000:
        employee[1] = "Officer"

for worker in database:
    print(worker)