def cat_twice(part1,part2):
    print("entering cat_twice")
    cat=part1+part2
    # call function : print_twice
    print_twice(cat)
    print("leaving cat_twice")    
def print_twice(apple):
    print("entering print_twice")
    print(apple)
    print(apple)
    print(print_twice.__name__)
    print("leaving print_twice")
print("program begin here !")
#  call  function : cat_twice
cat_twice('aaaa','bbbbb')
print("prgram ends !!!  bye ")