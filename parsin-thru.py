#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import os


###  Funtions ###


# main menu for our wrapper
#function so ASCII art only shows up once
def intro():
  print(""" 

                                ______              
                             .-'      `-.           
                           .'            `.         
                          /                \        
                         ;                 ;`       
                         |                 |;       
                         ;                 ;|
                         '\               / ;       
                          \`.           .' /        
                           `.`-._____.-' .'         
                             / /`_____.-'           
                            / / /                   
                           / / /
                          / / /
                         / / /
                        / / /
                       / / /
                      / / /
                     / / /
                    / / /
                    \/_/
   ____                _           _____ _                
  |  _ \ __ _ _ __ ___(_)_ __     |_   _| |__  _ __ _   _ 
  | |_) / _` | '__/ __| | '_ \ _____| | | '_ \| '__| | | |
  |  __/ (_| | |  \__ \ | | | |_____| | | | | | |  | |_| |
  |_|   \__,_|_|  |___/_|_| |_|     |_| |_| |_|_|   \__,_|
  
  """)
  print("Parsing-Thru is an interactive parser and file extractor!")
  main_menu()
# Have a Main menu func in case wrong selection was made
def main_menu():
  print("\n\nMain Menu")
  print("__"*35)
  option="0"
  while option =="0":
    print("What type of file will we be parsing through?\n1 - Pcap, Pcapng.\n2 - Regular log file.\n3 - Whats the difference?\n4 - Exit.")
    option=input("Please make a choice now (Use numbers):")
    if option == "1":
      pcap_options()
    elif option =="2":
      reg_logs()
    elif option =="3":
      diff_expl()
    elif option =="4":
      print("\n\nExiting... Thank you for using Parsin-Thru!")
      sys.exit()
    else:
      print("\n\nYeah, sorry, that is not going to work! Please choose again!")
      main_menu() 
#def other_options():
def pcap_options():
  print("\n\n")
  print("Pcap type files")
  print("__"*35)
  option="0"
  while option =="0":
    print("1 - Auto extract and parse.\n2 - Learn other ways to extract files. \n3 - Go to previous menu. \n4 - Exit.")
    option= input ("Please choose between 1-4 : ")
    if option =="1":
      tshark_cmds()
    elif option=="2":
      pcap_expl()
    elif option=="3":
      print("\n\nReturning to previous menu...")
      main_menu()
    elif option =="4":
      print("\n\nExiting... Thank you for using Parsin-Thru!")
      sys.exit()
# menu explaining other ways to extract objects from wireshark    
def pcap_expl():
  print("\n\n")
  print("Other ways to extract files from pcaps.")
  print("__"*35)
  print("Of course like many things in life there are mutliple ways to extract objects you may want. One being Wireshark, when desired pcap file is loaded into Wireshark tool you can click on File menu and go to Export Objects. The objects can be exported from HTTP Traffic (File -> Export Objects -> HTTP Traffic) - you can choose any particular files from the object list or save them all with just 1 click. Files can also be exported from SMB Traffic, emails can be exported from SMTP Traffic (File -> Export Objects -> IMF). Objects can also be extracted from FTP data. To do that you need to follow the TCP stream and there in the TCP stream window you will find a button-style menu labeled 'Show and save data as' which defaults to ASCII - Click on the menu and select Raw and click Save as... button. We hope you find it helpful  when you need to examine items from network traffic!")
  option="0"
  while option =="0":
    print("\n\n1 - Thanks, please return to previous menu.\n2 - Exit.")
    option = input ("Please choose between 1 and 2: ")
    if option =="1":
      pcap_options()
    elif option =="2":
      sys.exit()
    else:
      print("Yeah, sorry, that is not going to work! Please choose again!")
      pcap_expl()
#menu explaining the difference between pcap and log files
def diff_expl():
  print("\n\nDifferences between the two")
  print("__"*35)
  print("What is PCAP?\nPacket Capture or PCAP (also known as libpcap) is an application programming interface (API) that captures live network packet data from OSI model Layers 2-7. Network analyzers like Wireshark create .pcap files to collect and record packet data from a network. PCAP comes in a range of formats including Libpcap, WinPcap, and PCAPng.These PCAP files can be used to view TCP/IP and UDP network packets. If you want to record network traffic then you need to create a .pcapfile. You can create a .pcapfile by using a network analyzer or packet sniffing tool like Wireshark or tcpdump.\n\n\nWhat is a log file?\nLog data is a record of activity, typically saved in binary format, along with metadata such as timestamps and other information about the event being logged. From your firewall to your database server, if a system is designed correctly, it will generate logs in almost every part. Log management is a crucial part of IT infrastructure, and log information is key to identifying cybersecurity threats.") 
  option="0"
  while option =="0":
    print("\n\n1 - Thanks, please return to previous menu.\n2 - Exit.")
    option = input ("Please choose between 1 or 2: ")
    if option =="1":
      main_menu()
    elif option =="2":
      sys.exit()
    else:
      print("Yeah, sorry, that is not going to work! Please choose again!")
      diff_expl()
def tshark_cmds():  
  file = input ("Enter file name EXACTLY here: ")
  tshark_extract = os.system("tshark -r " + file + " --export-objects 'http,exported' -q")
  print("Extracting files to exported folder...")
  tshark_parse = os.system("tshark -r " + file + " -q -z ip_hosts,tree")
  print("Number of files extracted from " + file)
  file_count = os.system("find exported -type f | wc -l")
  return tshark_extract, tshark_parse, file_count, file_count

def reg_logs():
  print("\n\nRegular log Options")
  print("__"*35)
  print("1 - Auto parse log.\n2 - Learn log parsing basics.\n3 - Go to previous menu.\n4 - Exit.")
  option="0"
  while option =="0":  
    option = input ("Please choose between 1-4: ")
    if option =="1":
      log_parse()
    elif option =="2":
      how_parse()
    elif option=="3":
      main_menu()
    elif option=="4":
      sys.exit()
    else:
      print("Yeah, sorry, that is not going to work! Please choose again!")
      reg_logs()
#auto log parser  
def log_parse():
  file = input("Enter log file name EXACTLY")
  run_py = os.system("./log.py "+ file)
  return run_py
# and basic explaination of parse logging
def how_parse():
  print("\n\nBasics how to parse with aux cut etc.\nWe can use awk or cut Linux commands to parse our log files. We can get count of unique IP addresses that generated most or least traffic from the log file. It also can get sorted. We need to find a delimeter of the log file we are using log if we use 'cut' command. Adding grep allows us to get a strong tool for carving out data. For use of awk command as well as the cut command we need to know position (field number) of the IP address or other columns in the file.   ")
  print("\n\n"+"__"*35)
  option="0"
  while option =="0":
    print("1 - Thanks, please return to previous menu.\n2 - Exit.")
    option = input ("Please choose between 1 and 2: ")
    if option =="1":
      reg_logs()
    elif option =="2":
      sys.exit()
    else:
      print("Yeah, sorry, that is not going to work! Please choose again!")
      how_parse()
intro()