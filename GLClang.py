from run_system_functions import *
#create functions
def writedata_pre(readenfile, writeenfile):
    """this function reads writeenfile and writes the data of the writeenfile
    in readenfile(this function copy the data in writeenfile and paste it in readenfile)."""
    with open(f'{writeenfile}', 'r') as la2:
        x = la2.read()
    with open(f'{readenfile}', 'w') as la:
        la.write(f'{x}')
    la.close()
    la2.close()
def readdata_pre(readenfile, writeenfile):
    """this function reads readenfile and writes the data of the readenfile
        in writeenfile(this function copy the data in readenfile and paste it in writeenfile)."""
    with open(f'{readenfile}', 'r') as la2:
        x = la2.read()
    with open(f'{writeenfile}', 'w') as la:
        la.write(f'{x}')
    la.close()
    la2.close()
def clearall_pre(file1,file2):
    """this function clear all data of file1 and file2"""
    with open(f'{file1}', 'w') as la2:
        la2.write('')
    with open(f'{file2}', 'w') as la:
        la.write('')
    la.close()
    la2.close()
def clear_pre(file):
    """this function clear all data of file1"""
    with open(f'{file}', 'w') as la:
        la.write('')
    la.close()
def writedata():
    """this function reads main.gcf or main.PLFF and writes the data of the main.gcf or main.PLFF
        in lacodeasavea.txt(this function copy the data in main.gcf or main.PLFF and paste it in lacodeasavea.txt)."""
    with open('main.gcf', 'r') as la2:
        x = la2.read()
    with open('lacodeasavea.txt', 'w') as la:
        la.write(f'{x}')
    la.close()
    la2.close()
def readdata():
    """this function reads lacodeasavea.txt and writes the data of the lacodeasavea
            in main.gcf or main.PLFF (this function copy the data in lacodeasavea.txt and paste it in main.gcf or main.PLFF)."""
    with open('lacodeasavea.txt', 'r') as la2:
        x = la2.read()
    with open('main.gcf', 'w') as la:
        la.write(f'{x}')
    la.close()
    la2.close()
def clearall():
    """this function clear all data of lacodeasavea.txt and main.gcf or main.PLFF"""
    with open('lacodeasavea.txt', 'w') as la2:
        la2.write('')
    with open('main.gcf', 'w') as la:
        la.write('')
    la.close()
    la2.close()
def clear1():
    """this function clear all data of main.gcf or main.PLFF"""
    with open('main.gcf', 'w') as la:
        la.write('')
    la.close()
def clear2():
    """this function clear all data of lacodeasavea.txt"""
    with open('lacodeasavea.txt', 'w') as la2:
        la2.write('')
    la2.close()
def run_pre(programminglanguage,filename,run_type):
    """this function runs filename that is .gcf or .PLFF and this function
can compile the code or compile and run the code"""
    if run_type == 'True':
        CAR = 1
        run(programminglanguage,CAR,True,False,filename,'','',False,True,False)
    if run_type == 'False':
        CAR = 2
        run(programminglanguage, CAR, True, False, filename, '', '', False, True, False)
def allrun_pre(filename,run_type,runorder=None):
    """this function runs filename that is .gcf or .PLFF and this function
can compile the code or compile and run the code"""
    if runorder is None:
        runorder = []
    if run_type == 'True':
        CAR = 1
        for i in runorder:
            run(i,CAR,True,False,filename,'','',False,True,False)
    if run_type == 'False':
        CAR = 2
        for i in runorder:
            run(i,CAR,True,False,filename,'','',False,True,False)
def parallelrun(programminglanguage:str,CAROCO:int,runned:bool,returned:bool,file_path:str='',code:str='',PRDF:str='',Parallelrun:bool=False,showrunmessage:bool=True,showmessageshowingwarnings:bool=False):
    run(programminglanguage,CAROCO,runned,returned,file_path,code,PRDF,Parallelrun,showrunmessage,showmessageshowingwarnings)
