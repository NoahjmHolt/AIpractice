
#   START UP THE VIRTUAL ENVIORNMENT

source .venv/bin/activate

# PROBLEMS EXPERIENCED AND SOLUTIONS

Chap 2.1
Ran into issue where trying to run recently added files with imports from its own directory were not working
Solution was to add a file named __init__ 
This solution lets python know that the directory is a package and so able to be imported
and used in other files and before it is added, it was maybe trying to use the regular
pkg package and so not seeing the files I had made.

Chap 1.4
struggled for a little while to see how to get the arguments from the terminal input.
Turned out that the 1st or [0] is given by the name of the program.
option [1] was the one I was after and needed to check (the first of the actual arguments passed)


# OTHER NOTES AND COMMENTS

This project is exciting, working with AI.
I have an interview this week with a company making one also so bet this
will be a good talking point to consider and have worked on.

