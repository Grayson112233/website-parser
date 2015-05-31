class Post:

	def __init__(self, title, author, body):
		self.title = title.strip() # String
		self.author = author.strip() # String
		self.body = body # List of Strings
		for i in range(len(self.body)):
			body[i] = body[i].strip()
		for i in range(len(self.body)):
			body[i] = "<p> " + body[i] + "</p>"

	def render(self, template):
		lines = template.readlines()
		for i in range(len(lines)):
			lines[i] = lines[i].replace("[[title]]", self.title)
			lines[i] = lines[i].replace("[[author]]", self.author)
			lines[i] = lines[i].replace("[[body]]", "\n".join(self.body))
		return lines