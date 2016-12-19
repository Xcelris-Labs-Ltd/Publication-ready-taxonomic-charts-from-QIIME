![](http://www.xcelrislabs.com/Images/Xcelris-An-Abellon-Company-Logo.png)


## We make DNA speak..
## Welcome to Xcelris Labs Ltd. GitHub Pages (by Bioinformatics division)

## About merge_QIIME_images.py

![]( https://httpsimage.com/img/flowchart4.png)


* This script parses the pie_chart.html file (output from [plot_taxa_summary.py](http://qiime.org/scripts/plot_taxa_summary.html))

* Maps the pie chart and legend image names to corresponding samples.

* Copies the files to user defined directory

* Rename the files according to sample ids

* Merges the pie charts and legends

## Usage

 `python merge_QIIME_images.py -p pie_charts.html -c /charts_folder
-o user_defined_output_folder`

## Important Note
Prerequisites for `merge_QIIME_images.py`:

1. Python v2.7

2. Legend files should be generated in `png` format (default is pdf). This could be achieved by running the script `plot_taxa_summary.py` with the option `-t/--type_of_file` as `png`. Given below is an example:

`plot_taxa_summary.py -i phylum.txt -l phylum -c pie -o phylum_charts/ -t png`

##License
This script is released under GNU GENERAL PUBLIC LICENSE, v3, 29 June 2007

## Development and Maintenance
Developed by - Vijay Lakhujani

vijay.lakhujani@xcelrislabs.com **[Project Scientist, Bioinformatics]**

Maintained by @Xcelris-Labs-Ltd on GitHub.

***

## Correspondance
chandan.badapanda@xcelrislabs.com **[Associate General Manager, Bioinformatics]**

[Xcelris Labs Ltd. &#169;](http://www.xcelrisgenomics.com/ContactUs.html)
