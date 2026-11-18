# Introduction to Version Control and Git

Version control system is a piece of software that is used to track changes to your software. They also facilitate collaboration and keep a record of all the changes to your codebase. They also contain and keep record of metada, who made changes and what changes were made.

Snapshot: This is the state of a directory and everything inside it.
Blob: This is what a file is referred as in git terminology.
Tree: This is what a folder is referred as in git terminology.

# Git Structure

type blob = array<byte>

type tree = map<string, tree* | blob*>

type commit = string { <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;snapshot tree* <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parents array<commits*> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;author string <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message string
}

type objects = blob | tree | commit

objects = map<string, object> (where string is a SHA-1 hash)
 
def strore(obj)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id = sha1(obj) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;objects[id] = obj 

def load(id) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return objects[id]

references = map(strings, strings) (it maps human readable names to SHA-1 hashes) <br>

So what is a git repositort? <br>
It is a set of objects and references
