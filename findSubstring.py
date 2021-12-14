string="ABCDCDnCDCFHFHIFHCIJDIJCDDCDCCDCDC"
sub_string="CDC"
count=0
b=0
while(b!=-1):
    b=string.rfind(sub_string)
    string=string[:b+1]
    count+=1
print(count)

