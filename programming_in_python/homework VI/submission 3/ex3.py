import os
import glob


def get_abs_paths(root_path: str, ext_filter: str=None) ->list:
    root_path=os.path.abspath(root_path)

    # checking if root_path is a directory
    if os.path.isdir(root_path):
        abs_filename=os.path.abspath(root_path)

        # checking if path exits
        if os.path.exists(abs_filename):
            found_files=[]

            # all files included
            if ext_filter is None:
                file_path=os.path.join("**","*.*")
                directory = os.path.join(abs_filename,file_path)
                found_files = glob.glob(directory, recursive=True)

            # only the files with that extension included
            else:
                if ext_filter!=".txt" and ext_filter!=".py":
                    raise ValueError("the extension provided it's not right")
                file_path="*"+ext_filter
                directory=os.path.join(abs_filename,"**",file_path)
                found_files = glob.glob(directory,recursive=True)

            if len(found_files)!=0:
                found_files.sort()
            return found_files
        else:
            raise ValueError("path does not exist")
    else:
        raise ValueError("the root path is not a directory")
