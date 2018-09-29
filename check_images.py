#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/check_images.py
#

import os
from os import listdir
from time import time
import argparse


def main():

    # Set start time
    start_time = time()

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

    # Prints overall runtime in format hh:mm:ss
    print('\nTotal Elapsed Runtime:', str(int((tot_time/3600))) + ":" + str(int(((tot_time / 3600)/60))) +
          ":" + str(int(((tot_time % 3600) % 60))))


placeholder_dir = r'C:\Users\hchan\PycharmProjects\Image-Classifier-Lab'
placeholder_model = 'vgg'
placeholder_pet_name_file = 'dognames.txt'
pet_images_folder_name = 'pet_images'


def get_input_args(get_input_dir, get_input_model, get_input_pet_name_file):

    # Stores inputs into shorter text
    gia_ins = [get_input_dir, get_input_model, get_input_pet_name_file]

    # Creates parse processes function inputs
    gia_parser = argparse.ArgumentParser()

    # Adds arguments to parser
    # Necessary to parse args so python will recognize them as strings, other wise function inputs will be type<bytes>
    gia_parser.add_argument('--dir', type=str, default='/Users/adonisvasquez/PycharmProjects/werk',
                            help='Path to folder')
    gia_parser.add_argument('--arch', type=str, default='vgg',
                            help='chosen model')
    gia_parser.add_argument('--petfile', type=str, default='dognames.txt',
                            help='text file that has dognames')

    # Parses arguments with function inputs
    gia_parse_the_args = gia_parser.parse_args(['--dir', gia_ins[0], '--arch', gia_ins[1], '--petfile', gia_ins[2]])
    # Gets the values from argument parse in the form of a dictionary
    gia_parse_args_dic = vars(gia_parse_the_args)
    # Creates a vector of strings for for dictionary values (argument entries)
    gia_parse_args_data = tuple(gia_parse_args_dic.values())

    # Creates variables to pass through function
    gia_parse_args_dir = gia_parse_args_data[0]
    gia_parse_args_arch = gia_parse_args_data[1]
    gia_parse_args_pet_file = gia_parse_args_data[2]

    # Function will output three variables
    return gia_parse_args_dir, gia_parse_args_arch, gia_parse_args_pet_file


# Runs function and assigns three variables to the three outputs (returns) of get_input_args
used_dir, used_arch, used_dog_name_file = get_input_args(placeholder_dir, placeholder_model, placeholder_pet_name_file)
print('Outputs of get_input_args :' "\n", used_dir, "\n", used_arch, "\n", used_dog_name_file)


def get_pet_labels(get_pet_labels_dir, get_pet_labels_pet_file):

    gpl_ins = [get_pet_labels_dir, get_pet_labels_pet_file]

    gpl_parser = argparse.ArgumentParser()
    gpl_parser.add_argument('--dir', type=str, default='/Users/adonisvasquez/PycharmProjects/werk',
                            help='Path to folder')
    gpl_parser.add_argument('--petfile', type=str, default='dognames.txt',
                            help='text file that has dognames')

    # Parses arguments with function inputs
    gpl_parse_the_args = gpl_parser.parse_args(['--dir', gpl_ins[0], '--petfile', gpl_ins[1]])
    # Gets the values from argument parse in the form of a dictionary
    gpl_parse_args_dic = vars(gpl_parse_the_args)
    # Creates a vector of strings for for dictionary values (argument entries)
    gpl_parse_args_data = tuple(gpl_parse_args_dic.values())

    # Creates variables to pass through function
    gpl_parse_args_dir = gpl_parse_args_data[0]
    gpl_parse_args_pet_file = gpl_parse_args_data[1]

    # Retrieves file names from folder pet_images | tuple makes filename_list hashable (usable in for loops)
    filename_list = tuple(listdir(os.path.join(gpl_parse_args_dir, pet_images_folder_name)))
    # Joins the strings into a usable format (#justwindowsthings)
    pet_names_initial = open(os.path.join(gpl_parse_args_dir, gpl_parse_args_pet_file), 'r')
    # Reads text file and separates long string by new lines
    pet_name_list = tuple(pet_names_initial.read().splitlines())
    # Closes the file to preserve memory
    pet_names_initial.close()

    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist
    pet_dic_keys = filename_list
    pet_dic_values = pet_name_list

    # Pairs file names to pet names in a dictionary
    pet_dic = dict()
    for i in range(0, len(pet_dic_keys), 1):
        if pet_dic_keys[i] not in pet_dic:
            pet_dic[pet_dic_keys[i]] = pet_dic_values[i]
        else:
            print("** Warning: Key=", pet_dic_keys[i],
                  "already exists in pet_dic with value =", pet_dic[pet_dic_keys[i]])

    return pet_dic


# Runs get_pet_labels with outputs of get_input_args
answers_dic = get_pet_labels(used_dir, used_dog_name_file)

# TODO: 4. Define classify_images() function to create the classifier
# labels with the classifier function using in_arg.arch, comparing the
# labels, and creating a dictionary of results (result_dic)


def classifying_images(classifying_images_dir, pet_dic_to_compare):

    ci_ins = [classifying_images_dir, pet_dic_to_compare]
    test_image_paths = list()

    ci_parser = argparse.ArgumentParser()
    ci_parser.add_argument('--dir', type=str, default='/Users/adonisvasquez/PycharmProjects/werk',
                           help='Path to folder')

    # Parses arguments with function inputs
    ci_parse_dir = ci_parser.parse_args(['--dir', ci_ins[0]])
    ci_parse_dict = ci_ins[1]

    # Gets project directory from argument parse in the form of a tuple
    ci_parse_args_dir = tuple(vars(ci_parse_dir).values())
    # Converts tuple entry into string, I don't know why
    ci_parse_args_dir = ci_parse_args_dir[0]
    # Creates list of pet image file names
    ci_filename_list = tuple(listdir(os.path.join(ci_parse_args_dir, pet_images_folder_name)))

    # Creates a list of paths to images
    for i in range(len(ci_filename_list)):

        # Get i-th image file path (point at each image)
        test_image_paths.append(os.path.join(
            os.path.join(ci_parse_args_dir, pet_images_folder_name), ci_filename_list[i]))

    # Creates matching list of labels for each file
    for i in range(len(ci_filename_list)):

        

    #get pet image label

    #plug file directory into Model and record output (classiferlabel)

    #compare labels

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

classifying_images(used_dir, answers_dic)

#result_dic = classify_images(in_arg.dir, answers_dic, in_arg.arch)

#print("194" + in_args.dir)
#print("195" + answers_dic)
#print("196" + in_args.arch)

