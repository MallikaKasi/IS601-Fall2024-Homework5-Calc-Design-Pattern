import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
import multiprocessing
#from dotenv import load_dotenv
import os



class App:
    def __init__(self):
        self.command_handler = CommandHandler()
   
    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue

        #self.command_handler.register_command("menu", MenuCommand(self.command_handler))


            
    def start(self):
        self.load_plugins()
        print("\nOption To Perform Interative Calculation:")
        print("        ")

        print("Type A. To Perform Add")
        print("Type S. To Perform Subtract")
        print("Type M. To Perform Multiply")
        print("Type D. To Perform Divide")
        print("Type E. To Exit")
        choice = input("Choose an option : ")
        while True:
            try:
                if choice == 'C':
                    print("Type A. To Perform Add")
                    print("Type S. To Perform Subtract")
                    print("Type M. To Perform Multiply")
                    print("Type D. To Perform Divide")
                    print("Type E. To Exit")
                    choice = input("Choose an option : ")
                    continue
                elif choice == 'A':
                    self.command_handler.load_plugin('Add')
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                    Add_command = self.command_handler.create_command('Add', a, b)
                    result = self.command_handler.execute_command('Add')
                elif choice == 'S':
                    self.command_handler.load_plugin('Subtract')
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                    Subtract_command = self.command_handler.create_command('Subtract', a, b)
                    result = self.command_handler.execute_command('Subtract')
                elif choice == 'M':
                    self.command_handler.load_plugin('Multiply')
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                    Multiply_command = self.command_handler.create_command('Multiply', a, b)
                    result = self.command_handler.execute_command('Multiply')
                elif choice == 'D':
                    self.command_handler.load_plugin('Divide')
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                    Divide_command = self.command_handler.create_command('Divide', a, b)
                    result = self.command_handler.execute_command('Divide')
                elif choice == 'E':
                    self.command_handler.load_plugin('exit')
                    exit_command = self.command_handler.create_command('exit')
                    result = self.command_handler.execute_command('exit')
                else:
                    print("Invalid choice. Please select a valid option.")
            except ZeroDivisionError:
                print("Error: Division by zero.")
            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"An error occurred: {e}")
            print("Type C : to Continue , Type E : to Exit  ")

            choice = input("")


def start_app():
    app = App()
    app.start()

if __name__ == "__main__":
    multiprocessing.Process(target=start_app).start()