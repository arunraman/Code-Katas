import random, time
i = 1000

while True:
    with open('access.log', 'a') as F:
        log_template = str(random.getrandbits(30)) + " " + str(random.choice([100,101,102,200,201,202,203,204,300,304
                                                                         ,400,401,402,500])) + " " + '/foo' + "\n"
        F.write(log_template)
        F.close()
        time.sleep(1)
