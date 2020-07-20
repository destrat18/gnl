import click


@click.command()
@click.option('--depth', '-d', default=1, help='number of greetings')
@click.argument('dir_name')
def gnl(dir_name, depth):
    #TODO list all files

    #create folders and move files
    pass

if __name__ == "__main__":
    gnl()
