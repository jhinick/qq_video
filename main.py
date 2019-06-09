



appName_to_processName = {
    '__test__': 'QQLive.exe',
    "腾讯视频": 'QQLive.exe',           # There are two processes with this name
    'QQLiveBrowser': 'QQLiveBrowser.exe',
}


def get_pid_from_processName(_processName=appName_to_processName.get('__test__')):
    """
    This function is to return all PID corresponding to the specified process name.
    :param _processName: Not application name, process name must be founded in Task_Manager.
    :return: A list of PID
    """
    import subprocess
    sub_proc = subprocess.run('tasklist', capture_output=True)
    sub_proc = sub_proc.stdout.decode('ASCII')
    table = [line.split() for line in sub_proc.split('\r\n')]
    if type(_processName) is str or int:
        '''There is only one process to process.'''
        _return = []
        for i in table:
            if str(_processName) in i:
                _return.append(i[1])
    else:
        '''There is a list of processes to process.'''
        pass


def get_port_from_PID(_PID):
    """
    Get all port numbers, including TCP, UDP etc, of the process of _PID
    :param _PID: A number or string of number
    :return: A list of port info, item example: ['TCP', '192.168.1.107:32574', '113.96.200.28:11863', 'CLOSE_WAIT', '15176']
    """
    import subprocess
    sub_proc = subprocess.run('netstat -aon', capture_output=True)
    sub_proc = sub_proc.stdout.decode('ASCII')
    table = [line.split() for line in sub_proc.split('\r\n')]
    _return = []
    for i in table[3:]:
        if len(i) != 0:
            if str(_PID) == i[-1]:
                _return.append(i)
    return _return




if __name__ == '__main__':
    pid = get_pid_from_processName()
    get_port_from_PID(pid[0])