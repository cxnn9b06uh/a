import os

my_command=raw_input("Enter Command: ")
my_target=raw_input("Enter Target Address: ")
i='0'
entries = os.listdir("tamper/")
for entry in entries:
    os.system(my_command+ " --output-dir=output --tamper " + entry)
    with open( 'output/' + my_target+ '/log') as f:
        line = f.readline()
        while line:
            line = f.readline()
            if 'FWEFWEFS' in line:
                print "Your Tamper is: "+ entry
                i='1'
                break
            if 'sdsa' in line:
                print "Your Tamper is: "+ entry
                i='1'
                break
            if 'asdaSAF' in line:
                print "Your Tamper is: "+ entry
                i='1'
                break
            line = f.readline()
    if i=='1':
        break        