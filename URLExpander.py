origin = input("Enter the original URL, replacing the number to be incremented with a '#' sign: ")
range_bot = input("Enter the starting value for your range: ")
range_top = input("Enter the ending value for your range: ")
name = str(input("Enter the name of the file to save: "))

file_name = name+".html"
origin_string = str(origin)

with open(file_name, 'a') as out:
    out.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><title>title</title></head>')
    out.write('\n')
    out.write('<script src="https://code.jquery.com/jquery-latest.js"></script>')
    out.write('\n')
    out.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>')
    out.write('\n')
    out.write('<body>')

for x in range(int(range_bot), int(range_top)+1):
    new_list = origin_string.replace("#", str(x))
    print(new_list)
    with open(file_name, 'a') as out:
        out.write('<a href="'+new_list+'">'+new_list+'</a>')
        out.write('\n')
    with open(file_name, 'a') as out:
        out.write('<br>')
        out.write('\n')
    with open(file_name, 'a') as out:
        out.write('<br>')
        out.write('\n')

with open(file_name, 'a') as out:
    out.write('<button id="openButton">Open</button>')
    out.write('\n')
    out.write('</body>')
    out.write('\n')

with open(file_name, 'a') as out:
    out.write("<script>$('#openButton').click(function() {$('a').each(function() {window.open($(this).attr('href') );});});</script>")
    out.write('\n')

with open(file_name, 'a') as out:
    out.write('</html>')

