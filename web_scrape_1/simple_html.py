from bs4 import BeautifulSoup

SIMPLE_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SIMPLE_HTML</title>
</head>
<body>
    <h1>This is the title</h1>
    <p class="subtitle">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque dolore doloremque hic magnam, nam nostrum perferendis qui tempora vel vero.</p>
    <p>Here is another p tag without a class</p>
    <ul>
        <li>Derek</li>
        <li>Adam</li>
        <li>Debra</li>
        <li>Kevin</li>
        <li>Patrick</li>
    </ul>
</body>
</html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_contents)

def find_subtitle():
    p = simple_soup.find('p', {'class': 'subtitle'})
    print(p.string)

def find_other_p():
    p = simple_soup.find_all('p')
    other_p = [i for i in p if 'subtitle' not in i.attrs.get('class', [])]
    print(other_p[0].string)

find_title()
find_list_items()
find_subtitle()
find_other_p()