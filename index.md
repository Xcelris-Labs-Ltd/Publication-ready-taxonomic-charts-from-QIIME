![](http://www.xcelrislabs.com/Images/Xcelris-An-Abellon-Company-Logo.png)

> #### _We make DNA speak.._





---

## Welcome to Xcelris Labs Ltd. GitHub Pages

###            (by Bioinformatics division)

---

# _prepare_taxa_charts.py_: Ultrafast program to generate publication ready taxonomic pie chart images from QIIME

![Flowchart of the overall programmatic solution]( https://github.com/Xcelris-Labs-Ltd/Publication-ready-taxonomic-charts-from-QIIME/blob/master/flowchart4.png)

* This script parses the pie_chart.html file (output from [`plot_taxa_summary.py`](http://qiime.org/scripts/plot_taxa_summary.html))

* Maps the pie chart and legend image names to corresponding samples.

* Copies the files to user defined directory

* Rename the files according to sample ids

* Merges the pie charts and legends

---

## Usage

```python
python prepare_taxa_charts.py -p pie_charts.html -c /charts_folder -o user_defined_output_folder
```
---

## List of Python modules used 


| S. No.        | Module        |
| ------------- |:-------------:|
| 1.|[fnmatch](https://docs.python.org/2/library/fnmatch.html)  |
| 2.|[os](https://docs.python.org/2/library/os.html)  |
| 3.|[getopt](https://docs.python.org/2/library/getopt.html)  |
| 4.|[PIL](http://www.pythonware.com/products/pil)  |
| 5.|[re](https://docs.python.org/2/library/re.html)  |
| 6.|[shutil](https://docs.python.org/2/library/shutil.html)  |
| 7.|[sys](https://docs.python.org/2/library/sys.html)  |
| 8.|[timeit](https://docs.python.org/2/library/timeit.html)  |

---

## Important Note

Prerequisites for `prepare_taxa_charts.py`:

1. Python v2.7. The program will not work with Python v3. Python v2.7 was chosen as it is stable.

2. Legend files should be generated in `png` format (default is pdf). This could be achieved by running the script `plot_taxa_summary.py` with the option `-t/--type_of_file` as `png`. Given below is an example:

```python
plot_taxa_summary.py -i phylum.txt -l phylum -c pie -o phylum_charts/ -t png
```

** Note: High resolution images can be generated using the `-d`, `--dpi` option for the script `plot_taxa_summary.py`. See below example (setting the dpi to 100 produce good quality images):

```python
plot_taxa_summary.py -i phylum.txt -l phylum -c pie -o phylum_charts/ -t png -d 100
```
---

## License

This script is released under [GNU GENERAL PUBLIC LICENSE](https://github.com/Xcelris-Labs-Ltd/Publication-ready-taxonomic-charts-from-QIIME/blob/gh-pages/LICENSE.md), v3, 29 June 2007

---

## Development and Maintenance

![](https://github.com/Xcelris-Labs-Ltd/Publication-ready-taxonomic-charts-from-QIIME/blob/gh-pages/vijay1.jpg "Vijay Lakhujani")

**Developed by -** [**Vijay Lakhujani**](https://in.linkedin.com/in/lakhujanivijay)

vijay.lakhujani@xcelrislabs.com **[Project Scientist, Bioinformatics]**

Maintained by @Xcelris-Labs-Ltd on GitHub.

---

## Publication
[_prepare_taxa_charts.py: A Python program to automate generation of publication ready taxonomic pie chart images from QIIME._](http://www.sciencedirect.com/science/article/pii/S2213596016302070)

## Citing
**Please cite:**
_Lakhujani, V. and Badapanda, C., 2017. prepare_taxa_charts. py: A Python program to automate generation of publication ready taxonomic pie chart images from QIIME. Genomics Data, 12, pp.97-101._


## Correspondance
![](https://github.com/Xcelris-Labs-Ltd/Publication-ready-taxonomic-charts-from-QIIME/blob/gh-pages/chandan2.jpg "Dr Chandan Badapanda")

chandan.badapanda@xcelrislabs.com **[Associate General Manager, Bioinformatics]**

## Some noise on Twitter about the work

![](https://github.com/Xcelris-Labs-Ltd/Publication-ready-taxonomic-charts-from-QIIME/blob/gh-pages/twitter.PNG "Tweets")

[Xcelris Labs Ltd. &#169;](http://www.xcelrisgenomics.com/ContactUs.html)
