# Name: Jose Hernandez
# UAID: 010950132

import socket

class ATMServer:
    def __init__(self, host="localhost", port=9800):
        self.balance = 100  # Start balance
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Server started and listening on {}:{}".format(self.host, self.port))

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            command, *params = data.split()
            if command == "DEPOSIT":
                amount = float(params[0])
                if amount > 0:
                    self.balance += amount
                    response = f"Deposit successful. New balance: ${self.balance:.2f}"
                else:
                    response = "Invalid deposit amount."
            elif command == "WITHDRAW":
                if params[0].lower() == "all":
                    self.balance = 0
                    response = "All money withdrawn. New balance: $0.00"
                else:
                    amount = float(params[0])
                    if amount > 0 and self.balance >= amount:
                        self.balance -= amount
                        response = f"Withdrawal successful. New balance: ${self.balance:.2f}"
                    elif amount > 0:
                        response = "Insufficient balance."
                    else:
                        response = "Invalid withdrawal amount."
            elif command == "BALANCE":
                response = f"Current balance: ${self.balance:.2f}"
            else:
                response = "Unknown command."

            client_socket.send(response.encode())

    def run(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print("Connection established with: {}".format(addr))
            self.handle_client(client_socket)
            client_socket.close()
            print("Connection closed with: {}".format(addr))

if __name__ == "__main__":
    atm_server = ATMServer()
    atm_server.run()
