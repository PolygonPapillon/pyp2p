import argparse

'''Argument parsing'''
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='The selected file to be sent', type=str)
parser.add_argument('-cs', '--chunksize', help='Set the chunk size(kb)', type=int)
parser.add_argument('-t', '--target', help='The target recipient', type=str)
group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--listen', help='Listen for incoming files', action='store_true')
group.add_argument('-s', '--send', help='Send a file to a listener', action='store_true')
args = parser.parse_args()


if __name__ == '__main__':

    pass
