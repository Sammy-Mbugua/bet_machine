import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count= {
    "A":2,
    "B":4,
    "C":6,
    "D":8,

}
symbol_value= {
    "A":5,
    "B":4,
    "C":3,
    "D":2,

}

def check_winnings(columns,bet,lines,values):
    winnings=0
    winning_lines= []
    for line in range (lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append( line + 1)
    return winnings,winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.item():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True:
        amount= input("Enter the amount you want to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("The value must be greater than 0.")
        else:
            print("Enter the number")

    return amount

def get_number_of_lines():
    while True:
        lines= input(
            "Enter the number of lines(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Enter the number of lines")

    return lines

def get_bet():
    while True:
        amount= input("Enter the amount you want to bet on each line? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The value must between {MIN_BET} - {MAX_BET}.")
        else:
            print("Enter the number")

    return amount


def main():
    balance=deposit()
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet > balance:
            print(f"you have insufficient funds.your balance is ${balance}")
        else:
            break
    print(f"your bettting with ${bet} on {lines}.the total bet is:${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines", *winning_lines)
main()
            
            