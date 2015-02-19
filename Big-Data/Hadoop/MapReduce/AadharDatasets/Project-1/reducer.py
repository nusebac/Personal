import sys

def reducer():
    get_key=None
    total_adhaar = 0
    for line in sys.stdin:
        newdata = line.strip().split(",")
        if len(newdata) !=2:
            continue
        new_key,adhaar_count = newdata
        if get_key and get_key != new_key:
            print "{0}\t{1}".format(get_key,total_adhaar)
            total_adhaar =0
        get_key = new_key
        try:
        	total_adhaar += float(adhaar_count)
        except:
        	continue
    if get_key !=None:
        print "{0}\t{1}".format(get_key,total_adhaar)
        
        

test_text = """Uttarakhand,1653
Uttarakhand,95
Uttarakhand,138
Uttarakhand,59
Uttarakhand,3338
Uttarakhand,3392
Uttarakhand,4144
Uttarakhand,2938
Uttarakhand,2401
Uttarakhand,154
Uttarakhand,308
Uttarakhand,10932
Uttarakhand,1120
West Bengal,20176
West Bengal,1890
West Bengal,3672
West Bengal,2197
West Bengal,1095
West Bengal,5513
West Bengal,1184
West Bengal,841
West Bengal,12951
West Bengal,450
West Bengal,4598
West Bengal,10989
West Bengal,1411
West Bengal,20746
West Bengal,21973
West Bengal,1472
West Bengal,3273
West Bengal,28752
West Bengal,612"""

# This function allows you to test the mapper with the provided test string
def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	reducer()
	sys.stdin = sys.__stdin__

main()
