# Write a python programme to translate a messege into secret code language. Use the rules below to translate normal English into secret code language.

# Coding:

# if the word contains atleast 3 charecters, remove the first letter and append it at the end now append three random charecters at the starting and the end.
# else:
# Simply reverse the string

# Decoding:

# If the word contains less than three charecters, reverse it.
# else:
# Remove 3 random charecters from start and end . Now Remove the last letter and append it to the beginning.

import string
import random

st = input("Enter messege :- ")

def codeDecode(st):
    N = 3

    res = ''.join(random.choices(string.ascii_lowercase +  string.digits, k=N))
    res1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))

    words = st.split(" ")
    coding = input("Press 0 for coding or Press 1 for Decoding :- ")
    if(coding == "0"):
      coding = True
    elif(coding == "1"):
      coding = False
    if (coding):
      nwords = []
      for word in words:
        if (len(word) >= 3):
          # r1 = "hgs"
          # r2 = "uyp"
          stnew = str(res) + word[1:] + word[0] + str(res1);
          nwords.append(stnew)
        else:
          nwords.append(word[::-1])
      print(" ".join(nwords))

    else:
      nwords = []
      for word in words:
        if (len(word) >= 3):
          stnew = word[3:-3]
          stnew = stnew[-1] + stnew[:-1]
          nwords.append(stnew)
        else:
          nwords.append(word[::-1])
      print(" ".join(nwords))
  

# st = 0;
codeDecode(st)