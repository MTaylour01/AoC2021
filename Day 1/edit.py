path = "numbers.txt"
import re
with open (path, 'r') as f:
    content = f.read()
    content_new = re.sub(' ', r'\n', content, flags = re.M)

with open (path, "w") as f:
    f.write(content_new)