# standard libraries
import sys

from factory.CompressFactory import CompressFactory

if __name__ == '__main__':
    CompressFactory.build(sys.argv[1:]).execute()
