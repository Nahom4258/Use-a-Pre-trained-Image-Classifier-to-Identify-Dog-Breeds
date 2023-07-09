#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Nahom Habtamu
# DATE CREATED: July 7, 2023                      
# REVISED DATE: July 9, 2023
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    results_dic = dict()
    
    filenames = listdir(image_dir)
    pet_labels = [''] * len(filenames)
    
    # create the corrected pet labels
    for i in range(len(filenames)):
        # set to lower case
        low_label = filenames[i].lower()
        # split using '_'
        word_list = low_label.split('_')
        
        new_pet_name = ''
        for word in word_list:
            if word.isalpha():
                new_pet_name += word + " "
                
        new_pet_name = new_pet_name.strip()
        
        # set the new pet name to the pet labels list
        pet_labels[i] = new_pet_name
    
    # create the dictionary
    for i in range(len(filenames)):
        # ignore if the file is hidden
        if filenames[i][0] != '.':
            results_dic[filenames[i]] = [pet_labels[i]]
        
    return results_dic
