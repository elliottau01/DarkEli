#!/usr/bin/env python
# coding: utf-8

# In[1]:


Tall=170
Rich=1000000
Handsome=90
if Tall>=180 and Rich>=1000000 and Handsome>=90:
    print('Tall, Rich, Handsome ')
else: print('SAD')


i=0
print('yo',i)
i=i+1
print('yo',i)
i=i+1
print('yo',i)
i=i+1


def f(x):
    return x+3
print ( f(5) )


a=0
while(a<12):
  print('hello')
  a+=1


var1 = 'Hello World!'
var2 = 'Python Programming'
print( var1 )
print( var2 )


var1 = 'Hello World!'
var2 = 'Python Programming'
print( var1[0] )
print( var2[1:5] )

b = 'Hello World!'
b2 = 'Python Programming'
print( b[0] )
print( b2[1:5] )


score= 10.5
print( type(score))


a= bool(-1)
print(a)


a= 'Fuck' + 'You'
print(a)

a= 'Fuck\n' + 'You'
print(a)

a='test''ing'
print(a)

a='Testing\n' * 10
print(a)


x = '0123456789'
print( x[-1])
print( x[0:5])
print( x[0::2])
print( x[1::2])
print( x[9::-1])
print( x[0:])
print( x[:])

print(x.startswith('01'))
print(x.endswith('6789'))

x = '01234567899999999'
print(x.count('9'))

x = '01234567899999999'
print(x.replace('9','c'))


# In[4]:


def f(x):
    return 3*x + 5 
print (f(5))


# In[7]:


def f(x): 
    return m*x+5 
m=4
print (f(5))


# In[ ]:


# Mat lib 
Colour=input("Enter a colour:")
PluralNoun=input("Enter a plural noun:")
Celebrity=input("Enter the name of a celebrity:")

print('Roses are',Colour)
print(PluralNoun, 'are blue')
print("I love",Celebrity)



# In[27]:


PrimarySchool=input("Enter the name of the primary school:")
SecondarySchool=input("Enter the name of the secondary school:")
University=input("Enter the name of the university:")

print('The primary school that you graduated from is',PrimarySchool)
print('The secondary school that you graduated from is',SecondarySchool)
print('The university that you graduated from is',University)






# In[ ]:


var1='Sa456789'
print ( var1[0:5] )
print ( var1[8::-2])


# In[28]:



Num1=float(input("Enter the first number:"))
OP=input("Enter the operator:")
Num2=float(input("Enter the second number:"))

if OP=='+':
    print('Num1+Num2')
elif OP=='-':
    print('Num1-Num2')
elif OP=='*':
     print('Num1*Num2')
elif OP=='/':
    print('Num1/Num2')
else:
    print('invalid Operator')


# In[23]:


num1 = int(input("num1: "))
op = input("Operator: ")
num2 = int(input("num2: "))

if op == "+":
     print(num1 + num2)
elif op == "-":
     print(num1 - num2)
elif op == "/":
     print(num1 / num2)
elif op == "*":
     print(num1 * num2)
else:
     print("Invalid Operator")


# In[3]:


P=float(input("Principal:"))
M=float(input("Maturity:"))
CR=float(input("Coupon Rate:"))
MIR=float(input("Market Interest Rate:"))
PV=float((P/((1+MIR)**(M)))+((P*CR)*((1-((1+MIR)**(-M)))/MIR)))
print(PV)   
BP=P
CP=P*CR
IP=P*MIR
AA=IP-CP
print("Bond Payable:" + float(P))
print("Cash Payment:" + float(CP))
print("Interest Payment:" + float(IP))
print("Amortization amount:" + float(AA))


# In[8]:


print(42,500)


# In[9]:


print(type(123))


# In[10]:


a=55+5
print('The value is',a)


# In[11]:


print(len("Hello"))


# In[ ]:


print(add(sq))


# In[13]:


