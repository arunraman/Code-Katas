a = ['1','2','3','4','5','6','7','8','9']

def circular_counter(int_list, skip):
  skip = skip - 1 # list starts with 0 index
  idx = 0
  while len(int_list)>0:
      idx = (skip+idx)%len(int_list) # hashing to keep changing the index to every 3rd
      print int_list.pop(idx)


circular_counter(a,3)