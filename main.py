import requests
page = requests.get("http://leeil.devnetwedge.com/parcel/view/070209152004/2019")


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


html = list(soup.children)
body=[(item) for item in html][3]
head=list(body.children)[1].get_text()

dic_values={}
dic_values['Parcel ID']=head.replace('\n', '').split(' ')[-1]

payment= list(soup.find('a',  id="PaymentHistory", class_="anchor").next_siblings)


z= [x.tbody.get_text().split('\n') for x in payment[1:2]][0][1:-1]

print (z)


for x, y in zip(list(soup.find('thead'))[1].get_text().split('\n')[1:-1], list(soup.find('tbody'))[1].get_text().split('\n')[1:-1]):
    dic_values[x]=y

labels= [x.get_text().split('\n\n') for x in list(soup.select('thead'))[1:]][0][1:-1][0].split('\n')

taxes=[x.get_text().split('\n\n') for x in list(soup.select('tbody'))[1:]][0][1:-1]
taxes[0]='\n' +taxes[0]
taxes1=[x.get_text().split('\n\n') for x in list(soup.select('tbody'))[1:]][1][1:-1]
taxes1[0]='\n' +taxes1[0]

for x in [list(zip(labels, x.split('\n')[1:])) for x in taxes]:
    for m in x[1:]:
        dic_values[x[0][1]+' '+m[0]]=m[1]

for x in [list(zip(labels, x.split('\n')[1:])) for x in taxes1]:
    for m in x[1:]:
        dic_values[x[0][1]+' '+m[0]]=m[1]

print (dic_values)
