from datetime import datetime

def greet():
    print("Bot: Hello! Nice to meet you.")

def tell_name():
    print("Bot: My name is DecodeBot. I am a rule-based chatbot.")

def show_help():
    print("""
Bot: Available Commands:
- hello / hi / hey
- good morning / good evening
- what is your name / who are you
- time / what time is it
- date / today's date
- joke / tell me a joke
- thanks / thank you
- bye / exit / quit
""")

def say_thanks():
    print("Bot: You're welcome!")

def tell_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Bot: Current time is", current_time)

def tell_date():
    current_date = datetime.now().strftime("%d/%m/%Y")
    print("Bot: Today's date is", current_date)

def tell_joke():
    print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

def unknown():
    print("Bot: Sorry, I don't understand that. Type 'help' to see commands.")


commands = {
    "hello": greet,
    "hi": greet,
    "hey": greet,
    "good morning": greet,
    "good evening": greet,

    "what is your name": tell_name,
    "who are you": tell_name,

    "help": show_help,
    "commands": show_help,

    "thanks": say_thanks,
    "thank you": say_thanks,

    "time": tell_time,
    "what time is it": tell_time,

    "date": tell_date,
    "today's date": tell_date,
    "what is today's date": tell_date,

    "joke": tell_joke,
    "tell me a joke": tell_joke
}

exit_commands = ["bye", "exit", "quit"]

print("Bot: Hello! I am DecodeBot.")
print("Bot: Type 'help' to see what I can do.")

while True:
    user_input = input("You: ")

    user_input = " ".join(user_input.lower().split())

    if user_input in exit_commands:
        print("Bot: Goodbye!")
        break

    command_function = commands.get(user_input, unknown)
    command_function()