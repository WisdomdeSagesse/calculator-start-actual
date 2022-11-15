#addition
def add(n1, n2):
  return n1 + n2

#subtraction
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operators = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/": divide,
}
def read_string(prompt):
  operators_list = list(operators)
  result = input(prompt)
  if result not in operators_list:
    output = "wrong input"
    print(output)
  else:
    output = result
  return output



def calculator():
  num_one = float(input("What is the first number: "))
  for k,v in operators.items():
      print("".join(k))
  end_calc = False
  while not end_calc:
    symbol = read_string("Pick an operation symbol from the list above: ")
    if symbol == "wrong input":
      end_calc = True
      calculator()
    else:
      num_two = float(input("What is the next number: "))
      math_function = operators[symbol]
      answer = math_function(num_one, num_two)
      print(f"answer = {answer}")
      continue_calc = input(f"Enter 'y' to continue calculating with {answer} or 'n' to start a new " + 
                      "calculation or 'q' to quit ").lower()
      if continue_calc == 'y':
        num_one = answer
      elif continue_calc == 'n':
        end_calc = True
        calculator()
      elif continue_calc == 'q':
        end_calc = True

calculator()