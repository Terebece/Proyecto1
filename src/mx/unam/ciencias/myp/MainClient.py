import Client

def main():
    host = str(input("Enter host: "))
    port = int(input("Enter port: "))

    client = Client.Client(host, port)
    client.runClient()

if __name__ == '__main__':
    main()
