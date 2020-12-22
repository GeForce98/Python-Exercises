from urllib import urlopen
from bs4 import BeautifulSoup

#Quincy Asemota
#Weekly Assignment 10

#Welcome Message
print('Please enter the value')

# Getting the URL input from user
url = input("Please enter the URL: ")
r = request.get(url)
soup = BeautifulSoup(r.content)

# Counting number of words
text_p = (' '.join(s.findAll(text = True)) for s in soup.findAll('p'))
c_p = Counter((x.rstrip(punctuation).lower() for y in text_p
  for x in y.split()))
text_div = (' '.join(s.findAll(text = True)) for s in soup.findAll('div'))
c_div = Counter((x.rstrip(punctuation).lower() for y in text_div
  for x in y.split()))
total = c_div + c_p

print(total)

# Total number of each heading
c_H1 = c_H2 = c_H3 = c_H4 = c_H5 = c_H6 = 0
for tag in soup.findAll():
  if (tag.name == "H1"
    or tag.name == "<H1>):
    c_H1 = c_H1 + 1
    if (tag.name == "H2"
      or tag.name == "<H2>):
      c_H2 = c_H2 + 1
      if (tag.name == "H3"
        or tag.name == "<H3>):
        c_H3 = c_H3 + 1
        if (tag.name == "H4"
          or tag.name == "<H4>):
          c_H4 = c_H4 + 1
          if (tag.name == "H5"
            or tag.name == "<H5>):
            c_H5 = c_H5 + 1
            if (tag.name == "H6"
              or tag.name == "<H6>):
              c_H6 = c_H6 + 1 print(c_H1) print(c_H2) print(c_H3) print(c_H4) print(c_H5) print(c_H6)

              # Total number of paragraphs count = 0
              for tag in soup.findAll():
              if (tag.name == 'p'
                or tag.name == '<p>)
                count = count + 1 print(count)

                # Counts the total number of images

                print(len(soup.find_all('img')))

                # Count total number of links count = 0
                for link in soup.find_all('a', href = True):
                count = count + 1 print(count)

                print(des)
