# -*- coding: utf-8 -*-
"""vigenere.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mB5ws-P3J9-BGiphamOCqtDTQNbjrT73
"""

import matplotlib.pyplot as plt
import numpy as np
#guess the length of the key
l = 7
#example encrypted text
text = 'PZAXGYJAKNTVMJLIVXXBKKEXYIFAJFAHRCYJAVFYHEJMCBSHDHHNMVUJZRXKQYZVGALSWE\
LFHFSMPCUBBFFUIKNGEVHPZPNFCMBUCHYMZPSRMEFYVYVNRCYHFRHRMWUPOTGCHPFJMMHC\
IDXTHYYVYVXVWAHEBNGBEAUBBQJKYFJGXZKYADKKFKIMUXGIJVYHTRXKBDWTXCKUMULIWQ\
YUCRXIDHHNLXLKUSNGGLUWFRHRMPHZMTVXOATNWIPASAYFIHPHZMKSVQZFJWSJPPAWHJMP\
YAWZIHYYKYMMIJPEJDISPVAUMSMAJGAXGIITQAVIUJKFATHYOHRNZYUNKBABZUPLUWYSLI\
HFRHRJNVYXMIZNLQNQTLAZERHRUJKMBLSWEHFRHRUJKECKIHCATNGGSXLDBXGONPFHMLYZ\
LBJKXGAUFRLSHPOQOKSHPSUWXWIBATNYMADAMPTMHOAOHUILYYUVXEHZDQTGSQBPDBMLUJ\
KFQXHUIHSNMLUPJMWUIWWBENWFSPOABXABKLJYESCPCGUGILWIXNTRXEUENVYLAZKBMIGO\
DQBNTJKYFJGHYJJADKEAAATNNWYKMENVYLAUQCPSLGZFXIVYRLZCVCVAYFQKIUPZFXHYLY\
YUCBGUHUMCBSHWSUWYVUOADDVXONLADKMHPLXUXGNQHXYKSJAYFHTRXKBDMTXUOVMBMSJN\
VYXMIIQYAEXVUHSEJYINUHYNKMWWUORMMTAUELTVYZLQYECUXVGCIVCRHOHTRXNPSQMPSO\
VYJGCWKTBJGMYOOMEXFYAUDNLTIJKUWZXIWTMADINZLYJGHZKYBAHHOYAEJGHMAYHRVIMP\
OMCIVIPLOCMLYLYUETGSWUPBXGONPFHHJNDLUAVYMPVYNKWNDPEQTWAAUQATXYZWABBXCR\
LUWGSPWAUXGXBWATJLFYAUOANGCWSFXMLYZPSRMEFAJAWHQSSLFXHGUNLMKHYNPOQBXMGL\
VDCTRNLYUWVMJHLERGHYAKUCBWIQYAKEMAWAUXGXIQWTXEHWECUUEMVAYFRXWCJJXDWMHC\
ATNKMADAFXIVCRHOHPIBWCQJEAUUZDNLTYYAQMMLYBBZMTQYJAMUKMADAAOIIILSQCHIHC\
HSNBRJNPHJMIWKTYDGMWWAUXGWLANMAWPYOZAOMLYILPRNQINAQLARIHVSHPLYPOQABXCO\
PZBMEHPTQBLEAAZFNQXMKYAUWJUOOUXGIXHLFCXVMYPFRSIHOOMEXXBAYUPAXNKJAVFYHE'

#using Kasiski examination to find the possible lengths of the key
patterns = []
lengths = []
divisors = []

for i in range(len(text)-l):
  if text.count(text[i:i+l]) > 1:
    patterns.append(text[i:i+l])

for i in patterns:
  if patterns.count(i) > 1:
    patterns.remove(i)

for i in patterns:
  lengths.append(text.rfind(i)-text.find(i)+l)

for i in range(min(lengths)):
  divisor = True;
  for length in lengths:
    if length%(i+1) != 0:
      divisor = False;
      break
  if divisor:
    divisors.append(i+1)
print(divisors)

#use one of the common divisors as a key length
kl = divisors[-1]
#using frequency analysis for each letter of the key to determine what the key is
rows_of_kl = []
while len(text) > 0:
  rows_of_kl.append(text[:kl])
  text = text[kl:]

