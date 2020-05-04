'''
Determine whether you want the number of the Fibonacci term listed
'''
import time
from pathlib import Path
import argparse
import os
numbered = False

'''
The file size limit of fib.txt where LIMIT is the power of 10 in bytes
ex. LIMIT = 9 means 10^9 bytes which is a file size of 1 gigabyte
'''
limit = 5

'''
Adds a space in between each iteration for easy text file reading
'''
newline = True

# ap = argparse.ArgumentParser(description='Generate Fibonacci Sequence')
# ap.add_argument("--limit",
# 	help="max output file size in 10 to the power of limit")
# ap.add_argument("--newline",
# 	help="add a new line between each iteration")
# ap.add_argument("--numbered",
# 	help="add a new line between each iteration")
# args = vars(ap.parse_args())

desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
path = desktop / Path(r'fibonacci-generator-output.txt')


def main():
    if os.path.exists(path):
        print('================\n OLD FILE FOUND\n----------------\n{}\n================\n'.format(path))
        os.remove(path)
        print('==============\n FILE DELETED\n==============\n')

    f = open(path, "a")

    def fib_gen():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    # courtesy of https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                         (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' %
              (prefix, bar, percent, suffix), end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()

    fs = fib_gen()
    next(fs)
    print('==================\n START GENERATION\n==================\n')
    i = 0

    while True:
        if numbered:
            f.write("{} TERM:\n".format(i))
        current_size = os.stat(path).st_size
        f.write("{}\n".format(str(next(fs))))
        if newline:
            f.write('\n')
        printProgressBar(current_size, 10**limit,
                         prefix='Progress:', suffix='Complete', length=50)
        i -= -1
        if os.stat(path).st_size >= 10**limit:
            print("\n\n======================================\n   LIMIT OF {} BYTES REACHED\n--------------------------------------".format(10**limit))
            break
    f.close()

start_time = time.time()
main()
print("   %s seconds\n======================================" % (time.time() - start_time))
