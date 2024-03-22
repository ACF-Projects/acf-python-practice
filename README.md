# ACF Python Repository

This repository contains a variety of assignments and demos to be used by ACF (Applied Computing Foundation) coaches.

This list is not exhaustive and is vaguely sorted on difficulty.
Assignments further down typically require more Python background to complete.

## How To Use

Every folder represents a single assignment, with comments inside of every file
introducing the problem statement and required code. To work with the code:

1. download/clone this repository
2. choose an assignment you'd like to complete (see the list below)
3. find its respective folder and its `main.py` file (and other files in the folder if provided)
4. ensure Python is installed on your computer and start coding!<br/>

_Alternatively, you may also copy the code of a file and paste it into an environment that can run Python like [the Replit website](https://replit.com/~)._

## Folder Structure

Every subfolder in `exercises` contains files for the TEMPLATED Python assignment. This can be given to a student to complete. Each subfolder also contains a separate `complete` folder, which houses a potential solution to the problem with completed code.

(Alternatively, there is also a `demos` folder which contains completed projects.
These may be shown to pique student interest.)

### Practice Exercises

input practice:

- [Kahoot link for understanding](https://play.kahoot.it/v2/?quizId=6372bfd5-97ae-4f63-8b18-bf3f44ccf8dc)

conditional practice:

- `exercises/bank-cracker`
  - Break into ACF's secret bank account by **reverse-engineering Python code** that was previously deemed "secure"... learn how to manipulate inputs and data types to figure out the secret code and gain access to their vault!
- [Kahoot link for understanding](https://play.kahoot.it/v2/?quizId=16a1e9b8-bd6d-496f-82b7-d38973577b7c)

list practice:

- `exercises/valid-word-checker`
  - You're given a list of almost ALL of the valid words in the English dictionary. Python can loop through this quickly, so without worrying about speed, let's **write code to spellcheck our writing**!
- [Kahoot link for understanding](https://play.kahoot.it/v2/?quizId=874fa8a0-a4b7-4673-8040-005db7118ba9)

for-loop practice:

- `exercises/database-scanning`
  - You're given a database of employee information, stored in a list. Figure out how to write a loop and **analyze every employee's individual information** to get some important statistics and promote the hardest workers!
- [Kahoot link for understanding](https://play.kahoot.it/v2/?quizId=a6977ead-1e54-40b9-9ca2-470312072f3e)

for-loop/while-loop practice:

- `exercises/password-strength`
  - My password _"hi"_ is weak? What about... _"hi3"_? Oops, maybe not. Here, you'll **write some code that separates passwords into three categories: weak, moderate, and strong**. Then, you can come up something that turns it into something stronger!
- [Kahoot link for understanding](https://play.kahoot.it/v2/?quizId=0655996e-1917-44a2-8157-f2203521676a)

function practice:

- `exercises/word-counter`
  - Given a giant assortment of words, **write some code to count the occurrences of a specific word**! Then, use this program to find the most popular word in the document.
- `exercises/custom-interpreter`
  - Python is an interpreted language, built off of the C programming language (sometimes, it's referred to as _CPython_). Here, you'll write code to **design your own programming language runnable by a unique file extension** by parsing tokens and checking conditions!
  - _(This is a relatively difficult exercise; establish a good understanding of an interpreter before approaching this!)_
- [Kahoot link for understanding](https://play.kahoot.it/v2/?quizId=5f57d7aa-49eb-4ff0-b4ac-93ac761a56aa)
- [Kahoot link for vocab](https://play.kahoot.it/v2/?quizId=ba829f77-4878-4540-8d53-46cf55d31a94)

file reading/writing practice:

- `exercises/explore-courses`
  - We've supplied you a database of course information from Stanford University. The problem? There's thousands of courses! Finish the pre-existing code to **make parsing through the database easier** and help students find the courses they want.
- `exercises/pokemon-data`
  - We _almost_ have a working text-based Pokemon game! We just need to scrape a file and create some Pokemon objects for each one. You'll need to write some code to **retrieve Pokemon information from this pre-made file**; feel free to add your own, too!

oop practice:

- [Kahoot link for understanding](https://play.kahoot.it/v2/?quizId=44f51349-4de0-4d28-8667-8b911eef5519)

queue practice:

- `exercises/song-queuer`
  - Who needs Spotify, when we can just make our own version of it? Here, we'll explore the queue data structure and use it to **make a FIFO (first-in-first-out) playlist** to play the songs we want in order! (No actual audio plays in this exercise.)

stack practice:

- `exercises/valid-parentheses`
  - The "valid parentheses" problem is a common question that's shown up in big tech company interviews in the past. Here, you'll learn how to **implement your own version of the stack data structure** and use it to solve the problem efficiently!

optimization practice:

- `exercises/search-optimization`
  - It takes a while to search for an item in our list, when our list has upwards of millions or billions of elements. Here, you'll **gain exposure to the popular binary search method** to cut down our runtime significantly!
- `exercises/sort-optimization`
  - How do computers sort a list? It turns out that it's actually super complicated, and there's many different ways to do it. Here, you'll **implement a few of them: bubble sort and selection sort**, and see how they compare in runtime to Python's tim sort.

### Demos

O(N) visualization + multithreading:

- `demos/mt-timevisualizer`
  - Visualize the power of various algorithms with the **matplotlib graphing library**! To speed things up, we can also use **multithreading: running code simultaneously** rather than waiting for old code to complete.

Multithreaded password cracker:

- `demos/mt-passcracker`
  - See **a brute-force password cracker in Python**! Give it a string of characters to guess, and it'll loop through all possible combinations in an attempt to guess it. We can make this even faster with multithreading!!

<br>
<small><i>List compiled and projects developed by Lucas Wang.
Inspiration for `bank-cracker` project taken from Stanford University, CS107.
</i></small>