import turtle
wn=turtle.Screen()
wn.bgcolor("cyan")
alex=turtle.Turtle()
alex.color("red")
alex.pensize("5")
alex.forward(150)
alex.left(90)
alex.forward(75)
alex.salary=50000
print(alex.salary)
wn.exitonclick()


# In[5]:


import turtle 
wn=turtle.Screen()
wn.bgcolor("white")

jamal=turtle.Turtle()
jamal.color("blue")
jamal.pensize(5)

jamal.right(90)
jamal.forward(60)
jamal.left(90)
jamal.forward(30)

tina=turtle.Turtle()
tina.color('orange')
tina.pensize(5)

tina.left(180)
tina.forward(30)

wn.exitonclick()


# In[1]:


import turtle
wn = turtle.Screen()

Eli= turtle.Turtle()

distance= 60
angle = 90 

for _ in range(10): 
    Eli.forward (distance)
    Eli.left (angle)
    distance = distance + 10 
    angle= angle + 3


# In[4]:


import turtle 

wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess=turtle.Turtle()
tess.color('blue')
tess.shape('turtle')

dist=5 
tess.down()
for _ in range(30): 
    tess.stamp()
    tess.forward(dist)
    tess.right(24)
    dist= dist + 2



# In[1]:


# Wrong
import turtle

wn= turtle.Screen()
wn.bgcolor('lightgreen')

jose=turtle.Turtle()
jose.shape('turtle')
jose.up()

for _ in range(10):
    jose.stamp()
    jose.forward(50)
    jose.right(36)
    jose.forward(-50)


# In[1]:


# Wrong
import turtle

wn= turtle.Screen()
wn.bgcolor('lightgreen')

jose=turtle.Turtle()
jose.shape('turtle')
jose.up()

for _ in range(3):
    jose.stamp()
    jose.forward(-50)
    jose.right(36)
    jose.forward(50)


# In[1]:


# Correct
import turtle

wn= turtle.Screen()
wn.bgcolor('lightgreen')

jose=turtle.Turtle()
jose.shape('turtle')
jose.color('red','pink')
jose.up()

for _ in range(10):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(36)
    
    
    


# In[1]:


class Employee: 
    
    
    def __init__ (self, first, last, pay): 
        self.first= first 
        self.last= last
        self.pay= pay
        self.email= first + '.' + last + '@company.com'
        

emp_1= Employee('Corey', 'Schafer', 50000)
emp_2= Employee('Test', 'User', 60000)


print(emp_1.email)
print(emp_2.email)


# In[1]:


#Star
import turtle 
wn= turtle.Screen()
alex=turtle.Turtle()
alex.color('blue')
alex.up()
alex.forward(60)

for _ in range(5):
    alex.down()
    alex.left(144)
    alex.forward(74.16407865)
    alex.left(72)


# In[1]:


#Regular Pentagon
import turtle 
wn= turtle.Screen()
alex=turtle.Turtle()
alex.speed(0)
alex.color('blue')
alex.up()
alex.forward(60)

alex.down()
alex.left(144)
for _ in range(5):
    alex.forward(74.16407865)
    alex.left(72)


# In[3]:


mylist= ['one', 2, 'three']
myTuple= ('one', 2, 'three')
print(type(mylist))
print(type(myTuple))

mylist= [100]
myTuple= (100,)
print(type(mylist))
print(type(myTuple))


# In[4]:


s= "Python"
mylist=["one",2,"three"]

print(s[0])
print(mylist[0])
print(len(s))
print(len(mylist))

print(s[len(s)-1])


# In[15]:


fuck = "The world fucks me everyday!!!" 
pussy= fuck.index("e")
print(pussy)
coward= fuck.split()
print(coward)
"/".join(coward)
#fuck.split()
#fuck.count('e')
#'/'.join(fuck)


# In[18]:


b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)

print(a)


# In[25]:


sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

last= sports.index()
print(last)


# In[3]:


for name in ['zuri' + 'joe' + 'lee']:
    print(name.count('e'))


# In[4]:


for char in 'LMao':
    print(char)


# In[7]:


