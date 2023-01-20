#import module
import speedtest

#chosing ideal server
test = speedtest.Speedtest()
print("SERVER LOADING............")
test.get_servers()
print("CHOSING IDEAL SERVERS.............")
ideal  = test.get_best_server()
print(ideal)

#chosing option
option = int(input('''What speed do you want to test:  


1) Download Speed  
  
2) Upload Speed  
  
3) Ping 
  
Your Choice: '''))
if option == 1: 
    #call download functions
    print("EXECUTING DOWNLOAD TEST......")
    download_outcome = test.download()
    print(f"DOWNLOAD SPEED: {download_outcome/1024/1024: .3f} MBPS")

elif option == 2: 
    #call upload functions
    print("EXECUTING UPLOAD TEST......")
    upload_outcome = test.upload()
    print(f"UPLOAD SPEED: {upload_outcome/1024/1024: .3f} MBPS")

elif option == 3: 
    ping_outcome = test.results.ping
    print(f"PING: {ping_outcome/1024/1024: .3f} ms")
    
else: 
    print("PLEASE ENTER CORRECT CHOICE")




