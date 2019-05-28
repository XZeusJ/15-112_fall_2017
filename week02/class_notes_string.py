# Some String Constants
import string
print(string.ascii_letters)   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print("-----------")
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)          # 0123456789
print("-----------")
print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.printable)       # digits + letters + punctuation + whitespace
print("-----------")
print(string.whitespace)      # space + tab + linefeed + return + ...


# Some String Operators 
	# String + and *
	# The in operator
	# String indexing and slicing

# Some String-related Built-In Functions
	# input(), str(), and len()
	# chr() and ord()
	# eval()

# Some String Methods
	# Character types: isalnum(), isalpha(), isdigit(), islower(), isspace(), isupper()
	# String edits: lower(), upper(), replace(), strip()
	# Substring search: count(), startswith(), endswith(), find(), index()

# String Formatting 
breed = "beagle"
print("Did you see a %s?" % breed)

dogs = 42
print("There are %d dogs." % dogs)

grade = 87.385
print("Your current grade is %0.1f!" % grade)

dogs = 42
cats = 18
exclamation = "Wow"
print("There are %d dogs and %d cats. %s!!!" % (dogs, cats, exclamation))


# format left-aligned with %-[minWidth]
dogs = 42
cats = 3
print("%-10s %-10s" % ("dogs", "cats"))
print("%-10d %-10d" % (dogs, cats))

# Basic File IO
# Note: As this requires read-write access to your hard drive,
#       this will not run in the browser in Brython.

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

contentsToWrite = "This is a test!\nIt is only a test!"
writeFile("foo.txt", contentsToWrite)

contentsRead = readFile("foo.txt")
assert(contentsRead == contentsToWrite)

print("Open the file foo.txt and verify its contents.")