for idx in range (4): 
    Square=idx*idx
print(Square)


# In[2]:


for name in ['Joe', 'Xi', 'Ben']:
    print(name + ",let's come to my house tonight.")


# In[3]:


print("This will execute first")

for _ in range(3):
    print("This line will execute three times")
    print("This line will also execute three times")

print("Now we are outside of the for loop!")


# In[4]:


print("This will execute first")

for _ in [0,1,2]:
    print("This line will execute three times")
    print("This line will also execute three times")

print("Now we are outside of the for loop!")


# In[ ]:


import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()


# In[1]:


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
print(accum)


# In[2]:


#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = range(1,11)
accum = 0
for w in nums:
    accum = accum + w
print(accum)


# In[3]:


print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))

# Note: `range` function is already casted as `list` in the textbook
print(range(5))


# In[4]:


accum = 0
for w in range(11):
    accum = accum + w
print(accum)

# or, if you use two inputs for the range function

sec_accum = 0
for w in range(1,11):
    sec_accum = sec_accum + w
print(sec_accum)


# In[6]:


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for w in nums:
    count = count + 1
print(count)


# In[7]:


numbers = range(0,41) 
print(list(numbers)) 
sum1 = 0
for w in numbers: 
    sum1= sum1 + w
print(sum1) 


# In[8]:


numbers = range(0,41) 
print(list(numbers)) 
for w in numbers: 
    sum1=0
    sum1= sum1 + w
print(sum1) 


# In[2]:


str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs = 0 
for i in str1: 
    numbs += 1
print(numbs) 


# In[4]:


str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."


# In[6]:


s = 'Python'
print(len(s))


# In[7]:


s = "python"
for idx in range(len(s)):
   print(s[idx % 2])


# In[11]:


if __name__ == '__main__':
    n = int(raw_input().strip())
n>=1, n<=100
s= n%2
if s>0: 
    print('Weird')
if s = 0 and range(2,6):
    print("Not Weird")
if s= 0 and range(6,21):
    print("Weird")
if s= 0 and range(>21):
    print("Not Weird")


# In[ ]:


#Hackerrank Q2 (1st attempt)
if __name__ == '__main__':
    n = int(raw_input().strip())
n>=1, n<=100
s= n%2
if s>0: 
    print(n, 'Weird')
if (s = 0) and (range(2,5)):
    print(n, "Not Weird")
if (s= 0) and (range(6,20)):
    print(n, "Weird")
if (s= 0) and (range(>20)):
    print(n, "Not Weird")


# In[12]:


#Hackerrank Q2 (Correct)
import= random 

n=random.random() 
print(n)
     
if (n%2!=0) or (n>=6 and n<=20): 
    print("Weird")
    
else:
    print("Not Weird")


# In[13]:


print(3//5)


# In[8]:


numbers = [1 ,2, 3, 4, 5]
a= numbers.append(6)
numbers


# In[13]:


numbers = [1 ,2, 3, 4, 5]
a= numbers.append(6)
numbers


# In[32]:


numbers = list(range(21))
numbers.append(21)
numbers


# In[33]:


arr = [1,2,2,3,4,5]
arr.remove(2)
print(arr)


# In[17]:


import requests
import io
import datetime
import pandas as pd

dfs={}

tickers = ['0001.HK']

for ticker in tickers:
    now = int(datetime.datetime.now().timestamp())+86400
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + ticker + "?period1=0&period2=" + str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"
    response = requests.get(url)
    file = io.StringIO(response.text)
    dfs[ticker] = pd.read_csv(file, index_col='Date')
    dfs['0001.HK']


# In[1]:


import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2021,1,1)
end = dt.datetime(2021,4,7)

df = web.DataReader('^hsi', 'yahoo', start, end)
print (df.head())
df.to_csv('hsidata.csv')


# In[ ]:


import pandas_datareader.data as web
from datetime import datetime 
import pandas as pd 


start = datetime (2020,1,1)
end = datetime (2020,7,31)
stock = 'GOOG'

