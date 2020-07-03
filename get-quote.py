import random
#random is a module from Python that allow me to select a random item inside an array 
#remember to not import modules inside of a function 
def Itiswhatitis():
  print("Keep it logically awesome.")

  #Remember to always change the name of the function at the beginning and at the end.
  #Comment everything. in that ways you can learn faster beign able to remember the different definitions every time you are working with you code.  Andy Matuschak and  Michael Nielsen work about SRS inside the documents that your are working on.

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  #That allow me to update automatically the RND the number of variables inside my array.
  rnd = random.randint(0, last)
  
  print(quotes[rnd], quotes[rnd], quotes[rnd], sep="\n")  
  #When you want to look for a specific items inside an array, use the [] modifier to tell Python that you are looking for an specific item inside the array.  
  #Remember that arrays always start at 0, so take it into account when you are lloking for an specific line
if __name__== "__main__":
  Itiswhatitis()

