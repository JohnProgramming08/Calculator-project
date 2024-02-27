import customtkinter as ctk


class Display():
  #sets up the initial root window
  def __init__(self):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    self.root = ctk.CTk()
    self.root.title("Basic Calculator")
    self.root.geometry("300x425")

  #sets up all the frames needed
  def frames(self):
    self.number_frame = ctk.CTkFrame(self.root)
    self.number_frame.grid(row = 2, column = 0)
    
    self.operation_frame = ctk.CTkFrame(self.root)
    self.operation_frame.grid(row = 2, column = 1)

  #sets up the entry widget
  def entry(self):
    self.entry_widget = ctk.CTkEntry(self.root, width = 300)
    self.entry_widget.grid(row = 0, column = 0, columnspan = 2)
    self.empty_row = ctk.CTkLabel(self.root, text = "")
    self.empty_row.grid(row = 1, column = 0)

  #sets up the number buttons
  def number_buttons(self, click):
    grid_positions = [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2),
        (3, 1)
    ]

    for i in range(10):
        row, column = grid_positions[i]
        self.number_button = ctk.CTkButton(self.number_frame, text = str(i), width = 50, height = 50, command = lambda: click(i, self.entry_widget))
        self.number_button.grid(row = row, column = column, padx = 10, pady = 10)
        self.number_button.configure(command = lambda number=i: click(number, self.entry_widget))
      
  #sets up the operator buttons
  def operator_buttons(self, click):
    self.addition_button = ctk.CTkButton(self.operation_frame, text = "+", width = 50, height = 35, command = lambda: click("+", self.entry_widget))
    self.addition_button.grid(row = 0,  column = 0, padx = 10, pady = 10)

    self.subtraction_button = ctk.CTkButton(self.operation_frame, text = "-", width = 50, height = 35, command = lambda: click("-", self.entry_widget))
    self.subtraction_button.grid(row = 1, column = 0, padx = 10, pady = 10)

    self.multiplication_button = ctk.CTkButton(self.operation_frame, text = "X", width = 50, height = 35, command = lambda: click("x", self.entry_widget))
    self.multiplication_button.grid(row = 2, column = 0, padx = 10, pady = 10)

    self.division_button = ctk.CTkButton(self.operation_frame, text = "÷", width = 50, height = 35, command = lambda: click("/", self.entry_widget))
    self.division_button.grid(row = 3, column = 0, padx = 10, pady = 10)

    self.equal_button = ctk.CTkButton(self.operation_frame, text = "=", width = 50, height = 35, command = lambda: click("=", self.entry_widget))
    self.equal_button.grid(row = 4, column = 0, padx = 10, pady = 10)

  def remove_buttons(self, click, click2):
    self.back_button = ctk.CTkButton(self.number_frame, text = "BACK", width = 50, height = 50, command = lambda: click(self.entry_widget))
    self.back_button.grid(row = 3, column = 0, padx = 10, pady = 10)

    self.clear_button = ctk.CTkButton(self.number_frame, text = "CLEAR", width = 50, height = 50, command = lambda: click2(self.entry_widget))
    self.clear_button.grid(row = 3, column = 2, padx = 10, pady = 10)