df = web.DataReader(stock,'yahoo',start,end)
df.to_excel(f'stockdata_{stock}.xlsx')


# In[6]:


pins = ['song', 'dress', 'fake']

for pin in pins: 
    print(pin)


# In[10]:


formulas = ['slope', 'x-axis', 'y-axis']

for formula in formulas:
    print (formula)


# In[24]:


addition_str = "2+5+10+20"

for sum_val in addition_str: 
    print(list(sum_val))
    sum_val.remove('+')
    print(list(sum_val))
    


# In[37]:


original_str = "The quick brown rhino jumped over the extremely lazy fox"

original_list = list(original_str.split())
num_words_list = []
for i in original_list:
    num_words_list.append((len(i)))

print(num_words_list)


# In[38]:



lett = ''
for i in range(7):
    lett += 'b'
    print(lett, end='')


# In[43]:


lett = ''
for i in range(7):
    lett += 'b'
    print(lett, end='')
    print(len(lett))


# In[40]:


lett = ' '
for i in range(7):
    lett = 'b'*7
print(lett)


# In[6]:


week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f_list = list(week_temps_f.split(','))
print(week_temps_f_list)

a=0 
for i in week_temps_f_list:
    print(float(i))
    a += float(i)

print(a)
avg_temp = a / 7 
print(avg_temp)
#avg_temp = i/ 7 
#print(avg_temp)


# In[13]:


str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.
for a in str_list:  
    print
    i = (str(len(a)))
print(i)


# In[5]:


percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]

resps = [] 
for items in percent_rain: 
    percent_rain_list = float(items)
    if items > 90: 
        resps.append('Bring an umbrella.') 
    elif items > 80: 
        resps.append('Good for the flowers?')
    elif items > 50: 
        resps.append('Watch out for clouds!')
    else: 
        resps.append('Nice day!')


# In[20]:


words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for item in words: 
    if item[len(item)-1] == 'e': 
        item = item + 'd'
    else: 
        item = item + 'ed'
    past_tense.append(item)
print(past_tense)


# In[31]:


rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
x=0 
rainfall_mi_list = list(rainfall_mi.split(','))
print(rainfall_mi_list)
for inches in rainfall_mi_list: 
    a= float(inches)
    if a > 3.0: 
        x+=1
num_rainy_months = x     
print(num_rainy_months)


# In[43]:


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
x = 0
sentence_list = list(sentence.split(' '))
print(sentence_list)
# Write your code here.
for item in sentence_list: 
    a = str(item[0])
    b = str(item[len(item)-1])
    if a==b :
        x += 1 
same_letter_count = x 
print(same_letter_count)


# In[42]:


a = 'aba'
print(a[0])


# In[61]:


items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
x = 0

for item in items:  
    if 'w' in item: 
        x += 1
        
acc_num = x 
print(acc_num)


# In[67]:


sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
a=0
b=0
sentence_list = list(sentence.split(' ')) 
print(sentence_list)

for item in sentence_list: 
    if 'a' and 'e' in item: 
        a += 1
    if  'a' or 'e' in item: 
        b += 1
print(a)
print(b)
x = b-a
num_a_or_e = x 
        
print(num_a_or_e)


# In[74]:


sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
a = 0

sentence_list = list(sentence.split(' ')) 
print(sentence_list)

for item in sentence_list: 
    if 'a' in item or 'e' in item: 
        a += 1

num_a_or_e = a
        
print(num_a_or_e)


# In[81]:


s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
s_list = list(s.split(' ')) 
print(s_list)

x = 0
for item in s_list : 
    if item in vowels: 
        x += 1
num_vowels = x


# In[ ]:


s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
 
x = 0
for item in s: 
    if item in vowels: 
        x += 1
num_vowels = x


# In[2]:


a = 'apple'
b = 'apple' 

print(id(a))
print(id(b))


# In[4]:


winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
winners.sort(reverse=True)
z_winners = winners
print(z_winners)


# In[1]:


