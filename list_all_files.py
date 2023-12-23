import os

class ListFiles:

    def list_in_folder(self, folder_dir:str) -> set:
        "Input folder directory, returns list of files in folder and subfolders in notation (filename, directory, folder depth)"
        if not os.path.isdir(folder_dir):
            print("Provided directory does not exist.")
            return None

        files_in_directory = set()
        folder_depth = 0
        def recur_check(folder_dir:str, files_set:set, folder_depth:int):
            if not os.listdir(folder_dir):
                return files_set
                        
            for item in os.listdir(folder_dir):
                if not os.path.isdir(os.path.join(folder_dir, item)):
                    files_set.add((item, folder_dir, folder_depth))
                else:
                    folder_depth += 1
                    recur_check(os.path.join(folder_dir, item),files_set, folder_depth)    
                    folder_depth -= 1
            
            return files_set

        files_in_directory = recur_check(folder_dir, files_in_directory, folder_depth)

        return files_in_directory


if __name__ == '__main__':

    list_files = ListFiles()
    directory = r''
    if not directory:
        directory = input('type directory to list all files in directory and subdirectories.')
    print(list_files.list_in_folder(directory))