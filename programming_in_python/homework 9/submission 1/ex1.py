import argparse
import re
import os


parser=argparse.ArgumentParser()
parser.add_argument("-i","--input_file",type=str,required=True)
parser.add_argument("-p","--patterns",nargs="+",type=str,required=True)
parser.add_argument("-s","--separator",type=str,default="\n",required=False)
parser.add_argument("-e","--encoding",type=str,default="utf-8",required=False)

args=parser.parse_args()
extract_file=args.input_file

if not os.path.isfile(extract_file):
    raise ValueError(f"{extract_file} is not a file")

extract_patterns=args.patterns
extract_separator=args.separator
extract_encoding=args.encoding

def output_files(extract_file,extract_patterns,extract_separator,extract_encoding):
    with open(extract_file,"r") as file:
        content=file.readlines()
        i_th_pattern=-1

        for pattern in extract_patterns:
            i_th_pattern+=1
            result=""
            for line in content:
                match_list=re.finditer(pattern,line)
                for element in match_list:
                    result=result+element.group()+extract_separator

            ending="_"+str(i_th_pattern)+".txt"
            file_name=extract_file+ending
            file=open(file_name,"w+",encoding=extract_encoding)
            file.write(result)


output_files(extract_file,extract_patterns,extract_separator,extract_encoding)





