# Programma Nerdle per trovare 3 cifre diviso 2 cifre = 1 cifra

from xml.etree.ElementTree import tostring
import math


def toString(List):
    return ''.join(List)


def allLexicographicRecur (string, data, last, index,res):
    length = len(string)

    for i in range(length):

        data[index] = string[i]

        if index==last:
            res.append(toString(data))
        else:
            allLexicographicRecur(string, data, last, index+1,res)

def allLexicographic(string,num,res):
    length = num

    data = [""] * (length+1)

    string = sorted(string)

    allLexicographicRecur(string, data, length-1, 0,res)

def divisors(num):
    div=[]
    for i in range(1,num+1):
        if(num%i==0):
            div.append(i)
    return div

def exclude(candidato,excludelist):
    for i in range(len(excludelist)):
        if(candidato.find(excludelist[i])!=-1):
            return True
    return False


# SETTA QUI I PARAMETRI
# in cifre mettere le cifre che si sanno del numero a 3 cifre, poi lui calcolerà le permutazioni
cifre = [3,4,6,9,8]
#cifre che sai che non ci sono (se lasciata vuota, assume che siano quelle che mancano dalla stringa precedente)
excludelist=[]
l=3 #lunghezza (in questo caso 3 cifre #TODO- implementare anche 2 cifre e 2 cifre)





res=[]
allcifre=[0,1,2,3,4,5,6,7,8,9]
if(len(excludelist)==0):
    excludelist=[ele for ele in allcifre if ele not in cifre]
string=''.join([str(x) for x in cifre])
excludelist=''.join([str(x) for x in excludelist])
print(string)
allLexicographic(string,l,res)
for j in range(len(res)):
    t=divisors(int(res[j]))
    lungh=len(t)
    met=int(lungh/2)
    print(str(res[j]),end="= ")
    for o in range(lungh):
        if(o<met):
            if(not (len(str(t[o]))>1 or len(str(t[lungh-(o+1)]))>2)):
                candidato= str(t[o])+","+str(t[lungh-(o+1)])
                if(not exclude(candidato,excludelist)):
                    print(candidato,end=" ; ")
    print(" ")

# This code is contributed to Bhavya Jain
