#!/usr/bin/env python

# An over-engineered calculator for use with docker-pipeline
# Reads the first line from two different files as numbers,
# adds them, then writes them to a third file.

# INPUTS
#
# CONT_INPUT_FILE1 - file with a number on the first line
# CONT_INPUT_FILE2 - file with a number on the first line

# OUTPUTS
#
# CONT_OUTPUT_FILE - file to write the sum of the other two numbers

import os

def read(filename):
  print 'Reading number from {}'.format(filename)
  with open(filename, 'r') as f:
    return int(f.readlines()[0].strip())

def write(filename, num):
  print 'Writing {} to {}'.format(num, filename)
  with open(filename, 'w') as f:
    f.write(str(num) + '\n')

def add(num1, num2):
  print 'Adding {} and {}'.format(num1, num2)
  return num1 + num2

def main(file1, file2, outputfile):
  [num1, num2] = [read(f) for f in [file1, file2]]
  result = add(num1, num2)
  write(outputfile, result)

if __name__ == '__main__':
  try:
    env_vars = ['CONT_INPUT_FILE1','CONT_INPUT_FILE2','CONT_OUTPUT_FILE']
    p = [file1, file2, outputfile] = [os.getenv(v) for v in env_vars]
    if None in p:
      missing = env_vars[p.index(None)]
      raise Exception('You forgot to set {}'.format(missing))
    main(file1, file2, outputfile)
  except Exception as e:
    print e.message
    exit(1)
