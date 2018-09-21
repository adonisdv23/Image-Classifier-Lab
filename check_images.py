#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/check_images.py
#                                                                             
# TODO: 0. Fill in your information in the programming header below
# PROGRAMMER: Adonis Vasquez
# DATE CREATED: August 31, 2018
# REVISED DATE:             <=(Date Revised - if any)
# REVISED DATE: 05/14/2018 - added import statement that imports the print 
#                           functions that can be used to check the lab
# PURPOSE: Check images & report results: read them in, predict their
#          content (classifier), compare prediction to actual value labels
#          and output results
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules

from os import listdir

# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports time() and sleep() functions from time module
from time import time, sleep

# Import argparse python module
import argparse

# Importas only listdir functino from OS module
from os import listdir

# Imports classifier function for using pretrained CNN to classify images
from classifier import classifier

# Main program function defined below
#wait = input("enter")
def main():
    # TODO: 1. Define start_time to measure total program runtime by
    # Set start time
    start_time = time()

    #sleep(22)

    # Sets end time
    end_time = time()

    # Computes overall runtime in seconds
    tot_time = end_time - start_time

    # Computes overall runtime in hours
    hours = int((tot_time/3600))

    # Computes overall runtime in minutes
    minutes = int(((tot_time / 3600)/60))

    # Computes overall runtime in seconds
    seconds = int(((tot_time % 3600) % 60))

    #print('\nTotal Elapsed Runtime:', tot_time, "in seconds"

    # Prints overall runtime in format hh:mm:ss
    print('\nTotal Elapsed Runtime:', str(int((tot_time/3600))+":"+int(((tot_time / 3600)/60))
    )+":"+int(((tot_time % 3600) % 60)))

    # TODO: 2. Define get_input_args() function to create & retrieve command
    # line arguments

dir     = '/Users/adonisvasquez/PycharmProjects/werk/pet_images/'
model   = 'vgg'
dogfile = "dognames.txt"

def get_input_args(dir, model, dognames):

    # Creates parse
    parser = argparse.ArgumentParser()

    #Argument 1: that's a path to a folder
    parser.add_argument('--dir', type = str, default = '/Users/adonisvasquez/PycharmProjects/werk/pet_images/',
                        help = 'Path to folder')
    parser.add_argument('--arch', type=str, default='vgg',
                        help='chosen model')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='text file that has dognames')

    get_input_args.dir = dir
    #print(get_input_args.dir)
    # returns parsed argument collection
    print("a")
    print(get_input_args.dir)
    print("a")

#wait = input("enter")
# Assigns variable in_args to parse_args()
in_args = get_input_args(dir, model, dogfile)
print(in_args)

        # TODO: 3. Define get_pet_labels() function to create pet image labels by
    # creating a dictionary with key=filename and value=file label to be used
    # to check the accuracy of the classifier function

#wait = input("enter")
#def get_pet_labels(pet_images):
def get_pet_labels():
#pet_images, pet_name

    # Retrieve the filenames from folder pet_images/
    filename_list = listdir('/Users/adonisvasquez/PycharmProjects/werk/pet_images')
    get_pet_labels.filename_list = filename_list
    filename_list = tuple(filename_list)

    print(get_pet_labels.filename_list)
    filedata = open('/Users/adonisvasquez/PycharmProjects/werk/dognames.txt', 'r')
    pet_name_list = filedata.read().splitlines()
    filedata.close()
    pet_name_list = tuple(pet_name_list)

    # Print 10 of the filenames from folder pet_images/
    #print("\nPrints 10 filenames from folder pet_images/")
    #for idx in range(0, 10, 1):
    #    print("%2d file: %-25s" % (idx + 1, filename_list[idx]))

    # Creates empty dictionary named pet_dic
    #pet_dic = dict()
    #pet_dic = {}

    # determines number of items in dictionary
    ##items_in_dic = len(pet_dic)
    ##print("\nEmpty Dictionary pet_dic - n items=", items_in_dic)

    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist
    keys = filename_list
    values = pet_name_list
    #print(keys[0])
    #print(values[0])
    pet_dic = dict()
    for idx in range(0, len(keys), 1):
        if keys[idx] not in pet_dic:
            pet_dic[keys[idx]] = values[idx]
        else:
            print("** Warning: Key=", keys[idx],
                "already exists in pet_dic with value =", pet_dic[keys[idx]])

    # Iterating through a dictionary printing all keys & their associated values NOT DOING
    # print("\nPrinting all key-value pairs in dictionary pet_dic:")
    # for key in pet_dic:
    #     print("Key=", key, "   Value=", pet_dic[key])
    get_pet_labels.pet_dic = pet_dic

    #print("\nnewline")
    #print(pet_dic['cat_07.jpg'])
    #answers_dic = get_pet_labels(in_args.dir)
    #answers_dic = get_pet_labels()
    #return answers_dic

get_pet_labels()
answers_dic = get_pet_labels.pet_dic
#print(answers_dic)


directory = str(get_input_args.dir)
filename_list = get_pet_labels.filename_list
test_image = filename_list
print(filename_list[1])
for i in range(len(filename_list)):

    # get image file directory (point at each image)
    test_image[i] = [directory, filename_list[i]]

print(test_image[1])
print("a")
    # TODO: 4. Define classify_images() function to create the classifier
    # labels with the classifier function uisng in_arg.arch, comparing the
    # labels, and creating a dictionary of results (result_dic)
    #def classify_images():
#directory1 = in_args.dir()
#print(get_input_args.dir())

def classifying_images():

    directory2 = in_args.dir()
    print(directory2)
    for i in range(len(get_pet_labels.filename_list)):

        #get image file directory (point at each image)
        test_image[i] = [directory , get_pet_labels.filename_list[i]]

    print(test_image)
    print("a")
        #get pet image label

        #plug file directory into Model and record output (classiferlabel)

        #compare labels

    # Defines a dog test image from pet_images folder
    test_image = in_arg.dir
    #
    # # Defines a model architecture to be used for classification
    # # NOTE: this function only works for model architectures:
    #      'vgg', 'alexnet', 'resnet'
    model = "vgg"

    # Demonstrates classifier() functions usage
    # NOTE: image_classication is a text string - It contains mixed case(both lower
    # and upper case letter) image labels that can be separated by commas when a
    # label has more than one word that can describe it.
    image_classification = classifier(test_image, model)


#result_dic = classify_images(in_arg.dir, answers_dic, in_arg.arch)

#print("194" + in_args.dir)
#print("195" + answers_dic)
#print("196" + in_args.arch)

