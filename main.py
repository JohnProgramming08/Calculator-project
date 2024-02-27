from display import Display
from back_end import BackEnd


if __name__ == "__main__":
  display = Display()
  display.frames()
  display.entry()
  back_end = BackEnd()
  display.number_buttons(BackEnd.number_click)
  display.operator_buttons(back_end.operator_click)
  display.remove_buttons(back_end.back, back_end.clear)
  display.root.mainloop()
