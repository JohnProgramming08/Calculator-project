import customtkinter as ctk


class BackEnd():
  #creates initial variables needed for calculations
  def __init__(self):
    self.number1 = 0
    self.number2 = 0
    self.answer = 0
    self.operator = ""
    self.number1_status = False

  #adds the number to the entry widget
  def number_click(number, entry_widget):
    entry_widget.insert(ctk.END, number)

  #performs calculations after both numbers have been entered
  def operator_click(self, operator, entry_widget):
    #only changes value of number1 if it hasn't been changed yet
    if self.number1_status == False:
      try:
        self.number1 = float(entry_widget.get())
        self.number1_status = True
        entry_widget.delete(0, ctk.END)

      except:
        entry_widget.delete(0, ctk.END)
        entry_widget.insert(0, "Error, you must enter a number")
    
    #sets everything up to be calculated
    match operator:
      case "+":
        self.operator = "+"
    
      case "-":
        self.operator = "-"
        
      case "x":
        self.operator = "x"

      case "÷":
        self.operator = "÷"

      case "=":
        try:
          self.number2 = float(entry_widget.get())
          self.calculate(self.number2)
          entry_widget.delete(0, ctk.END)
          entry_widget.insert(ctk.END, self.answer)
          self.number1_status = False

        except:
          entry_widget.delete(0, ctk.END)
          entry_widget.insert(0, "Error, you must enter a number")

  #performs the calculation based on the operator chosen
  def calculate(self, number2):
    match self.operator:
      case "+":
        self.answer = self.number1 + number2

      case "-":
        self.answer = self.number1 - number2

      case "x":
        self.answer = self.number1 * number2

      case "÷":
        try:
          self.answer = self.number1 / number2

        except:
          self.answer = "Error, cannot divide by 0"

  #deletes last character in entry_widget
  def back(self, entry_widget):
    current_value = entry_widget.get()
    new_value = current_value[:-1]
    entry_widget.delete(0, ctk.END)
    entry_widget.insert(0, new_value)

  #deletes all characters in entry_widget
  def clear(self, entry_widget):
    entry_widget.delete(0, ctk.END)