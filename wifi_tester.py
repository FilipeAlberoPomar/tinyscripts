import requests, time, datetime

# Tests a connection by makking an http request to a server every 5 seconds
# It logs 1x min that it's running
# It logs every time there is an error

# To run headless in the background
# $nohup python /home/pi/wifi_tester/wifi_tester.py &

# ConnectTimeoutError means no connection to host, sem conexao Virgin
# NewConnectionError means wifi issues.


def disconnects_logger():

    count = 1

    while(True):
        try:
            request = requests.head("http://www.bing.com", timeout=3)
            result = request.status_code
        except Exception as e:
            result = e

        current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        if (result != 200):
            with open('wifi_tester_error.log', 'a') as the_file:
                the_file.write(current_time +" ERROR:"+str(result)+"\n")
        
        if (count == 12):
            count = 1
            with open('wifi_tester_runs.log', 'a') as the_file:
                the_file.write(current_time +" EXECUTED\n")
        
        count += 1
        time.sleep(5)

disconnects_logger()
