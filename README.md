# td-client-test

Requirements:

Python:
  python 2.7.x
  prettytable-0.7.2
  
td:
 td-client
 
To install prettytable:
$sudo pip2.7 install https://pypi.python.org/packages/source/P/PrettyTable/prettytable-0.7.2.tar.bz2


To get help:
$ python t1.py -h
usage: t1.py [-h] -d DATABASE -t TABLE [-f [{csv,tabular}]] [-c [COLUMN]]
             [-l [LIMIT]] [-m [MIN]] [-M [MAX]] [-e [{hive,presto}]]

optional arguments:
  -h, --help            show this help message and exit
  -d DATABASE, --database DATABASE
                        Required, database name
  -t TABLE, --table TABLE
                        Required, table name
  -f [{csv,tabular}], --format [{csv,tabular}]
                        Optional and specifies output file format, default is
                        csv
  -c [COLUMN], --column [COLUMN]
                        Optional and specifies column(s) to query, if not
                        specified, all columns will be queried, use comma to
                        separate column names, e.g. c1,c2,c3
  -l [LIMIT], --limit [LIMIT]
                        Optional and specifies number of rows to get in the
                        query, default is all records
  -m [MIN], --min [MIN]
                        Optional and specifies the minimum timestamp, default
                        is NULL
  -M [MAX], --MAX [MAX]
                        Optional and specifies the maximum timestamp, default
                        is NULL
  -e [{hive,presto}], --engine [{hive,presto}]
                        Optional and specifies the query engine, default is
                        "presto"

Command line examples:
  $python td-client-test.py -d shan_test_db -t movie_rating -l 10 -e presto -f csv
  $python td-client-test.py -d shan_test_db -t movie_rating -c film,genre -l 10 -e presto -min 2011 -MAX 2018
