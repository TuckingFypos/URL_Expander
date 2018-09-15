origin = input("Enter the original URL, replacing the number to be incremented with a '#' sign: ")
range_bot = input("Enter the starting value for your range: ")
range_top = input("Enter the ending value for your range: ")
name = str(input("Enter the name of the file to save: "))

file_name = name+".html"
origin_string = str(origin)

with open(file_name, 'a') as out:
    out.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><title>title</title></head><body>')
    out.write('\n')

for x in range(int(range_bot), int(range_top)+1):
    new_list = origin_string.replace("#", str(x))
    print(new_list)
    with open(file_name, 'a') as out:
        out.write('<a href="'+new_list+'">'+new_list+'</a>')
    with open(file_name, 'a') as out:
        out.write('<br>')
    with open(file_name, 'a') as out:
        out.write('<br>')

with open(file_name, 'a') as out:
    out.write('</body></html>')

