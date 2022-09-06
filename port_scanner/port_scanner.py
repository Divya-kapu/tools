import socket
from datetime import *
import sys
import logging

# Well known ports only
ports_to_scan = range(1, 1024)


# Todo - Add code. Just a placeholder for now
def is_ip_valid(host_ip):
  return True


def scan_each_port(host_ip):
  try:
    for port in ports_to_scan:
      socket_handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      connection = socket_handle.connect_ex((host_ip, port))
      if connection == 0 and port != 135:
        try:
          service = socket_handle.recv(1024).decode()
          print('Port#{} is open and the related service is {}'.format(port, service))
        except:
          print('Port#{} open'.format(port))
          pass  # Ignore if service isn't fetched
      else:
        continue
        # os.system( 'cls' )  #  to clear the previous output screen
        # print('{} is closed port'.format(port))
      socket_handle.close()
  except KeyboardInterrupt:
    print("you cancelled the scan")
    sys.exit()
  except socket.error:
    print("couldn't connect to the server")
    sys.exit()
  except socket.gaierror:  # Host name ' ' is invalid
    print("couldn't resolve the host address")
    sys.exit()


def main():
  t_start = datetime.now()

  # -- For unit testing on localhost --
  # domain = socket.gethostname()
  # host_ip = socket.gethostbyname(domain)
  # print('ip for {} is {}'.format(domain, host_ip))

  host_ip = input("enter ip to scan : ")
  if not is_ip_valid(host_ip):
    logging.error("IP {} is not valid, enter a valid one".format(host_ip))

  print("processing scanning")
  print("scan start time: {}".format(t_start))

  scan_each_port(host_ip)

  t_end = datetime.now()
  print('total scanning time is: {}'.format(t_start - t_end))


if __name__ == "__main__":
  main()

