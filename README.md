

#### About the script:

This script parses the `pie_chart.html` file coming from `plot_taxa_summary.py` script from QIIME (for details, visit http://qiime.org/scripts/plot_taxa_summary.html.) and do the following:
  
1.Maps the pie chart and legend image names to corresponding samples.

2.Copies the files to user defined directory

3.Rename the files according to sample ids

4.Merges the pie charts and legends   


#### List of Python modules used in `merge_QIIME_images.py`

| S. No.        | Module        |
| ------------- |:-------------:|
| 1.             |  [fnmatch](https://docs.python.org/2/library/fnmatch.html)      |
| 2.             |    [os](https://docs.python.org/2/library/os.html)         |
| 3.             | [getopt](https://docs.python.org/2/library/getopt.html)        |
| 4.             | [PIL](http://www.pythonware.com/products/pil)           |
| 5.             | [re](https://docs.python.org/2/library/re.html)            |
| 6.             | [shutil](https://docs.python.org/2/library/shutil.html)        |
| 7.             | [sys](https://docs.python.org/2/library/sys.html)           |



#### Usage:
`merge_QIIME_images.py -p path_to_pie_charts.html -c path_to_charts_folder -o output_path_to_final_images`

#### Important Note:
Prerequisites for `merge_QIIME_images.py`

1. Python version 2.7

2. The legend files should be generated in png format (default is pdf). This could be achieved by running the script `plot_taxa_summary.py` with the option `-t/--type_of_file as png`. Given below is an example:

`plot_taxa_summary.py -i phylum.txt -l phylum -c pie -o phylum_charts/ -t png`

#### License
This script is released under GNU GENERAL PUBLIC LICENSE, v3, 29 June 2007

#### Author:
Vijay Lakhujani  (c) 2016 | Xcleris Labs Ltd.



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
