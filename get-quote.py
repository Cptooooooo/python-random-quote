import random
def foo():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  nf = open("quotes-copy.txt", "w")
  nf.writelines(quotes)

  print(quotes[random.randint(0, len(quotes)-1)], end="")

if __name__== "__main__":
  foo()
