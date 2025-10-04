import time
my_time=int(input("Enter time in seconds to wait: "))
for x in range(my_time,0,-1):
    second=x%60
    
    minute=(x//60)%60
    hours=(x//3600)%24
    print(f"{hours:02}:{minute:02}:{second:02}")


    
    time.sleep(1)
print("time is up")