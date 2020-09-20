# The program gets the size of a file (in MB) and the speed of the internet (in Mbps), calculates and informs 
# the estimated time of download of the file (in minutes)

fileSize = float(input("Enter the size of a file in MB: "))
internetSpeed = float(input("Enter the speed of the internet: "))

timeOfDownload = (fileSize / internetSpeed) / 60.0

print(f"The estimated time of download in minutes is: {timeOfDownload:0.1f} ")