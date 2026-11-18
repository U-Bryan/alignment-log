#!/bin/bash - used to run bash scripts (called shebang)


# Commands ------------------------------------------------------------------------------------------
# man - Gives you the manual for any command
# cd - 'change directory' command used to change directory
# cd . - brings you back into your current directory
# cd .. - takes you to the parent directory
# tab (on keyboard) - used to autocomplete
# which (then a command) - used to show the path of a command 
  # e.g which date will output the path of the date command
# ls - list command that lists the contents of a directory
# cat - print out the contents of a file
# sort - take its input, or file reffered to in it input, and print it out in sorted order
# head - prints the first n lines on a file (default is 10 lines)
  # e.g head -n3 data, data is the file we want to print from, -n3 is the number of lines
# grep - searcher that searches in files and directories for specific input
  # e.g grep 3 data, searches data for lines with the number 3 and prints it
  # e.g grep -r grep ., this searches recursively for grep starting from current directory
# sed -  used to search and replace
  # e.g sed -i 's/grep/jon/g' */*.md, -i does in-place replacement, rather than creating a new file
  #  the 's/grep/jon/g' replaces grep with jon globally and and */*.md searches this path
  #  and every other path for any .md file and these are the files that get the replacement
# awk - used for parsing files or pulling data from semi-structured files
  # e.g awk '{print $2}' data
# find - a command that find files
  # find ~/Downloads -type f -name '*.zip', find any file in downloads folder with name ending in .zip
# rm - remove, used to remove file, folder, or any specifi item
# | = pipe, used to take the output of one command and feed as input into another command
# chmod - give/take file permissions
  # chmod +x lecture.sh, gives execute permission
