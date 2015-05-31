from post import Post
from os import listdir
from os.path import isfile, join

def main():	

	# READ TEMPATE HTML FILES
	base_html = open("templates/base.html")
	post_html = open("templates/post.html")

	# CREATE PAGE
	page = base_html.readlines()
	posts = []

	# OPEN POST TXT FILES
	postfiles = [ f for f in listdir("posts") if isfile(join("posts",f)) ]

	for postfile in postfiles:
		temp = open("posts/" + postfile, "r")
		postlines = temp.readlines()
		post_obj = Post(postlines[0], postlines[1], postlines[2:])
		posts.append("".join(post_obj.render(post_html)))
		post_html.seek(0)
		temp.close()

	# INSERT POSTS INTO PAGE
	for i in range(len(page)):
		page[i] = page[i].replace("[[posts]]", "\n\n".join(posts))

	# WRITE PAGE TO OUTPUT HTML FILE
	final = open("output/final.html", "a+")
	final.write("".join(page))

	# CLOSE FILES
	base_html.close()
	post_html.close()

main()