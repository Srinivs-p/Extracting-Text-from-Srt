path = 'C:/Users/User/'
def Read_Srt(path):
    """
    This Function reads Srt files and get rid of non text and writes into txt files.
    """
    for filename in glob.glob(os.path.join(path, '*.srt')):
        Open_file = open(filename)
        read_f = Open_file.readlines()
        read_f = ''.join(read_f)
        Rm_nm = re.sub("\d", ' ', read_f)
        Rm_Nonalph = re.sub(":","", l2) 
        Rm_Nonalph = re.sub('-->','',Rm_Nonalph)      
        Rm_Nonalph = re.sub(',','',Rm_Nonalph)
        Rm_Newln = Rm_Nonalph.replace('\r', '').replace('\n', '')
        Rm_Wpce = re.sub('\s+', ' ', Rm_Newln).strip()
        f2 = open("C:/Users/User/Output.txt", "a+")
        f2.write(Rm_Wpce)
        f2.close()
Read_Srt(path)