alphabet = []
for i in range(ord('Z')-ord('A')+1):
  alphabet.append(0);

letters = []
for i in range(kl):
  letters.append(alphabet[:])

for i in rows_of_kl:
  for j in range(len(i)):
    letters[j][ord(i[j])-ord('A')] = letters[j][ord(i[j])-ord('A')] + 1

for i in range(len(letters)):
  x = []
  y = []
  for j in range(len(letters[i])):
    x.append(chr(j+ord('A')))
    y.append(letters[i][j])
  plt.bar(x,y)
  print("letter: " + str(i))
  plt.show()

text = 'PZAXGYJAKNTVMJLIVXXBKKEXYIFAJFAHRCYJAVFYHEJMCBSHDHHNMVUJZRXKQYZVGALSWE\
LFHFSMPCUBBFFUIKNGEVHPZPNFCMBUCHYMZPSRMEFYVYVNRCYHFRHRMWUPOTGCHPFJMMHC\
IDXTHYYVYVXVWAHEBNGBEAUBBQJKYFJGXZKYADKKFKIMUXGIJVYHTRXKBDWTXCKUMULIWQ\
YUCRXIDHHNLXLKUSNGGLUWFRHRMPHZMTVXOATNWIPASAYFIHPHZMKSVQZFJWSJPPAWHJMP\
YAWZIHYYKYMMIJPEJDISPVAUMSMAJGAXGIITQAVIUJKFATHYOHRNZYUNKBABZUPLUWYSLI\
HFRHRJNVYXMIZNLQNQTLAZERHRUJKMBLSWEHFRHRUJKECKIHCATNGGSXLDBXGONPFHMLYZ\
LBJKXGAUFRLSHPOQOKSHPSUWXWIBATNYMADAMPTMHOAOHUILYYUVXEHZDQTGSQBPDBMLUJ\
KFQXHUIHSNMLUPJMWUIWWBENWFSPOABXABKLJYESCPCGUGILWIXNTRXEUENVYLAZKBMIGO\
DQBNTJKYFJGHYJJADKEAAATNNWYKMENVYLAUQCPSLGZFXIVYRLZCVCVAYFQKIUPZFXHYLY\
YUCBGUHUMCBSHWSUWYVUOADDVXONLADKMHPLXUXGNQHXYKSJAYFHTRXKBDMTXUOVMBMSJN\
VYXMIIQYAEXVUHSEJYINUHYNKMWWUORMMTAUELTVYZLQYECUXVGCIVCRHOHTRXNPSQMPSO\
VYJGCWKTBJGMYOOMEXFYAUDNLTIJKUWZXIWTMADINZLYJGHZKYBAHHOYAEJGHMAYHRVIMP\
OMCIVIPLOCMLYLYUETGSWUPBXGONPFHHJNDLUAVYMPVYNKWNDPEQTWAAUQATXYZWABBXCR\
LUWGSPWAUXGXBWATJLFYAUOANGCWSFXMLYZPSRMEFAJAWHQSSLFXHGUNLMKHYNPOQBXMGL\
VDCTRNLYUWVMJHLERGHYAKUCBWIQYAKEMAWAUXGXIQWTXEHWECUUEMVAYFRXWCJJXDWMHC\
ATNKMADAFXIVCRHOHPIBWCQJEAUUZDNLTYYAQMMLYBBZMTQYJAMUKMADAAOIIILSQCHIHC\
HSNBRJNPHJMIWKTYDGMWWAUXGWLANMAWPYOZAOMLYILPRNQINAQLARIHVSHPLYPOQABXCO\
PZBMEHPTQBLEAAZFNQXMKYAUWJUOOUXGIXHLFCXVMYPFRSIHOOMEXXBAYUPAXNKJAVFYHE'

key = 'HMJTEUW'

def vigDecrypt(ciphertext, key):
    decrypted = ''
    for i, ch in enumerate(ciphertext):
        decrypted += unshiftLetter(ch, key[i % len(key)])
    return decrypted

def unshiftLetter(letter, keyLetter):
    letter = ord(letter) - ord("A")
    keyLetter = ord(keyLetter) - ord("A")
    new = (letter - keyLetter) % 26
    return chr(new + ord("A"))

print(vigDecrypt(text, key))