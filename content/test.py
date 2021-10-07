from os import write


story = "Once upon a time there was a student who took CMPUT404. I forgot the rest of this story :)"
words=  story.split()
for i in range(len(words)):
    with open(f"{i+1}.md", "w") as f:
        f.write(f"Title: {i+1}\n")
        f.write(f"Date: 2021-10-06 8:{len(words)-i:02}\n")
        f.write("Category: Blog\n\n")
        f.write(words[i])
