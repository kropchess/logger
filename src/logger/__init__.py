from .main import Logger

log = None


def init(demo=False, **kwargs):
    log = Logger(**kwargs)
    if demo:
        import time
        time.sleep(0.5)
        log.info('main', 'starting!')
        time.sleep(0.5)
        log.good('module1')
        time.sleep(2)
        log.bad ('module2', excepto='Demo_Module_2')
        log.para()
        time.sleep(0.1)
        log.good('module3_1')
        time.sleep(0.1)
        log.good('module3_2')
        time.sleep(0.1)
        log.bad('module3_3')
        log.bad('module3_4', ImportError('DEMO').__str__())
        time.sleep(1)
        log.unpara()
        import random
        time.sleep(3)
        log.info('db', 'Connecting!')
        time.sleep(random.randint(968, 1056)/1000)
        log.warning('db', 'db ping is ' + random.randint(968, 1056).__str__())
        time.sleep(1)
        log.error('db', 'Connect Fail!!')
