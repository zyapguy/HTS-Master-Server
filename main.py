"""

HTS Master Servers
-------------------------------------
Written by zyapguy
Written in 11/04/2021 (DD/MM/YYYY)

Version 1.0

"""

import time



def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0

import mysql.connector

class ServerConnection:
    """
    Class for a ServerConnection
    """
    database = None
    cursor = None

    def runQuery(self, query):
        """
        Runs search query and returns result
        """
        self.cursor = self.database.cursor()
        self.cursor.execute(query)
        result =  self.cursor.fetchall()
        return result
    
    def runQueryCommit(self, query):
        """
        Runs query, returns nothing
        """
        self.cursor = self.database.cursor()
        self.cursor.execute(query)
        self.database.commit()

list_of_server_ips = [
    
]


def updateList():
    """
    Updates list from database
    """
    list_of_server_ips.clear()
    returnedData = server.runQuery("SELECT * FROM current_active_servers")
    for data in returnedData:
        list_of_server_ips.append(data[2])

def checkServers():
    """
    Checks servers and deletes server if inactive
    """
    updateList()
    for ip in list_of_server_ips:
        server_on = ping(ip)
        if (server_on == False):
            server.runQueryCommit('DELETE FROM current_active_servers WHERE server_ip="' + ip + '"')

def checkServersLoop():
    """
    Starts loop
    """
    while (True):
        checkServers()
        time.sleep(1)


import configparser
config = configparser.ConfigParser()
config.read('config.env')
server_host = config['SERVER_SETTINGS']['host']
server_user = config['SERVER_SETTINGS']['user']
server_pass = config['SERVER_SETTINGS']['pass']
server_dtbs = config['SERVER_SETTINGS']['dtbs']

server = ServerConnection()

server.database = mysql.connector.connect(
  host=server_host,
  user=server_user,
  password=server_pass,
  database=server_dtbs
)

checkServersLoop()