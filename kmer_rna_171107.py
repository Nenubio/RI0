#dic_of_squerance

a = 'CCACCUCAGCCAGAGUUCGUAACGGACCCUCGACUUUCUUUGGAUAGCUUU'
b = 'b'
#one_mer_frequency:cacluate the frequency of one mer RNA
def one_mer_frequency(name,squence):
    """calculate one_mer_frequency.

    Things to do.

    Args:
        name:
        squence:

    Returns:
        A dict of one_mer_frequency. For
        example:

        {'A': 0.25,
         'B': 0.35,
         'D': 0.15,
         'E': 0.25 }

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """    
    length= len( squence )                #count the length of squence
    one_mer_frequency_dic = {}
    one_mer_frequency_dic_list = []
    one_Nucleotide = ['A','G','C','U']    
    C_num = 0
    A_num = 0
    G_num = 0
    U_num = 0
    #print(squence)
    #print(length)
    for i in range(length):
        #print(i)
        if(squence[i] == 'A'):
            A_num = A_num + 1
        elif(squence[i] == 'G'):
            G_num = G_num + 1
        elif(squence[i] == 'C'):
            C_num = C_num + 1
        else:
            U_num = U_num + 1
    #print(C_num,A_num,G_num,U_num)      #for watch if it count right number
    one_mer_frequency_dic['A'] = A_num/length
    one_mer_frequency_dic['G'] = G_num/length
    one_mer_frequency_dic['C'] = C_num/length
    one_mer_frequency_dic['U'] = U_num/length
    one_mer_frequency_dic_list.append(round(A_num/length,8))
    one_mer_frequency_dic_list.append(round(G_num/length,8))
    one_mer_frequency_dic_list.append(round(C_num/length,8))
    one_mer_frequency_dic_list.append(round(U_num/length,8))
    
    one_Nucleotide = ['A','G','C','U']
    
    #print (one_mer_frequency_dic)       #for watch if it count right frequence
    return one_mer_frequency_dic_list
    #return one_mer_frequency_dic


#two_mer_frequency:cacluate the frequency of one mer RNA
def two_mer_frequency(name,squence):
    """calculate two_mer_frequency.

    Things to do.

    Args:
        name:
        squence:

    Returns:
        A dict of one_mer_frequency. For
        example:

        {'AB': 0.25,
         'BB': 0.35,
         'DB': 0.15,
         'EB': 0.25 }

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """    
    two_mer_frequency_dic = {}
    two_mer_frequency_dic_list = []
    one_Nucleotide = ['A','G','C','U']
    length_of_one_Nucleotide = len (one_Nucleotide)
    length= len( squence ) 
    two_Nucleotide = []
    a_kind_of_two_Nucleotide = ""
    for i in range( length_of_one_Nucleotide):
        for j in range( length_of_one_Nucleotide):
            two_Nucleotide.append (one_Nucleotide[i] + one_Nucleotide[j])
            a_kind_of_two_Nucleotide = one_Nucleotide[i] + one_Nucleotide[j]
            
            num = PatternCount(a_kind_of_two_Nucleotide, squence)
            two_mer_frequency_dic[a_kind_of_two_Nucleotide] = num / (length - 1)
            two_mer_frequency_dic_list.append(round(num / (length - 1),8))
            
    #print (two_Nucleotide)
    #print (two_mer_frequency_dic)
    #two_mer_frequency_dic_list = two_mer_frequency_dic_list * 4
    #for i in range(len(two_mer_frequency_dic_list) - 1):
    #   two_mer_frequency_dic_list[i] = two_mer_frequency_dic_list[i]  * 4
    return two_mer_frequency_dic_list
#    return two_mer_frequency_dic
            
#two_mer_frequency(['A','G','C','G'])

