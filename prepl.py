import argparse
import os 
import re
import sys,getopt  
# Function to matching strings in a filename in an entire folder 
def main():
    usage()
    parser = argparse.ArgumentParser(prog='prepl', usage='%(prog)s [options]', prefix_chars='--')
    parser.add_argument('--foldername', nargs='+', type=str, help='foldername in which files to be changed',required=True)
    parser.add_argument('--stringtomatch', nargs='+', type=str,help='string to match',required=True)
    parser.add_argument('--stringtoreplace', nargs='+', type=str, help='stringtoreplace',required=True)
    args = parser.parse_args()
    #print(args.foldername[0])
    #print(args.stringtomatch[0])
    #print(args.stringtoreplace[0])
    for filename in os.listdir(args.foldername[0]): 
        tfile = filename
        folder = args.foldername[0] + "\\"
        if args.stringtomatch[0] != "" and args.stringtoreplace[0] != "": 
            tfile = re.sub(args.stringtomatch[0],args.stringtoreplace[0],tfile)
            os.rename(folder + filename, folder+tfile) 
            print(tfile)
        else:
            tfile = args.stringtoreplace[0] + "_" + tfile
            os.rename(folder + filename, folder+tfile) 
            print(tfile)
def usage():
    print ('prepl.py -f <foldername> -s <stringtomatch> -r <stringtoreplace>')
if __name__ == "__main__":
    main()	