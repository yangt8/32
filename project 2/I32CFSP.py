from collections import namedtuple
import socket

ConnectfourConnection = namedtuple(
    'ConnectfourConnection',
    ['socket', 'input', 'output'])

def connect(host: str, port: int) -> ConnectfourConnection:
    '''
    Connects to a Connectfour server running on the given host and listening
    on the given port, returning a Connectfour object describing
    that connection if successful, or raising an exception if the attempt
    to connect fails.
    '''   
    connectfour_socket = socket.socket()
    
    connectfour_socket.connect((host, port))

    connectfour_input = connectfour_socket.makefile('r')
    connectfour_output = connectfour_socket.makefile('w')

    return ConnectfourConnection(
        socket = connectfour_socket,
        input = connectfour_input,
        output = connectfour_output)


def hello(connection: ConnectfourConnection, username: str):
    '''
    Logs a user 
    '''
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    print(_read_line(connection))

def start_game(connection: ConnectfourConnection, username: str):
    '''
    starts the game
    '''
    _write_line(connection, 'AI_GAME')
    
def close(connection: ConnectfourConnection) -> None:
    'Closes the connection to the Polling server'
    connection.input.close()
    connection.output.close()
    connection.socket.close()

def _read_line(connection: ConnectfourConnection) -> str:
    '''
    Reads a line of text sent from the server and returns it without
    a newline on the end of it
    '''
    line = connection.input.readline()[:-1]
    return line

def _write_line(connection: ConnectfourConnection, line: str) -> None:
    '''
    Writes a line of text to the server, including the appropriate
    newline sequence, and ensures that it is sent immediately.
    '''
    connection.output.write(line + '\r\n')
    connection.output.flush()
