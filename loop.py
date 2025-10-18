# ~ magicians = ['alice','david','carolina']
# ~ for magician in magicians:
    # ~ print(f"{magician.title()},that was a great trick!")
    # ~ print(f"I can't wait to see your next trick,{magician.title()}\n")
# ~ print(f"\nThank you,everyone.That was a great magic show!")

# ~ for value in range(1,5):
    # ~ numbers=list(range(1,5))
# ~ print(numbers)

# ~ even_numbers = list(range(2,11,2))
# ~ print(even_numbers)

# ~ squares = []
# ~ for value in range(1,11):
    # ~ squares.append(value ** 2)
# ~ print(squares)

# ~ digits=list(range(1,10))
# ~ digits.append(0)
# ~ print(digits)
# ~ print(min(digits))
# ~ print(max(digits))
# ~ print(sum(digits))

# ~ squares=[value ** 2 for value in range(1,10)]
# ~ print(squares)

players =['charles','martina','michael','florence','eli']
print("Here are my first three players on my team:")
for player in players[:3]:
    print(player)

#   元组
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
dimensions[0]=250   #   元组元素不可修改
    
