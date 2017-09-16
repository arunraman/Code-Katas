import re, os, time, glob


ACCESS_LOG='/Users/aruraman/GitHub/Code-Katas/Interview/Real World/Q/access.log'
CHECKPOINT_FILE='/Users/aruraman/GitHub/Code-Katas/Interview/Real World/Q/gmetric_status.chk'


class Solution(object):
    def __init__(self):
        '''Initialize any data structures or variables needed for keeping track
        of the tasty bits we find in the log we are parsing.'''
        self.http_1xx = 0
        self.http_2xx = 0
        self.http_3xx = 0
        self.http_4xx = 0
        self.http_5xx = 0

        # Regular expression for matching lines we are interested in, and capturing
        # fields from the line (in this case, http_status_code).
        self.reg = re.compile(r'\s')
        self.result = []

    def generate_metrics(self):
        access_log_size = os.stat(ACCESS_LOG).st_size
        access_log_inode_num = os.stat(ACCESS_LOG).st_ino

        # The checkpoint point file is not created then
        # either the check point file is gone or
        # its starting for the first time
        if not os.path.exists(CHECKPOINT_FILE):
            self.write_checkpoint(0, access_log_inode_num)
            # First time will cause a spike So don't do anything
            return
        else:
            if time.time() - os.stat(CHECKPOINT_FILE).st_mtime <= 59:
                #print "The checkpoint file is very recent"
                chkpoint_position, inode_num = self.read_checkpoint()

                if inode_num != access_log_inode_num and chkpoint_position > access_log_size:
                    # File has rotated and we need to read from previous rotated file
                    ROTATED_ACCESS_LOG = self.get_file_name_of_rotated_access_log(inode_num)
                    # read from the rotated log
                    self.read_access_log(chkpoint_position, access_log_inode_num, ROTATED_ACCESS_LOG)
                    chkpoint_position = 0

            else:
                # Touch the checkpoint file and return
                os.utime(CHECKPOINT_FILE, None)
                return

        self.read_access_log(chkpoint_position, access_log_inode_num, ACCESS_LOG)

        print self.get_state()

    def write_checkpoint(self, position, access_log_inode_num):
        ACCESS_LOG_INFO = 'POSITION:{}\nINODE_NUM:{}'.format(position, access_log_inode_num)
        with open(CHECKPOINT_FILE, 'w') as chkpoint_file:
            chkpoint_file.write(ACCESS_LOG_INFO)

    def read_checkpoint(self):
        with open(CHECKPOINT_FILE) as chkpoint_file:
            for line in chkpoint_file.readlines():
                yield int(line.strip().split(':')[1])

    def read_lines(self, F, checkpoint_position):
        F.seek(checkpoint_position)
        for line in F:
            line = line.strip()
            if not line:
                continue
            yield line

    def get_file_name_of_rotated_access_log(self, inode_num):
        ROTATED_ACCESS_LOG = os.path.join(os.getcwd())
        access_log_files = [file for file in glob.glob(os.path.join(ROTATED_ACCESS_LOG, '*.log'))]
        access_log_files.sort(key=os.path.getmtime)
        return access_log_files[0]
        #for rotated_log in access_log_files:
        #    if os.stat(rotated_log).st_ino == inode_num:
        #        return rotated_log

    def read_access_log(self, chkpoint_position, access_log_inode_num, fileName):
        with open(fileName) as access_log:
            for line in self.read_lines(access_log, chkpoint_position):
                regMatch = self.reg.split(line)
                if regMatch:
                    status = int(regMatch[1])
                    if (status < 200):
                        self.http_1xx += 1
                    elif ((status >= 200) and (status < 300)):
                        self.http_2xx += 1
                    elif ((status >= 300) and (status < 400)):
                        self.http_3xx += 1
                    elif ((status >= 400) and (status < 500)):
                        self.http_4xx += 1
                    else:
                        self.http_5xx += 1
            self.write_checkpoint(access_log.tell(), access_log_inode_num)


    def get_state(self, duration = 60):
        '''Run any necessary calculations on the data collected from the logs
        and return a list of metric objects.'''

        self.duration = float(duration)

        return [
         ["http_1xx", (self.http_1xx / self.duration)],
         ["http_2xx", (self.http_2xx / self.duration)],
         ["http_3xx", (self.http_3xx / self.duration)],
         ["http_4xx", (self.http_4xx / self.duration)],
         ["http_5xx", (self.http_5xx / self.duration)]
        ]


S = Solution()
S.generate_metrics()


# crontab -e
# */1   *    *    *    *    python ganglia_qps.py