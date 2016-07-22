#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import csv
import collections


### COMPARISON THING ###
x = 0

current_directory = os.listdir(os.getcwd())
csv_files = filter(lambda file: '.csv' in file, current_directory)
for files in csv_files:
	if '.csv' in files:
		print('%s -----> %s' % (x, files))
		x += 1

choice = raw_input("Which file do you want to use as the OLD file ? ->>>")  ## checki1.csv
past_file = csv_files[int(choice)]
print "Using {} as the OLD file".format(past_file)
choice = raw_input("Which file do you want to use as the NEW file ? ->>>")  ## cheki2.csv
recent_file = csv_files[int(choice)]
print "Using {} as the OLD file".format(recent_file)
print 'Comparing {} to {}'.format(past_file, recent_file)


### CLEANING CSV FILES (REMOVING GET PARAMETERS)

def remove_get_parameters(fname):
	with open(fname, "r") as f:
		lines = (line.rstrip() for line in f)
		altered_lines = [line.split("?")[0] for line in lines]
	with open(fname + ".tmp", "w") as f:
		f.write('\n'.join(altered_lines) + '\n')


def find_dupes(data_set, data_list):
	seen = set()
	for n in data_list:
		if n in seen:
			print "duplicate:", n
		else:
			seen.add(n)

remove_get_parameters(recent_file)
remove_get_parameters(past_file)

s_now = frozenset(tuple(row) for row in csv.reader(open(recent_file + ".tmp", 'r'), delimiter=';'))  ## RECENT
s_past = frozenset(tuple(row) for row in csv.reader(open(past_file + ".tmp", 'r'), delimiter=';'))  ## ANCIEN

l_now = [row[0] for row in csv.reader(open(recent_file + ".tmp", 'r'), delimiter=';')]
l_past = [row[0] for row in csv.reader(open(past_file + ".tmp", 'r'), delimiter=';')]


total_now_dupes = len(l_now)
total_past_dupes = len(l_past)
tot_now_set = len(s_now)
tot_past_set = len(s_past)

print("Total {} file with duplicates: {}".format(recent_file, total_now_dupes))
print("Total {} file with duplicates: {}".format(past_file, total_past_dupes))
print("Total {} file without duplicates: {}".format(recent_file, tot_now_set))
print("Total {} file without duplicates: {}".format(past_file, tot_past_set))
print("Duplicates in file {} : {}".format(recent_file, total_now_dupes - tot_now_set))
print("Duplicates in file {} : {}".format(past_file, total_past_dupes - tot_past_set))
c_now = collections.Counter(l_now)
c_past = collections.Counter(l_past)
# print c_now
# print c_past
# find_dupes(s_now, l_now)
#find_dupes(s_past, l_past)

# print "OLD file without duplicates: {} links".format(len(s_past))
# print "NEW file without duplicates: {} links".format(len(s_now))

added = list()

added_lines = s_now - s_past
for row in added_lines:
	added.append(";".join(row))

removed = list()

removed_lines = s_past - s_now
for row in removed_lines:
	removed.append(";".join(row))

c = csv.writer(open("CHANGELOG.csv", "a"), delimiter=";")
for item_added in added:
	c.writerow(['ADDED', item_added])

for item_removed in removed:
	c.writerow(['REMOVED', item_removed])

## Removing temporary files
os.remove(recent_file + ".tmp")
os.remove(past_file + ".tmp")
