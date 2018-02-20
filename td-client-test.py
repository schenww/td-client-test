#!/usr/bin/env python
import argparse
import os
import sys
import tdclient

apikey = "3867/4c6a67efbbc95f475ac8c9ec092f87b4c01b8c99"

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--database', required=True, help='Required, database name')
parser.add_argument('-t', '--table', required=True, help='Required, table name')
parser.add_argument('-f', '--format', nargs='?', default='tabular', help='Optional and specifies output file format, default is csv')
parser.add_argument('-c', '--column', nargs='?', default='*', help='Optional and specifies column(s) to query, if not specified, all columns will be queried, use comma to separate column names, e.g. c1,c2,c3')
parser.add_argument('-l', '--limit', nargs='?', default='0', type=int, help='Optional and specifies number of rows to get in the query, default is all records')
parser.add_argument('-m', '--min', nargs='?', default='NULL', help='Optional and specifies the minimum timestamp, default is NULL')
parser.add_argument('-M', '--MAX', nargs='?', default='NULL', help='Optional and specifies the maximum timestamp, default is NULL')
parser.add_argument('-e', '--engine', nargs='?', default='presto', choices=['hive','presto'], help='Optional and specifies the query engine, default is "presto"')
args = parser.parse_args()

# construct the query
qry = 'select '
qry += args.column
qry += ' from '
qry += args.table
qry += ' where TD_TIME_RANGE(time, '
qry += args.min
qry += ', '
qry += args.MAX
qry += ')'
print qry

# validate the parameters passed in
if args.limit > 0:
  qry += ' LIMIT '
  qry += str(args.limit)
  # Prepare submitting job
# database name
db = args.database

# output file name
outfilename = "query_output.out"

try:
  with tdclient.Client(apikey) as client:
    job = client.query(db, qry, type=args.engine)
    job.wait()
    f = open(outfilename,"w")
    cnt = 0
    for row in job.result():
       cnt += 1
       print row
       f.write("%s\n" % str(row))
    f.close()
    if cnt == 0:
      print "The query returns 0 row"
    sys.exit()
except RuntimeError as e:
    #sys.exit("Failed to execute the query or download the query results to a file...")
    print e
