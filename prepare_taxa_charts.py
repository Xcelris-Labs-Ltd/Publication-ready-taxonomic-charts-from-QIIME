__author__ = "Vijay Lakhujani, Project Scientist, Xcelris Labs Ltd."
__maintainer__ = "Vijay Lakhujani, Project Scientist, Xcelris Labs Ltd."
__copyright__ = "Copyright 2016, Xcelris Labs Ltd."
__license__ = "GPL"
__version__ = "1.0"
__status__ = "Complete"
__email__="chandan.badapanda@xcelrislabs.com"


'''
                          __  __        _      _       _          _           _    _      _     
                          \ \/ /___ ___| |_ __(_)___  | |    __ _| |__  ___  | |  | |_ __| |    
                           \  // __/ _ \ | '__| / __| | |   / _` | '_ \/ __| | |  | __/ _` |    
                           /  \ (_|  __/ | |  | \__ \ | |__| (_| | |_) \__ \ | |__| || (_| |  _ 
                          /_/\_\___\___|_|_|  |_|___/ |_____\__,_|_.__/|___/ |_____\__\__,_| (_)

                            __        __                     _          ____  _   _    _    
                            \ \      / /__   _ __ ___   __ _| | _____  |  _ \| \ | |  / \   
                             \ \ /\ / / _ \ | '_ ` _ \ / _` | |/ / _ \ | | | |  \| | / _ \  
                              \ V  V /  __/ | | | | | | (_| |   <  __/ | |_| | |\  |/ ___ \ 
                               \_/\_/ \___| |_| |_| |_|\__,_|_|\_\___| |____/|_| \_/_/   \_\

                  _                
                                             ___ _ __   ___  __ _| | __            
                                            / __| '_ \ / _ \/ _` | |/ /            
                                            \__ \ |_) |  __/ (_| |   <   _   _   _ 
                                            |___/ .__/ \___|\__,_|_|\_\ (_) (_) (_)
                                                |_| 



About the script:
- This script parses the pie_chart.html file generated from 'plot_taxa_summary.py' script from QIIME 
  (for details, visit:http://qiime.org/scripts/plot_taxa_summary.html)
- Maps the pie chart and legend image names to corresponding samples.
- Copies the files to user defined directory
- Rename the files according to sample ids
- Merges the pie charts and legends   
     
Usage: "prepare_taxa_charts.py -p <path to pie_charts.html> -c <path to charts folder> -o <output path final images>"

Copyright (C) 2016  Xcelris Labs Ltd. | www.xcelrisgenomics.com

prepare_taxa_charts.py program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful,but WITHOUT ANY
WARRANTY; without even the implied warranty ofMERCHANTABILITY or FITNESS FOR A 
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this
program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street,
Fifth Floor, Boston, MA  02110-1301, USA.


Contact:
=======
Corresponding author: 
E-mail-chandan.badapanda@xcelrislabs.com;
Tel: +91-79-66092177; Fax: +91-79-66309341
'''

#    Importing modules
import os
import sys
import re
import shutil
import fnmatch
import getopt
from timeit import default_timer as timer
import PIL
from PIL import Image

#    Declaring variables
count=0
prefixes = ('Phylum_','Phylum', 'Class_','Class', 'Order_','Order', 'Family_','Family', 'Genus_','Genus')
found_p, found_c, found_o = False, False, False
current_key = None
final_images=[]
sample_taxa_mapping_list=[]
final_images=[]
file_list=[]
mapping_list={}
final_mapping_list={}
start = timer()

#    Taking user input for pie_chart.html file, charts folder and final output path
def usage():
    print "\nUsage: "
    print "      prepare_taxa_charts.py -p <pie_charts.html> -c <path to charts folder> -o <output folder path>\n"

try:
    options, remainder=getopt.getopt(sys.argv[1:], 'p:c:o:h')

except getopt.GetoptError as err:
    print str(err)
    usage()
    sys.exit()

