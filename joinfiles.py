#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from os import listdir, path, mkdir
from shutil import copy2


def directoryScan(local_path):
	directory = listdir(local_path)
	directory.sort()

	folders = []
	files = []
	for d in directory:
		if not any(local_path+'/'+d in ignore for ignore in ignore_list):
			if path.isdir(local_path+'/'+d):
				folders.append(d)
			elif path.isfile(local_path+'/'+d):
				files.append(d)

	return {'folders': folders, 'files': files}


def appendFiles(local_path):
	scan_result = directoryScan(local_path)
	global count

	for f in scan_result['files']:
		origin = local_path+'/'+f
		extension = path.splitext(origin)[1]
		target = './joined_files/%s%s' % (('000000'+str(count))[-6:], extension)
		
		copy2(origin, target)
		count += 1


	for f in scan_result['folders']:
		appendFiles(f)


ignore_list = ['./joined_files', './joinfiles.py']

count = 0

mkdir('joined_files')

appendFiles('.')