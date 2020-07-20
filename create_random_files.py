import os
from random import choice, randint
from string import ascii_letters

import click


@click.command()
@click.option('-d', '--depth', default=3, help='depth of files and folders makind')
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
    dir_queue.append((os.path.join(root),0))

    while(len(dir_queue)):
        cur_dir, cur_depth = dir_queue.pop()
        print(cur_dir, cur_depth)

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
        
        # create directories
        for i in range(randint(1, max_directory_count)):

            # generate directory name
            dir_name = ''.join(choice(ascii_letters) for i in range(randint(1, max_letter_count)))
            dir_path = os.path.join(cur_dir, dir_name)
            if cur_depth + 1 < depth:
                # add directory to dir_queue
                dir_queue.append((dir_path, cur_depth+1))


if __name__ == "__main__":
    main()