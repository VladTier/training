str = '{[([[[(} 2, 5 {]]](()'
def brackets_check(str):
   brackets = []
   map = {'(': ')', '[': ']', '{': '}'}
   for char in str:
        if char in map.keys():
          brackets.append(char)
        elif char in map.values():
          if map[brackets[-1]] == char:
            brackets.pop()
          else:
            return False
   return brackets
   return not len(brackets)  # 0 == True

print(brackets_check(str), brackets)
   
