import os
from random import choice, randint
from string import ascii_letters

import click


@click.command()
@click.option('-d', '--depth', default=1, help='depth of files and folders makind')
@click.option('--max-letter-count', default=10, help='max letters of files and directories names ')
@click.option('--max-file-count', default=10, help='max number of files in ond directory')
@click.option('--max-directory-count', default=10, help='max number of directories in one directory')
@click.argument('root')
def main(
    root, 
    depth, 
    max_letter_count, 
    max_file_count, 
    max_directory_count):

    # TODO check parameters if they are valid

    # running BFS algorithm on directory to create files and directories
    dir_queue = []

    # add root direcotry as first directory to start creating files
    dir_queue.append((root,0))

    while(len(dir_queue)):
        cur_dir, cur_depth = dir_queue.pop()
        cur_dir = os.path.join(cur_dir)

        # create directory if it's not existed
        if not os.path.exists(cur_dir):
            os.makedirs(cur_dir) 
        
        # create files
        for i in range(randint(1, max_file_count)):

            # generate files name
            file_name = ''.join(choice(ascii_letters) for i in range(randint(1, max_letter_count))) + ".txt"
            file_path = os.path.join(cur_dir, file_name)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("You know the rules and so do I\n")
            print(file_name)


        # create directories
        # add directory to dir_queue

        pass


if __name__ == "__main__":
    main()