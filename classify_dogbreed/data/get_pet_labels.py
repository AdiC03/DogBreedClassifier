# PROGRAMMER: Adithya Chintala
# DATE CREATED:                                  
# REVISED DATE: 6/21
# PURPOSE: Created the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).

# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    in_files = listdir(image_dir)

    results_dic = {}
    
    for idx in range(0, len(in_files), 1):
      if in_files[idx][0] != ".":
        curr_index = in_files[idx].index('.')
        while not in_files[idx][curr_index].isalpha():
          curr_index -= 1
        pet_label = in_files[idx][:curr_index + 1].replace("_", " ").lower()

        if in_files[idx] not in results_dic:
          results_dic[in_files[idx]] = [pet_label]
              
        else:
            print("** Warning: Duplicate files exist in directory:", 
                  in_files[idx])


    return results_dic