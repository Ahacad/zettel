Note: Based on the regular expressions, Python offers two different primitive operations. The match method checks for a match only at the beginning of the string while search checks for a match anywhere in the string. [[regex]]
re.match()
re.match() function will search the regular expression pattern and return the first occurrence. This method checks for a match only at the beginning of the string. So, if a match is found in the first line, it returns the match object. But if a match is found in some other line, it returns null.
For example, consider the following code. The expression "w+" and "\W" will match the words starting with letter 'g' and thereafter, anything
