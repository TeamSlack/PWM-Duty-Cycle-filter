import os

def is_number(num):
    try:
        float(num)
        return True 
    except ValueError:
        return False

print("Info: Ctrl+C at anytime to quit")
path_name = input("Enter path name: ") + "\\"


os.chdir(path_name)

i = 1
while i == 1:
    try:
        file_name = input("Enter file name: ")
        temp = file_name.split(".")

        thres = float(input("Enter the threshold: "))

        new_file_name = temp[0] + ".csv"
        f1 = open(file_name)
        f2 = open(path_name+new_file_name,"w+")

        first_time = True

        #go through each line in the target file but ignore the first 5 lines
        j = 5 #[Update 27/11/19] first 5 lines in the measurement file can throw an error
        for lines in f1:

            #[Update 27/11/19] After 5 lines, go into normal function routine
            if j == 0:
                raw_dat = lines.split(',')
                voltage = raw_dat[1]
                #strip removes \n from the string
                voltage = voltage.strip("\n")
                #print(voltage)
                if((is_number(voltage)==True)):
                    voltage = float(voltage)
                    #store the time when value goes above the threshold (start of pulse)
                    if(voltage > thres and first_time == True):
                        #a = input("Press to continue..")
                        time1 = float(raw_dat[0])*1000000
                        #print(time1, voltage)
                        first_time = False
                    #store the time when value goes below the threshold (end of pulse)
                    if(voltage < thres and first_time == False):
                        #a = input("Press to continue..")
                        time2 = float(raw_dat[0])*1000000
                        #print(time2,voltage)
                        #gets the total duration / length of the pulse
                        time = time2-time1
                        #print(time)
                        f2.write(str(time) + "," + str(voltage)+"\n")
                        first_time = True
            else:
                #[Update 27/11/19] countdown of the 5 lines
                j -= 1

        f1.close()
        f2.close()
        print("Filtering Done!")
    except IOError:
        print("Unable to open file. Check if file is open.")
    except KeyboardInterrupt:
        exit()
    
    
