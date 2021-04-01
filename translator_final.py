import tkinter as tk

output_label = None

# ------ Functions -----
# Changes the dropdown options based on the chosen language
def change_function_to_be_translated_menu(*args):
  testvar = translate_from_language.get()
  if testvar == languages[0]:
    translated_function.set(python_functions[0])
    drop_menu2['menu'].delete(0, 'end')
    for item in python_functions.values():
      drop_menu2['menu'].add_command(label = item, command = tk._setit(translated_function, item))
  elif testvar == languages[1]:
    translated_function.set(java_functions[0])
    drop_menu2['menu'].delete(0, 'end')
    for item in java_functions.values():
      drop_menu2['menu'].add_command(label = item, command = tk._setit(translated_function, item))
  elif testvar == languages[2]:
    translated_function.set(javascript_functions[0])
    drop_menu2['menu'].delete(0, 'end')
    for item in javascript_functions.values():
      drop_menu2['menu'].add_command(label = item, command = tk._setit(translated_function, item))

# function that tells the button to execute the translation
def my_click():

  global output_label

  def get_key(dict, val):
    for key, value in dict.items():
      if val == value:
        return key
  # keeps track of the language menu to pull the translation from
  output_label.destroy()
  if translate_to_language.get() == languages[0]:
    translate_var = 0
  elif translate_to_language.get() == languages[1]:
    translate_var = 1
  elif translate_to_language.get() == languages[2]:
    translate_var = 2
  
  # Function to generate the output label
  def generate_label(dict):

    global output_label

    output_label.destroy()
    output_label = tk.Label(root, text = dict[key_var])
    output_label.grid(row = 6, column = 0)
    return output_label

  # keep track of the key value of the function selected in the second label
  if translate_from_language.get() == languages[0]:
    key_var = get_key(python_functions, translated_function.get())
    if translate_var == 0:
      generate_label(python_functions)
    elif translate_var == 1:
      generate_label(java_functions)
    elif translate_var == 2:
      generate_label(javascript_functions)
  elif translate_from_language.get() == languages[1]:
    key_var = get_key(java_functions, translated_function.get())
    if translate_var == 0:
      generate_label(python_functions)
    elif translate_var == 1:
      generate_label(java_functions)
    elif translate_var == 2:
      generate_label(javascript_functions)
  elif translate_from_language.get() == languages[2]:
    key_var = get_key(javascript_functions, translated_function.get())
    if translate_var == 0:
      generate_label(python_functions)
    elif translate_var == 1:
      generate_label(java_functions)
    elif translate_var == 2:
      generate_label(javascript_functions)
  



# ----- Language list options and language dictionaries -----
# Languages the user can pick from
languages = ['Python', 'Java', 'JavaScript']

# Dictionaries containing the supported functions and their languages
python_functions = {0: "print(x)", 1: "str(object)", 2: "list(string)", 3: "int(string)", 4: "min(num1, num2)", 5: "max(num1, num2)", 6: "type(object)", 7: "list.append(object)", 8: "pop(object)", 9: "len(list)", 10: "for item in list"}
java_functions = {0: "System.out.println(x)", 1: "object.toString()", 2: "string.toCharArray()", 3: "Integer.parseInt(string)", 4: "Math.min(num1, num2)", 5: "Math.max(num1, num2)", 6: "object.getClass().getName()", 7: "ArrayList.add(object)", 8: "ArrayList.remove(int ArrayList.size() - 1)", 9: "ArrayList.size()", 10: "for (int i = 0; i < ArrayList.size(); i++)"}
javascript_functions = {0: "console.log(x)", 1: "object.toString()", 2: "string.split(\" \")", 3: "parseInt(string)", 4: "Math.min(num1, num2)", 5: "Math.max(num1, num2)", 6: "typeof object", 7: "array.push(object)", 8: "array.pop()", 9: "array.length", 10: "for (let i = 0; i < array.length; i++)"}



# ----- Session setup and widgets -----
# set up the tkinter root session
root = tk.Tk()
root.columnconfigure(0, uniform = 'column')
root.columnconfigure(1, uniform = 'column')
root.columnconfigure(2, uniform = 'column')

# Creates translate_from label and dropdown menu
translate_from_language = tk.StringVar()
translate_from_language.set(languages[0])
translate_from_label = tk.Label(root, text = "Translate From")
translate_from_label.grid(row = 0, column = 0)
translate_from_drop_menu = tk.OptionMenu(root, translate_from_language, *languages)
translate_from_drop_menu.grid(row = 1, column = 0)

# Creates translate_to label and dropdown menu
translate_to_language = tk.StringVar()
translate_to_language.set(languages[0])
translate_to_label = tk.Label(root, text = "Translate To")
translate_to_label.grid(row = 0, column = 2)
translate_to_drop_menu = tk.OptionMenu(root, translate_to_language, *languages)
translate_to_drop_menu.grid(row = 1, column = 2)

# Creates the function_to_be_translated label and dropdown menus
translated_function = tk.StringVar()
translated_function.set(python_functions[0])
second_label = tk.Label(root, text = "Choose a function")
second_label.grid(row = 2, column = 1)  
drop_menu2 = tk.OptionMenu(root, translated_function, *python_functions.values())
drop_menu2.grid(row = 3, column = 1)
# Implements the change_function_to_be_translated_menu function when the value in the first dropdown menu is changed
translate_from_language.trace('w', change_function_to_be_translated_menu)

# Creates the initilize button to get the translated function
translate_button = tk.Button(root, text = "Translate", command = my_click)
translate_button.grid(row = 4, column = 1)

# Output section
output = tk.Label(root, text = "Output")
output.grid(row = 5, column = 0)
output_label = tk.Label(root, text = ' ')
output_label.grid(row = 6, column = 0)


# ------------------------------------------------------------------------------------ #
# Runs the program
root.mainloop()