def parallelrunfilesgenrator(filename:str,fileformat:str):
    parallelrunfilesgen(filename,fileformat)
def GLC_filegenrator(file_name_without_file_format:str,Python_PRDF:bool=False,C_PRDF:bool=False,Java_PRDF:bool=False,JS_PRDF:bool=False,HTML_PRDF:bool=False,Batch_PRDF:bool=False,Kotlin_PRDF:bool=False):
    GLCfilegenrator(file_name_without_file_format,Python_PRDF,C_PRDF,Java_PRDF,JS_PRDF,HTML_PRDF,Batch_PRDF,Kotlin_PRDF)
def GLC_filegenrator2(file_name_without_file_format:str,Python_PRDF:bool=False,C_PRDF:bool=False,Java_PRDF:bool=False,JS_PRDF:bool=False,HTML_PRDF:bool=False,Batch_PRDF:bool=False,Kotlin_PRDF:bool=False):
    GLCfilegenrator2(file_name_without_file_format,Python_PRDF,C_PRDF,Java_PRDF,JS_PRDF,HTML_PRDF,Batch_PRDF,Kotlin_PRDF)
def restart():
    """this function restarts main.gcf or main.PLFF"""
    oldb = open('main.gcf', 'w')
    oldb.write('')
    oldb.close()
def restart_pre(filename):
    """this function restarts filename that is .gcf or .PLFF"""
    oldb = open(f'{filename}', 'w')
    oldb.write('')
    oldb.close()
def run_code(filename):
    """this function runs code like python files and C files and all other programming
    languages supported by GLC
    note:this function don't compile than by using GLC that means no function mapping
    or things like that it only compile and runs or only compile the file with cmd commands"""
    data = filename
    if '.py' in data:
        os.system(f'python {data}')
    if '.c compile' in data:
        data1 = data[:-8]
        os.system(f'gcc {data1}')
    if '.c run' in data:
        data1 = data[:-4]
        os.system(f'gcc {data1} & a.exe')
    if '.c r_compiled' in data:
        os.system('a.exe')
    if '.java' in data:
        os.system(f'java {data}')
    if '.kt compile' in data:
        data1 = data[:-8]
        os.system(f'kotlinc {data1}')
    if '.kt run' in data:
        data1 = data[:-4]
        data2 = data1[0].upper() + data1[1:]
        data3 = data2[:-2] + data2[-2:].upper()
        data4 = data3[:-3] + data3[-2:].upper()
        os.system(f'kotlinc {data1} & kotlin {data4}.class')
    if '.kt r_compiled' in data:
        data1 = data[:-11]
        data2 = data1[0].upper() + data1[1:]
        data3 = data2[:-2] + data2[-2:].upper()
        data4 = data3[:-3] + data3[-2:].upper()
        os.system(f"kotlin {data4}.class")
    if '.bat' in data:
        os.system(f"{data}")
    if '.js' in data:
        os.system(f"node {data}")
    if '.html' in data:
        os.system(f"{data}")
#basic run function that uses 5 another functions
def allbasicrun_pre(runorder,readenfile,writeenfile,runtype):
    """this function uses writedata and runmain,restart,readdata,clear2 functions to do run for
    main.gcf or main.PLFF without problems"""
    writedata_pre(readenfile, writeenfile)
    allrun_pre(writeenfile,runtype,runorder)
    restart_pre(writeenfile)
    readdata_pre(readenfile, writeenfile)
    clear_pre(readenfile)
def basicrun_pre(programminglanguage,readenfile,writeenfile,runtype):
    """this function uses writedata_pre and run_pre,restart_pre,readdata_pre,clear_pre functions to do run for
    filename that is .gcf or .PLFF without problems"""
    writedata_pre(readenfile, writeenfile)
    run_pre(programminglanguage,writeenfile, runtype)
    restart_pre(writeenfile)
    readdata_pre(readenfile, writeenfile)
    clear_pre(readenfile)