import re

with open("story.txt", "r") as f:
    story = f.read()

# Extract placeholders using regex
words = set(re.findall(r'<(.*?)>', story))

answers = {}
for word in words:
    answer = input(f"Enter a {word}: ")
    answers[f"<{word}>"] = answer

for placeholder, replacement in answers.items():
    story = story.replace(placeholder, replacement)

# Print the modified story
print("\nFinal Story:\n")
print(story)