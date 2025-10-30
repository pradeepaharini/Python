def average():
  total = 0
  count = 0
  while True:
    user_input = input("Enter the number or else enter q to quit: ")
    if user_input.lower() == 'q':
      break
    try:
      number = float(user_input)
      total += number
      count += 1
      print(f"The current average is {total/count:.2f}")
    except ValueError:
      print("Invalid input. Try again by entering a number or q")
    if count > 0:
      print(f"The final average is {total/count:.2f}")
    else:
      print("No numbers were entered")
average()