#three_mer_frequency:cacluate the frequency of one mer RNA
def three_mer_frequency(name,squence):
    """calculate three_mer_frequency.

    Things to do.

    Args:
        name:
        squence:

    Returns:
        A dict of one_mer_frequency. For
        example:

        {'ABC': 0.25,
         'BBC': 0.35,
         'CBC': 0.15,
         'DBC': 0.25 }

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """ 
    three_mer_frequency = {}
    three_mer_frequency_dic_list = []
    one_Nucleotide = ['A','G','C','U']
    two_Nucleotide = ['AA', 'AG', 'AC', 'AU', 'GA', 'GG', 'GC', 'GU', 'CA', 'CG', 'CC', 'CU', 'UA', 'UG', 'UC', 'UU']
    length_of_one_Nucleotide = len (one_Nucleotide)
    length_of_two_Nucleotide = len (two_Nucleotide)
    three_Nucleotide = []
    for i in range( length_of_one_Nucleotide):
        for j in range( length_of_two_Nucleotide):
            three_Nucleotide.append (one_Nucleotide[i] + two_Nucleotide[j])
            #three_Nucleotide.append (one_Nucleotide[i] + one_Nucleotide[j])
            a_kind_of_three_Nucleotide = one_Nucleotide[i] + two_Nucleotide[j]
            num = PatternCount(a_kind_of_three_Nucleotide, squence)
            length= len( squence ) 
            three_mer_frequency[a_kind_of_three_Nucleotide] = num / (length - 2)   
            three_mer_frequency_dic_list.append(round(num / (length - 2),8) )
    #print (three_mer_frequency)
    #print (three_Nucleotide)
    #print(three_mer_frequency_dic_list)
    #three_mer_frequency_dic_list  = three_mer_frequency_dic_list * 16
    #for i in range(len(three_mer_frequency_dic_list)) :
    #   three_mer_frequency_dic_list[i] = three_mer_frequency_dic_list[i] * 16
        
    
    #print(three_mer_frequency_dic_list)
    return three_mer_frequency_dic_list
#    return three_mer_frequency
    
    
#input pattern and text return pattern's num
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 



def mer_frequence(name,squence):
    """calculate 64+16 +8 = 84's_mer_frequency.

    Things to do:84 .

    Args:
        name:
        squence:

    Returns:
        A dict of one_mer_frequency. For
        example:

        {'A': 0.25,
         'BB': 0.35,
         'CCC': 0.15, }

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """     
    four_mer = one_mer_frequency(name, squence)
    sixteen_mer = two_mer_frequency(name, squence)
    sixtyfour_mer = three_mer_frequency(name, squence)  
    #eightyfour_mer = four_mer + sixteen_mer + sixtyfour_mer
    #eightyfour_mer=dict(four_mer, **sixteen_mer,**sixtyfour_mer)        #new way to add the dictionary
    eightyfour_mer = []
    eightyfour_mer =four_mer + sixteen_mer + sixtyfour_mer
    #print(name)
    #print(name[0:2])
    if(name[0:3] == 'pos'):
        #eightyfour_mer['flag'] = 1      #positive
        eightyfour_mer.append('1')
    elif(name[0:3] == 'neg'):
        #eightyfour_mer['flag'] = 0      #negetave
        eightyfour_mer.append('0')
    #eightyfour_mer_list = list(eightyfour_mer.values())
    
    
    #print (eightyfour_mer)
    for i in eightyfour_mer:
        print (i)
        fpw.write(str(i) + '  ')
    
    fpw.write('\n')
    #fpw.write(eightyfour_mer)
    #print (eightyfour_mer_list)
    return eightyfour_mer

#read things from txt

txtpath=r"21data.txt"
txtpath_w=r"21data1.txt"

fpw = open(txtpath_w,'w+')

fp=open(txtpath)
arr=[]

RNA_num = ''
RNA_squence = ''
flag = 'neg' #set flag of pos or neg
import re
for lines in fp.readlines():
    lines=lines.replace("\n","").split(",")
    
    #print(lines[0][0])
    #print('@@@')

    if(lines[0][0]== 'I'  ): #change the flag
        #print(lines)
        if(flag == 'pos'):
            flag = 'neg'
        elif(flag == 'neg'):
            flag = 'pos'
        #print(flag)
    if(lines[0][0]== '>' ):
        arr.append(lines)
        RNA_num = flag + lines[0]
        #print("!" + RNA_num)
    else:
        RNA_squence = lines
        #print("@" + RNA_squence[0])
        mer_frequence(RNA_num, RNA_squence[0])    
        
        #fpw.write(mer_frequence(RNA_num, RNA_squence[0]) )
        
fpw.close()  
fp.close()
