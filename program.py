import filecmp
import itertools
import os
from os import walk


def main():
    #/Volumes/MORTON/Pictures/Lightroom Masters
    rootdir = os.path.join('/', 'Volumes', 'MORTON', 'Pictures', 'Lightroom Masters')

    if not os.path.exists(rootdir) or not os.path.isdir(rootdir):
        print('Directory {} does not exist '.format(rootdir))

    for (dirpath, dirnames, filenames) in walk(rootdir):
        #print(dirpath)
        for file1, file2 in itertools.combinations(filenames, 2):
            file1prefix = get_filename_prefix(file1)
            file1fullpath = os.path.join(dirpath,file1)
            file2prefix = get_filename_prefix(file2)
            file2fullpath = os.path.join(dirpath, file2)

#            if file1prefix == file2prefix and os.path.isfile(file1fullpath) and os.path.isfile(file2fullpath):
            if os.path.isfile(file1fullpath) and os.path.isfile(file2fullpath):
                file_are_same = filecmp.cmp(os.path.join(file1fullpath),file2fullpath)
                if file_are_same and os.path.isfile(file1fullpath) and os.path.isfile(file2fullpath):
                    print('{} name is equivalent to {}'.format(file1, file2))
                    if(len(file1) > len(file2)):
                        print('Delete {}'.format(file1fullpath))
                        os.remove(file1fullpath)
                    else:
                        print('Delete {}'.format(file2fullpath))
                        os.remove(file2fullpath)


def get_filename_prefix(file):
    return file.split('-')[0].split('.')[0]


if __name__ == '__main__':
    main()
