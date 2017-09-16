from collections import defaultdict
import os

CHECKPOINT_FILE='/Users/aruraman/GitHub/Code-Katas/Interview/Real World/Q/gmetric_status.chk'
ACCESS_LOG='/Users/aruraman/GitHub/Code-Katas/Interview/Real World/Q/access.log'

def gmetric(stat_name, stat_value):
    print stat_name, stat_value

def write_checkpoint(position):
    with open(CHECKPOINT_FILE, 'w') as chkpoint_file:
        chkpoint_file.write(str(position))

def read_checkpoint():
    with open(CHECKPOINT_FILE) as chkpoint_file:
        return chkpoint_file.read()

def read_lines(F, checkpoint_position):
    F.seek(checkpoint_position)
    for line in F:
        line = line.strip()
        if not line:
            continue
        yield line

def main():
    statuses = defaultdict(int)
    access_log_size = os.path.getsize(ACCESS_LOG)
    # If the chkpoint doesn't exist just write a checkpoint for the current
    # size and skip this minute.
    if not os.path.exists(CHECKPOINT_FILE):
        write_checkpoint(access_log_size)
        return

    chkpoint_position = int(read_checkpoint())

    if chkpoint_position > access_log_size:
        # File must have been rotated. Start from beginning.
        chkpoint_position = 0

    with open(ACCESS_LOG) as access_log:
        #print access_log.seek(chkpoint_position)
        for line in read_lines(access_log, chkpoint_position):
            status = line.split(' ')[1]
            statuses[status] += 1
            write_checkpoint(access_log.tell())
            gmetric('requests_qps', sum(statuses.values()) / 60)
            for status, value in statuses.items():
                gmetric('request_{}_qps'.format(status), value / 60)

main()