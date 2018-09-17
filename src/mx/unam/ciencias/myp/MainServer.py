import sys
import Server

def main():
    if len(sys.argv) != 3:
        print("Correct usage:script, IP address, port number")
        exit()

    host = str(sys.argv[1])
    port = int(sys.argv[2])

    server = Server.Server(host, port)
    server.runServer()

if __name__ == '__main__':
    main()
