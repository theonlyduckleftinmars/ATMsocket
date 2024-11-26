# Name: Jose Hernandez
# UAID: 010950132

import socket

# client.py

def run_client():
    host = "localhost"
    port = 9800

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        print("\nMenu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            amount = input("Enter amount to deposit: ")
            try:
                amount = float(amount)
                if amount > 0:
                    client_socket.send(f"DEPOSIT {amount:.2f}".encode())
                else:
                    print("Invalid amount. Please enter a positive number.")
                    continue
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue
        elif choice == "2":
            amount = input("Enter amount to withdraw (or type 'all' to withdraw all money): ")
            if amount.lower() == "all":
                client_socket.send("WITHDRAW ALL".encode())
            else:
                try:
                    amount = float(amount)
                    if amount > 0:
                        client_socket.send(f"WITHDRAW {amount:.2f}".encode())
                    else:
                        print("Invalid amount. Please enter a positive number.")
                        continue
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
                    continue
        elif choice == "3":
            client_socket.send("BALANCE".encode())
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        response = client_socket.recv(1024).decode()
        print(response)

    client_socket.close()

if __name__ == "__main__":
    run_client()
