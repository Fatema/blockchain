import functools
import hashlib
import json
import struct
import time

from tqdm import tqdm


# finding a valid block with difficulty 0.001
# difficulty = 0.001
difficulty = 7454968648263
target_1 = 0x00000000FFFF0000000000000000000000000000000000000000000000000000
current_target = target_1 / difficulty

# approximate hex representation
current_target_HEX = '0x{0:0{1}X}'.format(int(current_target), 64)
print(current_target_HEX)

# An example block header - do not change any fields except nonce and coinbase_addr
example_block_header = {'height': 1478503,
                        'prev_block': '0000000000000da6cff8a34298ddb42e80204669367b781c87c88cf00787fcf6',
                        'total': 38982714093,
                        'fees': 36351,
                        'size': 484,
                        'ver': 536870912,
                        'time': 1550603039.882228,
                        'bits': 437239872,
                        'nonce': 0,                     #You may change this field of the block
                        'coinbase_addr': 'mmgw12',     #You should change this field of the block to your studentID
                        'n_tx': 2,
                        'mrkl_root': '69224771b7a2ed554b28857ed85a94b088dc3d89b53c2127bfc5c16ff49da229',
                        'txids': ['3f9dfc50198cf9c2b0328cd1452513e3953693708417440cd921ae18616f0bfc', '3352ead356030b335af000ed4e9030d487bf943089fc0912635f2bb020261e7f'],
                        'depth': 0}


def timeit(func):
    @functools.wraps(func)
    def newfunc(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        elapsedTime = time.time() - startTime
        print('function [{}] finished in {} ms'.format(
            func.__name__, int(elapsedTime * 1000)))
    return newfunc


@timeit
def findValidBlock():
    # approximate range to find the nonce -> 5*4+2 = 22 leading zeros so around 2**22 hashes expected -> set range to 1e7 as upper limit
    for i in range(int(1e7)):
        example_block_header['nonce'] = i

        # Simplified conversion of block header into bytes:
        block_serialised = json.dumps(example_block_header, sort_keys=True).encode()

        # Double SHA256 hashing of the serialised block
        block_hash = hashlib.sha256(hashlib.sha256(block_serialised).digest()).hexdigest()

        # find valid block for the current difficulty 0.001
        if int(block_hash, 16) < current_target:
            print('Hash with nonce ' + str(example_block_header['nonce']) + ': ' + block_hash)
            break

# findValidBlock()

# found valid block at nonce 6162644
