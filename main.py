# Calculate sum a, b
def sum(a, b):
  return a + b

def check_divide_by_zero(number):
  if (number == 0):
    return False
  else:
    return True

def divide(a, b):
  if (b != 0):
    return a / b
  else:
    return None


if __name__ == "__main__":
  print(f"Total : {sum(1, 2)}")
