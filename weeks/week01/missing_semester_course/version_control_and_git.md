# Introduction to Version Control and Git

Version control system is a piece of software that is used to track changes to your software. They also facilitate collaboration and keep a record of all the changes to your codebase. They also contain and keep record of metada, who made changes and what changes were made.

Snapshot: This is the state of a directory and everything inside it.
Blob: This is what a file is referred as in git terminology.
Tree: This is what a folder is referred as in git terminology.

# Git Structure

type blob = array<byte>

type tree = map<string, tree* | blob*>

type commit = string {
	snapshot tree*
	parents array<commits*>
	author string
	message string
}

type objects = blob | tree | commit

objects = map<string, object> (where string is a SHA-1 hash)
 
def strore(obj)
	id = sha1(obj)
	objects[id] = obj

def load(id)
	return objects[id]

references = map(strings, strings) (it maps human readable names to SHA-1 hashes)

So what is a git repositort?
It is a set of objects and references
