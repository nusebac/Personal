
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(",")
        if len(data)==4:
            state = data[0]
            aadhar_created = data[2]
            print "{0},{1}".format(state,aadhar_created)
        
        
test_text = """Uttarakhand,Almora,1653,12
Uttarakhand,Bageshwar,95,4
Uttarakhand,Chamoli,138,2
Uttarakhand,Champawat,59,0
Uttarakhand,Dehradun,3338,82
Uttarakhand,Haridwar,3392,131
Uttarakhand,Nainital,4144,61
Uttarakhand,Pauri Garhwal,2938,39
Uttarakhand,Pithoragarh,2401,14
Uttarakhand,Rudraprayag,154,0
Uttarakhand,Tehri Garhwal,308,7
Uttarakhand,Udham Singh Nagar,10932,274
Uttarakhand,Uttarkashi,1120,8
West Bengal,Bankura,20176,94
West Bengal,Barddhaman,1890,81
West Bengal,Birbhum,3672,46
West Bengal,Cooch Behar,2197,26
West Bengal,Dakshin Dinajpur,1095,12
West Bengal,Darjeeling,5513,41
West Bengal,Hooghly,1184,38
West Bengal,Howrah,841,6
West Bengal,Jalpaiguri,12951,157
West Bengal,Kolkata,450,11
West Bengal,Malda,4598,32
West Bengal,Murshidabad,10989,107
West Bengal,Nadia,1411,17
West Bengal,North 24 Parganas,20746,150
West Bengal,Paschim Medinipur,21973,423
West Bengal,Purba Medinipur,1472,51
West Bengal,Puruliya,3273,18
West Bengal,South 24 Parganas,28752,151
West Bengal,Uttar Dinajpur,612,12"""

# This function allows you to test the mapper with the provided test string
def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__

main()