numbs = [5, 10, 15, 20, 25]
for i in range(len(numbs)):
    numbs[i]=numbs[i]+5
print(numbs)


# In[2]:


s = input("Enter some text")
ac = ""
for c in s:
    ac = ac + c + "-" + c + "-"

print(ac)


# In[3]:


output = ''

for i in range(35): 
    output = output + 'a' 
print(output) 


# In[4]:


colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Purple", "Pink", "Brown", "Teal", "Turquois", "Peach", "Beige"]

for position in range(len(colors)):
    color = colors[position]
    print(color)
    if color[0] in ["P", "B", "T"]:
        del colors[position]

print(colors)


# In[12]:


colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Purple", "Pink", "Brown", "Teal", "Turquois", "Peach", "Beige"]

print(len(colors))
for i in range(len(colors)):
    color = colors[i]
    print(color)
    if color[0] in ["P", "B", "T"]:
        del colors[i]

print(colors)


# In[7]:


len(colors) 


# In[10]:


print(len('Friday'))


# In[16]:


scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
y = list(scores.split(' '))
x = 0
for i in range(len(y)):
    y[i] = int(y[i])
    if y[i] >= 90:
        x += 1
        
a_scores = x 
print(a_scores)


# In[35]:


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ' '
a = list(org.split(' '))
for i in a: 
    if i not in stopwords: 
        acro = acro + i[0].upper()
        
print(acro)



# In[33]:


inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for i in inventory: 
    i = i.split(',')
    str1 = 'The store has{} {}, each for{} USD.'
    str2 = str1.format(i[1], i[0], i[2])
    print(str2)


# In[27]:


p_phrase = "was it a car or a cat I saw"

r_phrase = p_phrase[::-1]


# In[47]:


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ''
a = sent.split(' ') 
for i in a: 
    if i not in stopwords: 
        acro = acro + i[0:2].upper() + '.' 
if acro[-1] == '.' : 
    print(acro[0:-1])


# In[50]:


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ''
a = sent.split(' ') 
for i in a: 
    if i not in stopwords: 
        acro = acro + i[0:2].upper() + '. ' 
if acro[-1] == ' ' : 
    print(acro[0:-2])


# In[52]:


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

stopwords = set(w.upper() for w in stopwords)
acro = ''.join(i[0] for i in org.upper().split(' ') if i not in stopwords)
print(acro)


# In[53]:


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro = '. '.join(word[:2].upper() for word in sent.split() if word not in stopwords)
print(acro)


# In[60]:


ael = "python!"
ael_list = list(ael) 
app = ael_list
print(app)


# ael = "python!"
# print(split(ael))

# In[61]:


ael = "python!"
print(split(ael))


# In[2]:


#CSV File 
BC = [('Tom, 31, Swimming'), ('Alex, 18, Judo'), ('Philip, 19, 100 metres' )]

head = 'Name,Age,Event'
print(head)
for items in BC: 
    show = '{}, {}, {}'.format(BC[0], BC[1], BC[2])
    print(show)


# In[4]:


#CSV File 
BC = [('Tom', 31, 'Swimming'), ('Alex', 18, 'Judo'), ('Philip', 19, '100 metres' )]

head = 'Name,Age,Event'
print(head)
for items in BC: 
    show = '{}, {}, {}'.format(items[0], items[1], items[2])
    print(show)


# In[6]:


#Writing CSV File 
BC = [('Tom', 31, 'Swimming'), ('Alex', 18, 'Judo'), ('Philip', 19, '100 metres' )]

outfile = open('testing.txt','w')
outfile.write('Name,Age,Event')
outfile.write('\n')

for items in BC: 
    show = '{}, {}, {}'.format(items[0], items[1], items[2])
    outfile.write(show)
    outfile.write('\n') 
    
outfile.close()


# In[9]:


Can = [('Name', 'Age', 'Sex')]

for items in Can: 
    print(','.join([items[0],items[1],items[2]])


# In[10]:


olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()


# In[ ]:


olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

