import socket

flag = True

while flag:
    # asking user for input
    answer = input('Do you want to provide url or ip address? (Type url for url or ip for ip address): ')

    if answer == "url":
        url = input('Please provide the url: ')
        # get ip address from user's input
        ip = socket.gethostbyname(url)
        # asking user for ports range
        portStart = int(input('Please provide starting port: '))
        portEnd = int(input('Please provide ending port: '))
        # create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(60)
        for port in range(portStart, portEnd + 1):
            result = s.connect_ex((ip, port))
            if result == 0:
                print('Port ' + str(port) + ' is open! Grapping banner...')
                # getting banner
                banner = s.recv(1024)
                print('The banner has been grapped! The banner is: ' + banner.decode('utf-8'))
            else:
                print('Port is not open!')
        # closes socket
        s.close()
        question = input('Do you want to provide more urls or ip addresses? (y/n): ')
        if question == "y":
            continue
        else:
            break
    elif answer == "ip":
        address = input('Please provide the ip address: ')
        # get ip address from user's input
        ip = address
        # asking user for ports range
        portStart = int(input('Please provide starting port: '))
        portEnd = int(input('Please provide ending port: '))
        # create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(60)
        for port in range(portStart, portEnd + 1):
            result = s.connect_ex((ip, port))
            if result == 0:
                print('Port ' + str(port) + ' is open! Grapping banner...')
                # getting banner
                banner = s.recv(1024)
                print('The banner has been grapped! The banner is: ' + banner.decode('utf-8'))
            else:
                print('Port is not open!')
        # closes socket
        s.close()
        question = input('Do you want to provide more urls or ip addresses? (y/n): ')
        if question == "y":
            continue
        else:
            break
    else:
        # user didn't reply with url or ip at the question
        print('Wrong answer... Terminating...')
        break