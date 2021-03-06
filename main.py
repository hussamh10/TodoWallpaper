from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Origin
# 8, 8  	430, 8		950, 8
# 8, 464	430, 464	950, 464

# Sizes
# 412, 280 # 530, 280 # 412, 280
# 412, 295 # 530, 295 # 412, 295

# Centres
# 214, 148	695, 148	1156, 148
# 214, 611	695, 611	1156, 611

centre = [(214, 148), (695, 148), (1156, 148), (214, 611), (695, 611), (1156, 611)]

def getNotes():

	todo_file = open("Todo.txt", 'r') 
	lst = todo_file.readlines()
	todos = []	
	for item in lst:
		todos.append (item.replace ('#', '\n'))

	print(todos)

	return todos


def writeNotes(wallpaper, notes):

	txt = ImageDraw.Draw(wallpaper)
	fnt = ImageFont.truetype("RobotoSlab-Thin.ttf", 50)

	i = 0
	for note in notes:
		noteSize = txt.multiline_textsize(note, fnt, 0)
		x = centre[i][0] - noteSize[0]/2
		y = centre[i][1] - noteSize[1]/2
		
		txt.multiline_text((int(x), int(y)), note, fill=(0, 0, 0), font=fnt, spacing=0, align='center')
		
		i = i+1
		
	return wallpaper	
	

def main():
	wallpaper = Image.open("out.bmp")

	notes = getNotes()
	wallpaper = writeNotes(wallpaper, notes)


	wallpaper.show()
	wallpaper.save('wallpaper.bmp')

	return

main()

