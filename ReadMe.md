# Publication-ready-taxonomic-charts-from-QIIME
Ultra fast program to generate publication ready taxonomic pie charts from QIIME.


#### About the script:

This script parses the `pie_chart.html` file coming from `plot_taxa_summary.py` script from QIIME (for details, visit http://qiime.org/scripts/plot_taxa_summary.html.) and do the following:
  
1.Maps the pie chart and legend image names to corresponding samples.

2.Copies the files to user defined directory

3.Rename the files according to sample ids

4.Merges the pie charts and legends   


#### List of Python modules used in `prepare_taxa_charts.py`

| S. No.        | Module        |
| ------------- |:-------------:|
| 1.             |  [fnmatch](https://docs.python.org/2/library/fnmatch.html)      |
| 2.             |    [os](https://docs.python.org/2/library/os.html)         |
| 3.             | [getopt](https://docs.python.org/2/library/getopt.html)        |
| 4.             | [PIL](http://www.pythonware.com/products/pil)           |
| 5.             | [re](https://docs.python.org/2/library/re.html)            |
| 6.             | [shutil](https://docs.python.org/2/library/shutil.html)        |
| 7.             | [sys](https://docs.python.org/2/library/sys.html)           |
| 8.             | [timeit](https://docs.python.org/2/library/timeit.html)           |



#### Usage:
`prepare_taxa_charts.py -p path_to_pie_charts.html -c path_to_charts_folder -o output_path_to_final_images`

#### Important Note:
Prerequisites for `prepare_taxa_charts.py`

1. Python version 2.7

2. The legend files should be generated in png format (default is pdf). This could be achieved by running the script `plot_taxa_summary.py` with the option `-t/--type_of_file as png`. Given below is an example:

`plot_taxa_summary.py -i phylum.txt -l phylum -c pie -o phylum_charts/ -t png`

** Note: High resolution images can be generated using the -d, --dpi option for the script plot_taxa_summary.py. See below example (setting the dpi to 100 produce good quality images):

`plot_taxa_summary.py -i phylum.txt -l phylum -c pie -o phylum_charts/ -t png -d 100`

#### License
This script is released under GNU GENERAL PUBLIC LICENSE, v3, 29 June 2007

## Development and Maintenance

**Developed by -**
**Vijay Lakhujani:**

<img align="left" width="200" height="200" src="https://github.com/Xcelris-Labs-Ltd/Publication-ready-taxonomic-charts-from-QIIME/blob/master/supplementary_files/vijay_lakhujani.jpg?raw=true">

 Project Scientist, Bioinformatics

 NGS division, Xcelris Labs Ltd

 vijay.lakhujani@xcelrislabs.com




---

**Let's connect!**

[![alt text][1.1]][1]
[![alt text][2.1]][2]
[![alt text][3.1]][3]
[![alt text][4.1]][4]

[1.1]: http://i.imgur.com/tXSoThF.png (twitter icon with padding)
[2.1]: http://i.imgur.com/P3YfQoD.png (facebook icon with padding)
[3.1]: http://i.imgur.com/0o48UoR.png (github icon)
[4.1]: https://github.com/Xcelris-Labs-Ltd/Publication-ready-taxonomic-charts-from-QIIME/blob/master/supplementary_files/LinkedIn.png?raw=true (linkedin icon)


[1]: http://www.twitter.com/vijay_lakhujani
[2]: http://www.facebook.com/mylifepages
[3]: https://github.com/lakhujanivijay
[4]: https://in.linkedin.com/in/lakhujanivijay

#### Full Details
Click [here](https://github.com/Xcelris-Labs-Ltd/Publication-ready-taxonomic-charts-from-QIIME/blob/gh-pages/index.md)

