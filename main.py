letter_value = {
  "A":10,"a":10,
  "B":11,"b":11,
  "C":12,"c":12,
  "D":13,"d":13,
  "E":14,"e":14,
  "F":15,"f":15,
  "G":16,"g":16,
  "H":17,"h":17,
  "I":18,"i":18,
  "J":19,"j":19,
  "K":20,"k":20,
  "L":21,"l":21,
  "M":22,"m":22,
  "N":23,"n":23,
  "O":24,"o":24,
  "P":25,"p":25,
  "Q":26,"q":26,
  "R":27,"r":27,
  "S":28,"s":28,
  "T":29,"t":29,
  "U":30,"u":30,
  "V":31,"v":31,
  "W":32,"w":32,
  "X":33,"x":33,
  "Y":34,"y":34,
  "Z":35,"z":35
}

def base_to_decimal(number, base):
  result = 0
  validity = 0
  for x in number:
    if x == ".":
      continue
    if x in letter_value:
      if letter_value[x] > validity:
        validity = letter_value[x]
        continue
    if x not in letter_value:
      if int(x) > validity:
        validity = int(x)
  if validity + 1 > base:
    return "Input Out Of Base"
  if base > 36:
    return "Not A Base"
  if "." in number:
    for index_dot in range(len(number)):
      if number[index_dot] == ".":
        break
    left_from_dot = number[0:index_dot]
    right_from_dot = number[index_dot + 1:len(number)]
    reverse_left_from_dot = left_from_dot[::-1]
    for q in range(len(left_from_dot)):
      if reverse_left_from_dot[q] in letter_value:
        result = result + base**q*letter_value[reverse_left_from_dot[q]]
        continue
      result = result + base**q*int(reverse_left_from_dot[q])
    for o in range(len(right_from_dot)):
      if right_from_dot[o] in letter_value:
        use_for_a_number = - o - 1
        result = result + base**use_for_a_number*letter_value[right_from_dot[o]]
        continue
      use_for_a_number = - o - 1
      result = result + base**use_for_a_number*int(right_from_dot[o])
    return result
  reverse_number = number[::-1]
  for i in range(len(number)):
    if reverse_number[i] in letter_value:
      result = result + base**i*letter_value[reverse_number[i]]
      continue
    result = result + base**i*int(reverse_number[i])
  return result

number_value = {
  10:"A",
  11:"B",
  12:"C",
  13:"D",
  14:"E",
  15:"F",
  16:"G",
  17:"H",
  18:"I",
  19:"J",
  20:"K",
  21:"L",
  22:"M",
  23:"N",
  24:"O",
  25:"P",
  26:"Q",
  27:"R",
  28:"S",
  29:"T",
  30:"U",
  31:"V",
  32:"W",
  33:"X",
  34:"Y",
  35:"Z"
}

def decimal_to_base(number, base):
  keeper = []
  processed_keeper = []
  was_double = 0
  for_was_double = 0
  result = ""
  if base > 36 or not(str(base).isdigit()):
    return "Not A Base"
  if "." in str(number):
    number = int(number*(base**10))
    was_double = 1
  while number != 0:
    highest_power = -1
    while number >= base**(highest_power + 1):
      highest_power = highest_power + 1
    number = number - (base**highest_power)
    keeper.append(highest_power)
  processed_keeper = [keeper.count(i) for i in range(keeper[0] + 1)]
  for i in range(len(processed_keeper)):
    if processed_keeper[i] >= 10:
      processed_keeper[i] = number_value[processed_keeper[i]]
  if was_double == 1:
    for i in processed_keeper:
      if for_was_double == 10:
        result = result + "."
      result = result + str(i)
      for_was_double = for_was_double + 1
    return result[::-1]
  for i in processed_keeper:
    result = result + str(i)
  return result[::-1]

print("----------------------------------------------------")
print("| These Calculators Can Handle Floats And Integers |")
print("| For All Bases (2 - 36)                           |")
print("| Letters Can Be In Uppercase or Lowercase         |")
print("----------------------------------------------------")
while 1 > 0:
  inside = False
  calculator = input("Type 'b-d' to convert any base to decimal or 'd-b' to convert decimal to any base: ")
  print(" ")
  if calculator == "b-d":
    while 1 > 0:
      user_input_number = input("Enter A Number In Any Base: ")
      user_input_base = input("Enter The Base The Number Is In: ")
      print(str(base_to_decimal(user_input_number,int(user_input_base))))
      print(" ")
      exit = input("Would You Like To Continue, type 'yes' or 'no': ")
      if exit == "no":
        inside = True
        break
      print(" ")
  if calculator == "d-b":
    while 1 > 0:
      user_input_numbers = input("Enter A Number In Decimal: ")
      user_input_bases = input("Enter The Base You Would Like To Convert It To: ")
      if "." in user_input_numbers:
        try:
          user_input_numbers = float(user_input_numbers)
        except ValueError:
          print("Number Not In Decimal")
          print(" ")
          continue
      else:
        try:
          user_input_numbers = int(user_input_numbers)
        except ValueError:
          print("Number Not In Decimal")
          print(" ")
          continue
      try:
          user_input_bases = int(user_input_bases)
      except ValueError:
        print("Not A Base")
        print(" ")
        continue
      print(decimal_to_base(user_input_numbers, user_input_bases))
      print(" ")
      exit = input("Would You Like To Continue, type 'yes' or 'no': ")
      if exit == "yes":
        print(" ")
        continue
      if exit == "no":
        inside = True
        break
      while exit != "yes" and exit != "no":
        inside = False
        print("Not An Input")
        print(" ")
        exit = input("Would You Like To Continue, type 'yes' or 'no': ")
        inside = True
      if inside == True:
        break
  if inside == False:
    print("Not An Input")
    continue
  print(" ")
