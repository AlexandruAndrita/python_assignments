import codecs
import subprocess


def check_encoding(encoding):
    try:
        codecs.lookup(encoding)
    except LookupError:
        print(f"The specified encoding '{encoding}' could not be found")
        return False
    return True

def check_program(program):
    try:
        p=subprocess.Popen([program])
        try:
            p.wait(timeout=0.01)
        except subprocess.TimeoutExpired:
            p.kill()
            return True
    except FileNotFoundError:
        print(f"The specified program '{program}' could not be found")
        return False


def running_program(program,arguments,encoding):
    if arguments == [] and encoding == "":
        print(f"Running program '{program}' without any arguments and no encoding")
        if check_program(program) is False:
            exit()
        p = subprocess.run([program], capture_output=True)
        print(f"The program finished with exit code {p.returncode}")
        output = p.stdout
        errors = p.stderr
        if errors:
            print("The program produced the following error output: ")
            print(errors)
        if output:
            print("The program produced the following standard output: ")
            print(output)


    elif arguments == [] and encoding != "":
        print(f"Running program '{program}' without any arguments and encoding '{encoding}'")
        if encoding != "" and check_encoding(encoding) is True:
            if check_program(program) is False:
                exit()
            p = subprocess.run([program], capture_output=True, encoding=encoding)
            print(f"The program finished with exit code {p.returncode}")
            output = p.stdout
            errors = p.stderr
            if errors:
                print("The program produced the following error output: ")
                print(errors)
            if output:
                print("The program produced the following standard output: ")
                print(output)


    elif arguments != [] and encoding == "":
        print(f"Running program '{program}' with arguments {arguments} and no encoding")
        if check_program(program) is False:
            exit()
        p = subprocess.run([program, *arguments], capture_output=True)
        print(f"The program finished with exit code {p.returncode}")
        output = p.stdout
        errors = p.stderr
        if errors:
            print("The program produced the following error output: ")
            print(errors)
        if output:
            print("The program produced the following standard output: ")
            print(output)


    elif arguments != [] and encoding != "":
        print(f"Running program '{program}' with arguments {arguments} and encoding '{encoding}'")
        if encoding != "" and check_encoding(encoding) is True:
            if check_program(program) is False:
                exit()
            p = subprocess.run([program, *arguments], capture_output=True, encoding=encoding)
            print(f"The program finished with exit code {p.returncode}")
            output = p.stdout
            errors = p.stderr
            if errors:
                print("The program produced the following error output: ")
                print(errors)
            if output:
                print("The program produced the following standard output: ")
                print(output)


program=input("Enter program or press ENTER to exit: ")
if program=="":
    exit(0)
arguments=[]
argument=input("Enter argument or press ENTER to skip: ")
while argument!="":
    arguments.append(argument)
    argument = input("Enter argument or press ENTER to skip: ")
encod=input("Enter encoding or press ENTER to skip: ")

running_program(program,arguments,encod)