for opt, arg in options:
    if opt in ('-p'):
        found_p = True
        pie_chart_html_file=arg
    if opt in ('-c'):
        found_c = True
        charts_folder_path=arg
    if opt in ('-o'):
        found_o = True
        output_folder=arg
    if opt in ('-h'):
        usage()
	sys.exit()

if not found_p:
    print "\nError: Missing parameter -p, pie_charts.html was not provided"
    usage()
    sys.exit(2)
if not found_c:
    print "\nError: Missing parameter -c, charts folder was not provided"
    usage()
    sys.exit(2)
if not found_o:
    print "\nError: Missing parameter -o, output folder was not provided"
    usage()
    sys.exit(2)

#    Parsing pie_charts.html file
print "\n=> Reading pie_charts.html" 
file =open(pie_chart_html_file)
for line in file:
    line=line.rstrip()

#   Parsing sample id taxonomy wise
    if 'Current Level' in line:
        regex = r"Current Level: (\w+\.?\w+)"
        matches = re.findall(regex, line)
        for match in matches:
	    sample_taxa_mapping_list.append(match)

#   Parsing corresponding image names  
    if "ntitle" in line:
        regex = r"charts\/(\w+).png"
        matches = re.findall(regex, line)
        for match in matches:
            sample_taxa_mapping_list.append(match)              
    
for element in sample_taxa_mapping_list:
    if any(element.startswith(p) for p in prefixes):
        current_key = element
        if current_key not in mapping_list:
            mapping_list[current_key] = []
    else:
        mapping_list[current_key].append(element)

for k, v in mapping_list.iteritems():
    if "_" in k:
        if 'legend' in "".join(v[-1]):
            final_mapping_list[k+".png"]="".join(v[-2])+".png"
            final_mapping_list[k+"_legend.png"]="".join(v[-2])+"_legend.png"
        
        else:
            final_mapping_list[k+".png"]="".join(v[-1])+".png"
            final_mapping_list[k+"_legend.png"]="".join(v[-1])+"_legend.png"

print "=> No. of samples: " + str(len(final_mapping_list)/10)

#    Check if output folder already exists, if yes, then remove and re-create
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)
os.makedirs(output_folder)

#    Copying pie and legend image files to user defined directory
for k, v in final_mapping_list.iteritems():
    shutil.copy2(charts_folder_path+"/"+v, output_folder)

print "\n=> Copying pie chart and legend images to:" 
print output_folder + "...\n"

os.chdir(output_folder)

for k, v in final_mapping_list.iteritems():
    os.rename(v,k)

print "=> Renaming images according to sample names...\n"

#   Reading images 
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.png'):
        file_list.append(file)

file_list=sorted(file_list)

print "=> Merging pie chart and legend images...\n"

for j in range(0,len(file_list)-1):
    if file_list[j][:-4] == file_list[j+1][:-11]:
        count+=1
        
        final_images.append(file_list[j])
        final_images.append(file_list[j+1])
        
        images = map(Image.open,final_images)

#    Calculating pie and legend image dimensions
        widths, heights = zip(*(i.size for i in images))
	total_width = widths[0]
	max_height = max(heights)

#    Creating blank landscape image
	new_im=Image.new('RGB', (total_width, max_height),(255, 255, 255))
        x_offset = 0
        y_offset = 0

#    Merging images
        for im in images:
            new_im.paste(im, (x_offset,y_offset))

#    Adjusting image offsets
            x_offset += im.size[1]-40
            y_offset += 170

#    Appending suffix "_final" in the output files
        result= file_list[j][:-4] + '_final.png'
        new_im.save(result)

#    Flushing old images 
        final_images=[]
        result=''

#    Printing logs for each sample
        if count % 5 == 0:
           print '	Merging images for sample#' + str(count/5) + "..."

print '\n=> Cleaning output directory...\n'
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.png'):
        if 'final' not in file:
            os.remove(file)

end = timer()
print "Total execution time:", str(end - start)[0:6] + " seconds.\n"
