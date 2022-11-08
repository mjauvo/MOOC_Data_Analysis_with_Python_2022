#!/usr/bin/env python3

# Gets a filename as a parameter, read through the lines
# from this file each line containing a filename, and
# finds the file extension for each file name.
def file_extensions(filename):
    no_file_extension_list = []
    file_extension_dict = {}

    with open(filename) as file:
        for line in file:
            if '.' in line:
                file_parts = line.split(".")
                ext = file_parts[-1].replace("\n", "")
                if ext in file_extension_dict.keys():
                    file_extension_dict[ext].append(line.replace("\n", ""))
                else:
                    file_extension_dict[ext] = [line.replace("\n", "")]
            else:
                no_file_extension_list.append(line.strip())

    return (no_file_extension_list, file_extension_dict)

def main():
    no_extension, extension = file_extensions("filenames.txt")
    print(f"{len(no_extension)} files with no extension")
    for ext in extension:
        print(f"{ext} {len(extension[ext])}")

if __name__ == "__main__":
    main()
